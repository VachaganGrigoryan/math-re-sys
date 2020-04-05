
class MathErrors:

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        try:
            return self.cls(*args, **kwargs)
        except:
            return None