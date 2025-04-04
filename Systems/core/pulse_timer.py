import datetime

LAUNCH_DATE = datetime.datetime.utcnow()

def months_since_launch():
    now = datetime.datetime.utcnow()
    diff = (now.year - LAUNCH_DATE.year) * 12 + (now.month - LAUNCH_DATE.month)
    return diff

def should_liberate(lib_months: int):
    return months_since_launch() >= lib_months
