---
id: cmd-uuid-10
data: hostname
tags:
  - recon
  - system
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.172Z'
verified: false
validated: true
submitted: true
---
# hostname

## Command

```bash
hostname
```

## Description

Retrieves the system's hostname for constructing the FTP bypass URL.

## Parameters

None.

## Examples

### Basic Usage

```bash
hostname
```

### Advanced Usage

```bash
hostname -f
```

## Expected Output

Hostname string, e.g., 'g64'.

## Related

- [[Related Procedure: Send-Crafted-HTTP-Request-to-Trigger-Heap-Overflow]]
