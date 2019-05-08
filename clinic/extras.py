from datetime import datetime, timedelta


def check_date(date):
    next_date = datetime.strptime(date.replace('-', ''), "%Y%m%d").date()

    if next_date > datetime.now().date():
        return True
    return False
