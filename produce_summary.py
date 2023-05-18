def format_and_print_deliveries(day):
    print(f"Day {day}")

    the_file = open(f"um-deliveries-day-{day}.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")

    the_file.close()

format_delivery(1)
format_delivery(2)
format_delivery(3)
