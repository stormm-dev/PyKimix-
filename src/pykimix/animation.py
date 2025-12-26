import time

class Tween:
    def __init__(self, obj, attr, start, end, duration, easing=None):
        self.obj = obj
        self.attr = attr
        self.start = start
        self.end = end
        self.duration = duration
        self.easing = easing
        self.start_time = time.time()

    def update(self):
        t = time.time() - self.start_time
        if t > self.duration:
            setattr(self.obj, self.attr, self.end)
        else:
            value = self.start + (self.end - self.start) * (t / self.duration)
            setattr(self.obj, self.attr, value)