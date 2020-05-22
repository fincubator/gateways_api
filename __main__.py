"""Main entry point to run in dev without docker and gunicorn
    $ python .
"""

from app import *
web.run_app(gw_app)
