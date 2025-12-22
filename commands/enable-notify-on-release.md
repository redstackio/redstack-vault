---
id: new-uuid-for-enable-notify
name: enable-notify-on-release
type: command
executor: bash
data: echo 1 > /tmp/cgrp/x/notify_on_release
output: null
created_at: '2023-04-06T03:56:17.110150+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cgroup
verified: true
validated: true
---

# enable-notify-on-release

## Command

```bash
echo 1 > /tmp/cgrp/x/notify_on_release
```

## Description

Enables notify_on_release flag in the cgroup subgroup to trigger kernel execution of the release agent upon process exit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo 1 | Set flag to enabled | Yes |
| > /tmp/cgrp/x/notify_on_release | Target file | Yes |

## Examples

### Basic Usage

```bash
echo 1 > /tmp/cgrp/x/notify_on_release
```

## Expected Output

(No output; confirm with cat /tmp/cgrp/x/notify_on_release showing 1.)

## Related

- [[procedures/Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]
