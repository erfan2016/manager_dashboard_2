from DateTimePersian import DateTimePersian

def decorator_logs(func):
    def wrapper(*args, **kwargs):
        file = open('runTime.log', '+a')
        date = DateTimePersian()
        file.write(f'{date} - {func.__name__} is running...')
        func(*args, **kwargs)
    return wrapper

@decorator_logs
def login_panel(username, password, time):
    pass


get_time = DateTimePersian()
login_panel("asd", 125, get_time)
print(get_time.getYearE())