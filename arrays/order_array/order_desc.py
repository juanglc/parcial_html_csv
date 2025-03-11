def order_desc_date(array):
    array = sorted(array, key=lambda x: x[0], reverse=True)
    return array

def order_desc_dept(array):
    array = sorted(array, key=lambda x: x[2], reverse=True)
    return array

def order_desc_muni(array):
    array = sorted(array, key=lambda x: x[4], reverse=True)
    return array

def order_desc_cant(array):
    array = sorted(array, key=lambda x: float(x[5]), reverse=True)
    return array