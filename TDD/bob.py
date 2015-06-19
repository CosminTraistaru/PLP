def hey(message):
    if message.isupper():
        return 'Whoa, chill out!'
    if message.encode('utf8').endswith('?'):
        return 'Sure.'
    if message.encode('utf8').isspace() or message == '':
        return 'Fine. Be that way!'
    return 'Whatever.'
