import re
def REGEXP(expr, item):
    reg = re.compile(expr, re.I)
    return reg.search(item) is not None