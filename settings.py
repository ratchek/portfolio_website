TEMPLATE_DIR = "templates"
STATIC_DIR = "assets"
SRC_DIR = "src"
OUTPUT_DIR = "output"

# Tuples of (font awesome icon, href, string to display)
SOCIAL_LINKS = [
    ("solid fa-envelope", "#", "Email me"),
    ("brands fa-linkedin", "https://www.linkedin.com/in/thomas-raczkowski/", "LinkedIn"),
    ("brands fa-github", "https://github.com/ratchek", "Github"),
    ("solid fa-file", "assets/Thomas-Raczkowski-resume.pdf", "Download my resume"),
]

# List of projects in the 'django' category
DJANGO_PROJECTS = [
    {
        "title": "Door2Door",
        "id": "door2door",
        "blurb": "<p>An online tracking system for real estate canvasing built in Django. Integrates the NYC Housing Preservation & Development database to speed up search for property owners.</p>",
        "main_image": "d2d-main.webp",
        "github_link": "https://github.com/ratchek/door2door",
        "project_link": "https://door2door.nyc/",
        "gallery": [
            "d2d-2.webp",
            "d2d-4.webp",
            "d2d-5.webp",
            "d2d-1.webp",
            "d2d-3.webp",
        ],
    },
    {
        "title": "OLC",
        "id": "olc",
        "blurb": "<p>Ported a static website into a Django webapp to increase ease of use, security, and loading times. The new website allows for administrators to login and dynamically upload content like parish forms and weekly bulletins. </p>",
        "main_image": "olc-2.webp",
        "project_link": "https://olc-brooklyn.com/",
        "gallery": [
            "olc-1.webp",
            "olc-2.webp",
            "olc-3.webp",
        ],
    },
]

# List of projects in the 'django' category
OPEN_SOURCE_PROJECTS = [
    {
        "title": "Vorta",
        "id": "vorta",
        "blurb": "<p>Vorta is an open-source GUI interface for a deduplication backup tool called Borg. I created a development mode which sandboxes settings and temporary files during development from the operating system's main instance of the program. This is useful for developers that want to work on the software without having to manually backup the settings and files of the instance they use to perform the actual backups on their computers.</p> <p> I also submitted a PR that fixed a bug during the development setup process and I updated the website's contribution guide to include omitted steps improving the chances that new developers will stick with the project instead of getting discouraged.</p>",
        "main_image": "vorta-main.gif",
        "github_link": "https://github.com/borgbase/vorta/commits?author=ratchek",
        "project_link": "https://vorta.borgbase.com/",
        "gallery": [],
    },
]

# List of projects in the 'django' category
MISC_PROJECTS = [
    {
        "title": "Colornote to Joplin",
        "blurb": "<p>This is a script that allows you to import notes from Colornote into Joplin. The main selling point is that it preserves the creation and modification dates for each note as well as the folder structure. It also allows for batch importing</p>",
        "main_image": "d2d-main.webp",
        "github_link": "https://github.com/ratchek/colornote_to_joplin",
    },
    {
        "title": "Gesture Counter",
        "blurb": "<p>A Python program that funcions as a hands free counter. Controlled with head gestures.Uses cv2 and dlib</p>",
        "main_image": "d2d-main.webp",
        "github_link": "https://github.com/ratchek/gesture_counter_2.0",
    },
    {
        "title": "o2cm Database",
        "blurb": "<p>A program created to aid the staff of the Big Apple Dance Competition in putting together a comprehensive list of their competitors.</p>",
        "main_image": "d2d-main.webp",
        "github_link": "https://github.com/ratchek/o2cmDatabase",
    },
    {
        "title": "Watson integration for Telegram",
        "blurb": "<p>Backend for a Telegram bot that allows you to query instances of Watson Assistant and Watson Discovery in real time. Written in NodeRed.</p>",
        "main_image": "d2d-main.webp",
        "github_link": "https://github.com/ratchek/ChemicalPlantSafetyAssistant",
    },
    {
        "title": "Anki Person Scraper",
        "blurb": "<p>Input a list of people and you get an Anki deck of their names, photos, and short intros. Scrapes wikipedia, so make sure the person has a wikipedia page. </p>",
        "main_image": "d2d-main.webp",
        "github_link": "https://github.com/ratchek/anki-person-scraper",
    },
    {
        "title": "Goal and Reward Tracker",
        "blurb": "<p>A simple webapp used to track goals, rewards, and goal timelines.</p>",
        "main_image": "d2d-main.webp",
        "github_link": "https://github.com/ratchek/GoalCounter",
    },
]

# List of templates to render
TEMPLATE_LIST = [
    "index.html",
    "contact.html",
    "django.html",
    "misc.html",
    "opensource.html",
]

# First item contains the project with all the info.
# Second item is the page in which it lives. (needed to create a hyperlink)
SIDEBAR_LIST = [
    (DJANGO_PROJECTS[0], "django.html"),
    (OPEN_SOURCE_PROJECTS[0], "opensource.html"),
]
