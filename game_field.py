for row in range(amount_of_days):
    row_list = []
    for col in range(hour_per_day):
        row_list.append('free')
    schedule.append(row_list)
list_print(schedule)