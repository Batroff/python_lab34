# БСБО-05-19 Савранский С.

old_msgs = []


def print_only_new(message):
    global old_msgs

    if message in old_msgs:
        return

    old_msgs.append(message)
    print(message)
