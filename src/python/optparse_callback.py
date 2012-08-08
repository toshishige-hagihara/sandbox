from datetime import datetime
from optparse import OptionParser

def to_date(option, opt, value, parser, date_format):
    try:
        date = datetime.strptime(value, date_format).date()
    except ValueError, e:
        parser.error(e.message)
    setattr(parser.values, option.dest, date)

parser = OptionParser()
parser.add_option('-d', type='string', dest='date',
        help='ISO 8601 date format',
        action='callback', callback=to_date,
        callback_kwargs={'date_format': '%Y-%m-%d'})
(options, args) = parser.parse_args()
print options.date
