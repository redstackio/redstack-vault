---
id: 81dd1943-ca2e-47a3-afad-67cabf5b078c
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:04.297313+00:00'
updated_at: '2023-04-10T20:25:55.316905+00:00'
platforms:
  - Linux
tags:
  - password-spraying
  - smb
validated: true
---

# crackmapexec-smb-spray-with-generated-mask

## Code

```bash
crackmapexec smb 10.0.0.1/24 -u Administrator -p `(./mp64.bin Pass@wor?l?a)`
```

## Description

This code snippet executes CrackMapExec to spray generated passwords from a mask against SMB in a network range, using mp64.bin for on-the-fly password creation. It's a concise way to test patterned passwords like yearly variations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.0.0.1/24 | Target IP range | 192.168.1.0/24 |
| Administrator | Username | guest |
| Pass@wor?l?a | Password mask for mp64.bin | Season2023?d?l |

## Usage

Run on a Linux host with CrackMapExec and mp64.bin. Use before broader enumeration to quickly validate common patterns. Integrate into scripts for automated spraying.

## Detection

- Network logs showing multiple SMB auth attempts from one source (port 445).
- Process monitoring for crackmapexec or mp64.bin execution.
- Failed login events (4625) patterned by time/IP.

## Related

- [[procedures/Password-Spraying-with-Pre-Generated-Passwords]]
- [[tools/CrackMapExec]]
