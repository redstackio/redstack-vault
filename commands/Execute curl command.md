---
id: 6517b030-5a27-4b00-8e68-1cb2adc4216c
name: Execute Curl Command
type: command
executor: bash
data: "from shlex import quote,split\nimport sys\nimport subprocess\n\nif __name__==\"\
  __main__\":\n    command = ['curl']\n    command = command + split(sys.argv[1])\n\
  \    print(command)\n    r = subprocess.Popen(command)"
output: null
created_at: '2023-04-06T03:55:54.012204+00:00'
updated_at: '2023-04-06T03:55:54.027705+00:00'
---

# Execute Curl Command

```bash
from shlex import quote,split
import sys
import subprocess

if __name__=="__main__":
    command = ['curl']
    command = command + split(sys.argv[1])
    print(command)
    r = subprocess.Popen(command)
```


