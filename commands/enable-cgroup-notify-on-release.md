---
data: echo 1 > /tmp/cgrp/x/notify_on_release
tags:
  - cgroup
type: command
executor: bash
platforms:
  - Linux
id: fd430c11-5e04-4473-8963-d0446c957f57
created_at: '2025-12-14T04:08:48.060Z'
updated_at: '2025-12-14T04:08:48.060Z'
verified: false
validated: true
submitted: true
---
# Enable Cgroup Notify on Release

## Command

```bash
echo 1 > /tmp/cgrp/x/notify_on_release
```

## Description

Activates release agent trigger for root execution.

## Parameters

None specific.

## Examples

### Basic Usage

```bash
echo 1 > /tmp/cgrp/x/notify_on_release
```

## Expected Output

Value set to 1.

## Related

- [[commands/setup-cgroup-for-root-execution]]
