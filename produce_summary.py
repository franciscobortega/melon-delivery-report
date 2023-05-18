def format_and_print_deliveries(day):
    # the day argument is used to dynamically set title per day
    print(f"Day {day}")

    # file is opened dynamically by using fstring with the day parameter
    the_file = open(f"um-deliveries-day-{day}.txt")

    # each line in the file is looped over
    for line in the_file:
        # any whitespace to right of last character is stripped
        line = line.rstrip()
        # a list of words is made using '|' as the delimiter for each line from the txt file
        words = line.split('|')

        # each item in the list is assigned to an appropriate variable
        melon = words[0]
        count = words[1]
        amount = words[2]

        # the line is output in a formatted statement for each iteration
        print(f"Delivered {count} {melon}s for total of ${amount}")

    # file is closed
    the_file.close()

format_delivery(1)
format_delivery(2)
format_delivery(3)
