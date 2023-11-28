import datetime

hours = 496
lesson_length = 4
days = int(hours/lesson_length)

course_date_list = []
cancelled_dates = [
    datetime.datetime(2023,12,25),
    datetime.datetime(2023,12,26),
    datetime.datetime(2024,1,1),
    datetime.datetime(2024,3,11),
    datetime.datetime(2024,4,1),
    datetime.datetime(2024,5,1),
    datetime.datetime(2024,6,24),
]

lesson_date = datetime.datetime(2023,12,18)
hours_temp = 0

while len(course_date_list) < days:
    weekday = lesson_date.isoweekday()
    if weekday in (1,2,3,4):
        if lesson_date in cancelled_dates:
            lesson_date = lesson_date + datetime.timedelta(days=1)
        else:
            course_date_list.append(lesson_date)
            lesson_date = lesson_date + datetime.timedelta(days=1)
            hours_temp += 4
    else:
        lesson_date = lesson_date + datetime.timedelta(days=3)



for day in course_date_list:
    print(day.strftime("%Y - %B - %d - %A"))
