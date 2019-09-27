from __future__ import print_function
from builtins import str  # Needed for back-compatibility
try:
    from io import StringIO as stringIO # for Python 3 from
except ImportError:
    import cStringIO as stringIO ## for Python 2
from builtins import str
import sys

PY3 = sys.version_info[0] >= 3
if PY3:
    # mixin class for Python3 supporting __cmp__
    class PY3__cmp__(object):
        def __eq__(self, other):
            return self.__cmp__(other) == 0

        def __ne__(self, other):
            return self.__cmp__(other) != 0

        def __gt__(self, other):
            return self.__cmp__(other) > 0

        def __lt__(self, other):
            return self.__cmp__(other) < 0

        def __ge__(self, other):
            return self.__cmp__(other) >= 0

        def __le__(self, other):
            return self.__cmp__(other) <= 0
else:
    class PY3__cmp__(object):
        pass
