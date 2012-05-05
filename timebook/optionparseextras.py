from optparse import Option, OptionValueError
from copy import copy
from datetime import datetime

def check_date(option, opt, value):
    try:
        return datetime.strptime(value, "%Y/%m/%d")
    except ValueError:
        raise OptionValueError(
            "option %s: invalid date value: %r. Should have a format like \"YYYY/MM/DD\"" % (opt, value))

class DateOption (Option):
    TYPES = Option.TYPES + ("date",)
    TYPE_CHECKER = copy(Option.TYPE_CHECKER)
    TYPE_CHECKER["date"] = check_date

