import re

def filter_by_date(array, date):
    result = []
    for x in array:
        if x[0] == date:
            result.append(x)
    return result

def filter_by_dept(array, dept):
    pattern = re.compile(dept, re.IGNORECASE)
    result = []
    for x in array:
        if pattern.search(x[2]):
            result.append(x)
    return result

def filter_by_muni(array, muni):
    pattern = re.compile(muni, re.IGNORECASE)
    result = []
    for x in array:
        if pattern.search(x[4]):
            result.append(x)
    return result

def filter_by_cant(array, cant):
    result = []
    for x in array:
        if x[5] == cant:
            result.append(x)
    return result