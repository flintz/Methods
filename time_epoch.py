#Function with no arguments but with a return value (epoch time)
#Re(John Philip Jones)
import time
def get_time():
    epoch_time = time.time()
    total_seconds = int(epoch_time)
    current_second = total_seconds % 60
    total_minutes = total_seconds // 60
    current_minute = total_minutes % 60
    total_hours = total_minutes // 60
    current_hours = total_hours % 24
    time_now = str(current_hours) + ":" + str(current_minute) + ":" + str(current_second)
    return time_now

current_time = get_time()
print(current_time)
