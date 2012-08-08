from copy import copy
from datetime import datetime
from optparse import Option, OptionValueError, OptionParser
import re

### Constants
DATE_FORMATE_REGX = re.compile(r'.*format=\((.+)\).*')

### Implementation
def check_date(option, opt, value):
    try:
        m = DATE_FORMATE_REGX.match(option.help)
        if m is None:
            raise OptionValueError('''Please specify date format in help text as
                                   following: ...format=(%Y-%s-%m)...''')
        return datetime.strptime(value, m.group(1))
    except ValueError, e:
        raise OptionValueError(str(e))

class MyOption(Option):
    TYPES = Option.TYPES + ('date',)
    TYPE_CHECKER = copy(Option.TYPE_CHECKER)
    TYPE_CHECKER['date'] = check_date

### Main
parser = OptionParser(option_class=MyOption)
parser.add_option('-d', type='date', dest='date',
                  help='format=(%Y-%m-%d)')
(options, args) = parser.parse_args()

print options.date
