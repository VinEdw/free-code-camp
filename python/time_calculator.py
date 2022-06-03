# https://replit.com/@VincentEdwards1/boilerplate-time-calculator

# It is a function that takes in two required parameters and one optional parameter: 
# a start time in the 12-hour clock format (ending in AM or PM), 
# a duration time that indicates the number of hours and minutes, 
# and (optional) a starting day of the week, case insensitive. 
# The function should add the duration time to the start time and return the result.

def add_time(start: str, duration: str, day: str = ''):
    #this dict will hold the values extracted from start (the start time)
    s = {'hr':int(start.split(':')[0]), 'min':int(start.split(':')[1][:2]), 'meridiem':start.split()[1], 'days':0}

    #convert the hour to the 24 hr format (military time); this makes calculations easier later on; we will convert back to the AM/PM format at the end
    if s['meridiem'] == 'PM' and s['hr'] != 12:
        s['hr'] += 12
    elif s['hr'] == 12:
        s['hr'] = 0

    #this dict will hold the values extracted from duration (the time duration)
    d = {'hr':int(duration.split(':')[0]), 'min':int(duration.split(':')[1])}
    
    #the day will be made all lowercase except for the first letter, which should be uppercase
    day = day.lower().capitalize()

    #start adding the time from d to s; store the results in s
    #add the minutes
    s['min'] += d['min']
    #if the result is greater than 59, roll over to hours
    if s['min'] > 59:
        s['hr'] += s['min'] // 60
        s['min'] %= 60
    
    #add the hours 
    s['hr'] += d['hr']
    #if the result is greater than 23, roll over to days
    if s['hr'] > 23:
        s['days'] += s['hr'] // 24
        s['hr'] %= 24

    #convert the hour back to the AM/PM format and assign the proper meridiem
    if s['hr'] >= 12:
        s['meridiem'] = 'PM'
        if s['hr'] != 12:
            s['hr'] -= 12
    else:
        s['meridiem'] = 'AM'
        if s['hr'] == 0:
            s['hr'] = 12

    #start creating the new_time str, what the function will return
    #insert 'hh:mm MM'
    new_time = f"{s['hr']}:{str(s['min']).rjust(2, '0')} {s['meridiem']}"

    #if a day was specified in the arguments, insert the correct day
    if day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        i = days_of_week.index(day)
        i += s['days']
        i %= 7
        new_time += f", {days_of_week[i]}"

    #if it is a different day, say how many days have passed 
    if s['days']:
        dayWarning = ' '
        if s['days'] == 1:
            dayWarning += '(next day)'
        else:
            dayWarning += f"({s['days']} days later)"
        new_time += dayWarning

    return new_time


if __name__ == "__main__":
    exArgs = ("11:06 PM", "2:02", 'Monday')
    print(add_time(*exArgs))
    print(add_time('12:01 AM', '60:1', 'Saturday'))
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))