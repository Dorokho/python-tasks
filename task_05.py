from datetime import datetime, timedelta

def date_in_future(integer):
    now = datetime.now()

    if isinstance(integer, int):
        future_date = now + timedelta(days=integer)
        return future_date.strftime('%d-%m-%Y %H:%M:%S')
    else:
        return now.strftime('%d-%m-%Y %H:%M:%S')
    
print(date_in_future([]))
print(date_in_future(2))
print(date_in_future(5))
