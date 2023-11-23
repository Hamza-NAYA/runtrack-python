
def time_to_text(time):
    new_time = time / 60
    new_time_int = int(new_time)
    new_time_float = new_time - new_time_int
    new_time_minute_float = new_time_float * 60
    new_time_minute = int(new_time_minute_float)

    print(str(new_time_int) + " heures et " + str(new_time_minute) + " minutes")


time_to_text(356)