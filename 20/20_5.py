# БСБО-05-19 Савранский С.

def lucky(ticket):
    def _sum(num):
        num = str(num)
        x = list(map(int, num))
        return sum(x[:3]) == sum(x[3:])

    return 'Счастливый' if _sum(ticket) == _sum(lastTicket) else 'Несчастливый'
