PLUGIN_PATHS = ['pelican-plugins'] 
PLUGINS = ['assets', 'pelican-toc', 'latex','neighbors']
AUTHOR = 'A cast of tens'
SITENAME = 'Eddy and Rivas Labs Resource Page'
SITEURL = 'eddyrivaslab.github.io'

PATH = 'content'
THEME = "./astrochelys"
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))
TIMEZONE = 'America/New_York'
PAGE_PATHS=['pages']
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
