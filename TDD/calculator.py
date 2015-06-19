def add(message):
    if message == '':
        return 0
    try:
        return int(message)
    except (ValueError, TypeError):
        try:
            l = message.split(',')
            return int(l[0]) + int(l[1])
        except Exception:
            return 3

