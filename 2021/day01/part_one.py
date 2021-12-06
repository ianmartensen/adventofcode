with open('sea_report.txt') as report:
    measurements = [m.replace('\n', '') for m in report.readlines()]


counter = 0
for i, val in enumerate(measurements):
    if i == 0:
        pass
    else: 
        if int(val) > int(measurements[i-1]):
            counter += 1