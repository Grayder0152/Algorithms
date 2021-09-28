def init_list(n: int, node) -> CircularSinglyLinkedList:
    number_list = CircularSinglyLinkedList()

    number_list.head_val = TicketNumber('1') if node is TicketNumber else Child('Child_1')
    tick = number_list.head_val

    for number in range(2, n + 1):
        tick.next_val = TicketNumber(str(number)) if node is TicketNumber else Child(f'Child_{number}')
        tick = tick.next_val

    tick.next_val = number_list.head_val

    return number_list


def get_children_ticket_numbers(count, children_recount, numbers_recount):
    result = {}

    children = init_list(count, Child)
    tickets = init_list(count, TicketNumber)

    children_index = 0
    tickets_index = 0

    i = 0
    while i != count:
        children_index += children_recount
        tickets_index += numbers_recount

        result[children.get_by_index(children_index).data_val] = tickets.get_by_index(tickets_index).data_val
        i += 1

    return result


if __name__ == '__main__':
    r = get_children_ticket_numbers(5, 1, 2)
    print(r)
