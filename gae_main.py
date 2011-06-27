import sys
from os.path import dirname, abspath, join


PROJECT_DIR = join(abspath(dirname(__file__)), "testapp")

if PROJECT_DIR not in sys.path or sys.path.index(PROJECT_DIR) > 0:
    while PROJECT_DIR in sys.path:
        sys.path.remove(PROJECT_DIR)
    sys.path.insert(0, PROJECT_DIR)

import djangoappengine.main.main
djangoappengine.main.main.main()
