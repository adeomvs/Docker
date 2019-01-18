#!/usr/bin/env python
# This is a generic launcher for FlaskIT2 application
# Could be use as a WSGI entry point
# or directly call from the command line (with a builtin web server) for testing

import re
import sys
import os

try:
    from flaskit.app import main, wsgi, check_wsgi
except ImportError, e:
    # activate local virtualenv (if defined)
    os.chdir(os.path.dirname(os.path.realpath("%s/.." % __file__)))
    activate_this = 'venv/bin/activate_this.py'
    if os.path.exists(activate_this):
        execfile(activate_this, dict(__file__=activate_this))
    from flaskit.app import main, wsgi, check_wsgi

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
elif check_wsgi(__file__, __name__):
    # on wsgi mode, application should be defined
    application = wsgi(__file__, __name__)
else:
    print "Unsupported execution mode (%s)" % __name__
    sys.exit(1)
    