---
type: command
executor: bash
data: john --restore
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - hash-cracking
  - john
  - session
verified: true
validated: true
---

# john-restore-interrupted-session

## Command

```bash
john --restore
```

## Description

Restores the most recent John cracking session from its checkpoint file (~/.john/john.rec), allowing continuation of long-running tasks after interruption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --restore | Flag to load and resume the last session | Yes |

## Examples

### Basic Usage

```bash
john --restore
```

### Advanced Usage

```bash
john --restore --session=backup.rec
```

## Expected Output

Loaded 1 previous sessions
Proceeding with single crack mode
Guesses: 50000g/s ...
```

## Related

- [[procedures/Crack-Password-Hashes-with-John-the-Ripper]]
- [[tools/John-the-Ripper]]
