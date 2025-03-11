def order_asc_date(array):
    array = sorted(array, key=lambda x: x[0])
    return array

def order_asc_dept(array):
    array = sorted(array, key=lambda x: x[2])
    return array

def order_asc_muni(array):
    array = sorted(array, key=lambda x: x[4])
    return array

def order_asc_cant(array):
    array = sorted(array, key=lambda x: float(x[5]))
    return array