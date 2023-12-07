from jinja2 import Environment
import os
import shutil
from jinja2 import FileSystemLoader
from os.path import join, exists, getmtime
import settings


# Class used to generate the site from the templates
class SiteGenerator(object):
    # Instantiate the dirs and templates
    # The structure is assumed to be as follows
    # project_root_dir
    # ├── generator.py
    # └── src_dir
    #     ├── static_dir
    #     |   ├── static_assets
    #     |   └── static_assets
    #     └── templates_dir
    #         ├── template_1.html
    #         └── template_2.html

    def __init__(
        self, static_dir="static", src_dir="src", template_dir="templates", output_dir="output", template_list=None
    ):
        if template_list is None:
            self.template_list = ["index.html"]
        else:
            self.template_list = template_list
        self.template_dir = template_dir
        self.static_dir = static_dir
        self.src_dir = src_dir
        self.output_dir = output_dir

    # Get the root directory of the script.
    def _root(self):
        return os.path.dirname(os.path.abspath(__file__))

    # Delete the output dir if exists
    # Create a new output dir
    def clean(self):
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.mkdir(os.path.join(self._root(), self.output_dir))

    # Generate the site
    def generate(self, **kwargs):
        # Clean up output dir if it exists
        self.clean()

        # Copy static files to output dir
        if self.static_dir is not None:
            shutil.copytree(
                os.path.join(self._root(), self.src_dir, self.static_dir),
                os.path.join(self._root(), self.output_dir, self.static_dir),
            )

        # Load Jinja2 environment
        env = Environment(loader=FileSystemLoader(os.path.join(self._root(), self.src_dir, self.template_dir)))

        # For every template in the template_dir
        for template_name in self.template_list:
            # Generate an appropriate html file in the outputdir with jinja
            with open(os.path.join(self._root(), self.output_dir, template_name), "w") as f:
                template = env.get_template(template_name)
                content = template.render(**kwargs)
                f.write(content)

        return True


# Main execution block.
if __name__ == "__main__":
    # Instantiate site generator
    sb = SiteGenerator(
        static_dir=settings.STATIC_DIR,
        src_dir=settings.SRC_DIR,
        template_dir=settings.TEMPLATE_DIR,
        output_dir=settings.OUTPUT_DIR,
        template_list=settings.TEMPLATE_LIST,
    )

    # Generate the site
    sb.generate(
        socials=settings.SOCIAL_LINKS,
    )
