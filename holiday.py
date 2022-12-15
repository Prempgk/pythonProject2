from datetime import datetime, timedelta
import calendar
import datetime


def weekday_count(start_date, end_date):
    week = {}
    for i in range((end_date - start_date).days):
        day = calendar.day_name[(start_date + datetime.timedelta(days=i + 1)).weekday()]
        week[day] = week[day] + 1 if day in week else 1

    return week


def find(startdate, enddate, sec_sat):
    startdate = datetime.datetime.strptime(startdate, '%d/%m/%Y')
    enddate = datetime.datetime.strptime(enddate, '%d/%m/%Y')
    print(startdate)
    print(enddate)
    no_days = enddate - startdate
    print(no_days)
    hlist = []
    sun = []
    sat = []
    for i in range(no_days.days + 1):
        date = startdate + timedelta(days=i)
        hlist.append(date)
    for h in hlist:
        if h.isoweekday() == 7:
            sun.append(h.date())
        if h.isoweekday() == 6:
            if h.date() in sec_sat:
                sat.append(h.date())
    return len(sat) + len(sun)


def secsat(start_month, end_month, syear, eyear):
    sec_sat = []

    for month in range(start_month, 13):
        cal = calendar.monthcalendar(syear, month)
        first_week = cal[0]
        second_week = cal[1]
        third_week = cal[2]

        if first_week[calendar.SATURDAY]:
            holi_day = second_week[calendar.SATURDAY]
            sec_sat.append(datetime.date(syear, month, holi_day))
        else:
            holi_day = third_week[calendar.SATURDAY]
            sec_sat.append(datetime.date(syear, month, holi_day))

    for month in range(1, end_month):
        cal = calendar.monthcalendar(eyear, month)
        first_week = cal[0]
        second_week = cal[1]
        third_week = cal[2]

        if first_week[calendar.SATURDAY]:
            holi_day = second_week[calendar.SATURDAY]
            sec_sat.append(datetime.date(eyear, month, holi_day))
        else:
            holi_day = third_week[calendar.SATURDAY]
            sec_sat.append(datetime.date(eyear, month, holi_day))
    val = find('13/01/2023', '17/01/2023', sec_sat)
    return [len(sec_sat), val]


start_date = datetime.datetime.strptime("01/06/2022", '%d/%m/%Y')
end_date = datetime.datetime.strptime("01/04/2023", '%d/%m/%Y')
start_month = start_date.month
end_month = end_date.month
syear = start_date.year
eyear = end_date.year
a = weekday_count(start_date, end_date)
b = secsat(start_month, end_month, syear, eyear)
print(a)
for j in a.keys():
    det = a[j]
    if j == 'Saturday':
        a[j] = a[j] - b[0]
    if j == 'Sunday':
        a[j] = a[j] - a[j]

print(sum(a.values())+b[1])
