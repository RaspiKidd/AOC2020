FILENAME="input.txt"

def get_fields(FILENAME=FILENAME):
    field_keys = list() # the order is important, so we will keep the field keys in a list
    field_valid_ranges = list() # as we add the field keys, we will store the pair of pair of numbers (because of or) that describe the valid range for each field
    personal_ticket = None
    nearby_tickets = list()

    # read field and its valid range
    with open(FILENAME, "r") as f:
        fields_mode = True
        personal_ticket_mode = False
        nearby_tickets_mode = False

        for line in f:
            if line == '\n':
                if fields_mode:
                    fields_mode = False
                    personal_ticket_mode = True
                elif personal_ticket_mode:
                    personal_ticket_mode = False
                    nearby_tickets_mode = True
                continue

            elif line[-1] == '\n':
                line = line[:-1]

            if fields_mode:
                field_valid_range = list()
                line = line.split(": ")

                field_keys.append(line[0]) # this is the field key

                valid_ranges_raw = line[1].split(" or ")

                for raw_range in valid_ranges_raw:
                    valid_range = raw_range.split("-")
                    valid_range[0] = int(valid_range[0])
                    valid_range[1] = int(valid_range[1])

                    field_valid_range.append(tuple(valid_range))

                field_valid_ranges.append(tuple(field_valid_range))
            elif personal_ticket_mode:
                if line[0] == 'y':
                    continue
                else:
                    personal_ticket = line.split(',')

                    for i in range(len(personal_ticket)):
                        personal_ticket[i] = int(personal_ticket[i])

            elif nearby_tickets_mode:
                if line[0] == 'n':
                    continue
                else:
                    nearby_ticket = line.split(',')

                    for i in range(len(nearby_ticket)):
                        nearby_ticket[i] = int(nearby_ticket[i])

                    nearby_tickets.append(nearby_ticket)


    return field_keys, field_valid_ranges, personal_ticket, nearby_tickets

def is_in_range(number, range):
    return number >= range[0] and number <= range[1]

def calculate_scanning_error_rate(tickets, field_keys, field_valid_ranges):
    error_rate = 0
    invalid_tickets = list()
    for ticket in tickets:
        for i in range(len(ticket)):
            is_valid = False
            for field_valid_range in field_valid_ranges:
                if is_in_range(ticket[i], field_valid_range[0]) or is_in_range(ticket[i], field_valid_range[1]):
                    is_valid = True
                    break

            if not is_valid:
                error_rate += ticket[i]
                invalid_tickets.append(ticket)

    return error_rate, invalid_tickets

# Part 2
def determine_field_order(valid_nearby_tickets, field_keys, field_valid_ranges):
    ordered_fields = dict()

    # scan for each column of each ticket
    for i in range(len(field_keys)):
        ordered_fields[i] = list()
        for k in range(len(field_valid_ranges)):
            is_valid_field = True
            for ticket in valid_nearby_tickets:
                if not is_in_range(ticket[i], field_valid_ranges[k][0]) and not is_in_range(ticket[i], field_valid_ranges[k][1]):
                    is_valid_field = False
                    break

            if is_valid_field:
                ordered_fields[i].append(field_keys[k])

    is_ordered = False

    while not is_ordered:
        is_ordered = True
        for key, value in ordered_fields.items():
            if len(value) > 1:
                is_ordered = False
            elif len(value) == 1:
                for position in ordered_fields.keys():
                    if position != key and value[0] in ordered_fields[position]:
                        ordered_fields[position].remove(value[0])

    return ordered_fields

# Part 1
field_keys, field_valid_ranges, personal_ticket, nearby_tickets = get_fields()

error_rate, invalid_tickets = calculate_scanning_error_rate(nearby_tickets, field_keys, field_valid_ranges)

print(error_rate)


# Part 2

for invalid_ticket in invalid_tickets:
    nearby_tickets.remove(invalid_ticket)


ordered_fields = determine_field_order(nearby_tickets, field_keys, field_valid_ranges)

for key, value in ordered_fields.items():
    print(key, " -> ", value)

product = 1

for key, value in ordered_fields.items():
    if "departure" in ordered_fields[key][0]:
        product *= personal_ticket[key]

print(product)
