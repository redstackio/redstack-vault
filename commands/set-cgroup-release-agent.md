---
data: echo "$host_path/cmd" > /tmp/cgrp/release_agent
tags:
  - cgroup
type: command
executor: bash
platforms:
  - Linux
id: 42676dfe-7339-4136-8ab2-3434aa94f2e9
created_at: '2025-12-14T04:08:48.053Z'
updated_at: '2025-12-14T04:08:48.053Z'
verified: false
validated: true
submitted: true
---
# Set Cgroup Release Agent

## Command

```bash
echo "$host_path/cmd" > /tmp/cgrp/release_agent
```

## Description

Configures script to run as root on cgroup release.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $host_path/cmd | Path to executable script | Yes |

## Examples

### Basic Usage

```bash
echo "$host_path/cmd" > /tmp/cgrp/release_agent
```

## Expected Output

Agent path written.

## Related

- [[commands/export-host-path-from-mtab]]
