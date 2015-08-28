import time


class Logger(object):

    levels = {
        'debug': 0,
        'info': 10,
        'warning': 20,
        'error': 30,
    }
    time_stamp = '{}'.format(time.strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, name=__name__, level='info'):
        self.name = name
        self.level = level

    def set_level(self, level):
        self.level = level

    def display_message(self, message):
        print(
            '{time_stamp} {name} {message}'.format(
                time_stamp=self.time_stamp,
                name=self.name,
                message=message
            )
        )

    def info(self, message):
        if self.levels[self.level] < 10:
            return
        self.display_message(message)

    def warning(self, message):
        if self.levels[self.level] < 20:
            return
        self.display_message(message)

    def error(self, message):
        if self.levels[self.level] < 30:
            return
        self.display_message(message)
