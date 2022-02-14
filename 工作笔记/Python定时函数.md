### Python常见问题

#### 基本数据类型操作

```python
python2

from threading import _Timer
def hello():
     print "hello, world"
class RepeatingTimer(_Timer): 
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)
t = RepeatingTimer(10.0, hello)
t.start()


python3 
from threading import Timer
def hello():
     print "hello, world"
class RepeatingTimer(Timer): 
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)
t = RepeatingTimer(10.0, hello)
t.start()
```

