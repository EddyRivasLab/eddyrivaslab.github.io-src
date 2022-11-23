PLUGIN_PATHS = ['pelican-plugins'] 
PLUGINS = ['assets', 'neighbors','render_math']
AUTHOR = 'A cast of tens'
SITENAME = 'Eddy and Rivas Labs Resource Page'
SITEURL = 'https://eddyrivaslab.github.io'

PATH = 'content'
THEME = "./customized"

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
USE_FOLDER_AS_CATEGORY=True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


ARTICLE_PATHS = ['author',]
ARTICLE_URL = 'author/{slug}.html'
ARTICLE_SAVE_AS = 'author/{slug}.html'
PAGE_PATHS = ['pages',]
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
