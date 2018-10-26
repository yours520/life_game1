from threading import Timer


class RepeatableTimer:
    def __init__(self, interval, trigger):
        '''
        将在主程序中初始化实例
        计时器以interval秒的频率触发
        trigger是个函数，计时器被触发时调用该函数
        '''
        self.interval = interval
        self.trigger = trigger

        pass

    def start(self):
        '''启动计时器，之后将以interval秒的间隔持续触发'''
        timer = Timer(self.interval, self.trigger)
        timer.start()
        pass
