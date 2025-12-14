---
data: 'export host_path=`sed -n ''s/.*\perdir=\([^,\]*\).*/\1/p'' /etc/mtab`'
tags:
  - parsing
type: command
executor: bash
platforms:
  - Linux
id: 54d44093-ec33-46f9-8cc3-4a35a07f28d3
created_at: '2025-12-14T04:08:48.056Z'
updated_at: '2025-12-14T04:08:48.056Z'
verified: false
validated: true
submitted: true
---
# Export Host Path from Mtab

## Command

```bash
export host_path=`sed -n 's/.*\perdir=\([^,\]*\).*/\1/p' /etc/mtab`
```

## Description

Parses /etc/mtab to extract host perdir path for file operations.

## Parameters

None.

## Examples

### Basic Usage

```bash
export host_path=`sed -n 's/.*\perdir=\([^,\]*\).*/\1/p' /etc/mtab`
```

## Expected Output

host_path set to e.g., /host/path.

## Related

- [[commands/set-cgroup-release-agent]]
