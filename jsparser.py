from python-spidermonkey import Runtime
rt=Runtime()

class script(tags.BaseTag):
    def add_data(self, data):
        self.context.eval(data)

def jscall(context, func):
    def _f(evt):
        evt=tojsevt(evt)
        return context.eval_script(func+'(evt)')
    return _f