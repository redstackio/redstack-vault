---
id: e4701e2f-f540-4eec-8e90-990857055327
name: create-and-mount-cgroup
type: command
executor: bash
data: >-
  mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir
  /tmp/cgrp/x
output: null
created_at: '2023-04-06T03:56:17.110150+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cgroup
  - mount
verified: true
validated: true
---

# create-and-mount-cgroup

## Command

```bash
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
```

## Description

Creates a temporary directory, mounts the cgroup v1 filesystem with RDMA option, and sets up a subgroup for release agent configuration in privilege escalation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| mkdir /tmp/cgrp | Create mount point | Yes |
| mount -t cgroup | Mount cgroup filesystem type | Yes |
| -o rdma | Remount option for capabilities | Yes |
| cgroup /tmp/cgrp | Source and target | Yes |
| mkdir /tmp/cgrp/x | Create subgroup | Yes |

## Examples

### Basic Usage

```bash
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
```

## Expected Output

(No output on success; verify with ls /tmp/cgrp to see cgroup files like tasks, cgroup.procs.)

## Related

- [[procedures/Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]
