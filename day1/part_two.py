with open('sea_report.txt') as report:
    measurements = [int(m.replace('\n', '')) for m in report.readlines()]

counter = 0
current_sum = measurements[0] + measurements[1] + measurements[2]
for i, val in enumerate(measurements):
    if i == (len(measurements) - 3):
        window_sum = measurements[i] + measurements[i+1] + measurements[i+2]
        if window_sum > current_sum:
            counter += 1
        break
    
    if (measurements[i] + measurements[i+1] + measurements[i+2]) > current_sum:
        counter += 1

    current_sum = measurements[i] + measurements[i+1] + measurements[i+2]