TEMPLATE_DIR = "templates"
STATIC_DIR = "assets"
SRC_DIR = "src"
OUTPUT_DIR = "output"
TEMPLATE_LIST = [
    "index.html",
    "contact.html",
    "django.html",
]

# Tuples of (font awesome icon, href, string to display)
SOCIAL_LINKS = [
    ("solid fa-envelope", "#", "Email me"),
    ("brands fa-linkedin", "#", "LinkedIn"),
    ("brands fa-github", "#", "Github"),
    ("solid fa-file", "#", "Download my resume"),
]

DJANGO_PROJECTS = [
    {
        "title": "Door2Door",
        "blurb": "<p>An online tracking system for real estate canvasing built in Django. Integrates the NYC Housing Preservation & Development database to speed up search for property owners.</p>",
        "main_image": "d2d-main.png",
        "github_link": "https://github.com/ratchek/door2door",
        "project_link": "https://door2door.nyc/",
        "gallery": [
            "d2d-2.png",
            "d2d-4.png",
            "d2d-5.png",
            "d2d-1.png",
            "d2d-3.png",
        ],
    },
    {
        "title": "And I'm a freelance Django developer.",
        "blurb": "<p>Hi from the blurb!</p>",
        "main_image": "d2d-main.png",
        "github_link": "https://github.com/ratchek",
        "project_link": "https://www.google.com/",
        "gallery": ["d2d-1.png", "d2d-2.png", "d2d-3.png", "d2d-4.png", "d2d-5.png"],
    },
]
