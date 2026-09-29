import time
def timestamp():
    b=time.localtime()
    return f"[{b.tm_hour}:{b.tm_min}-{b.tm_mday}/{b.tm_mon}/{b.tm_year}]"