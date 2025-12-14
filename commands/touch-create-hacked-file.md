---
data: touch HACKED
tags:
  - file-creation
  - shell
type: command
output: Creates the file 'HACKED' if it doesn't exist
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.689Z'
id: f79e20c2-07eb-4f3e-96b5-ff0f077e777b
verified: false
validated: true
submitted: true
---
# touch-create-hacked-file

## Command

```bash
touch HACKED
```

## Description

Creates an empty file named HACKED on the filesystem, used here as a proof-of-concept for arbitrary command execution via injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `HACKED` | Filename to create or update timestamp | Yes |

## Examples

### Basic Usage

```bash
touch HACKED
```

### Advanced Usage

```bash
touch -a HACKED  # Update access time only
```

## Expected Output

No output on success; file is created with current timestamp.

## Related

- [[Related Procedure|procedures/Exploit-gity-RCE-with-Injected-Commands]]
