---
data: 'steam://openexternalforpid/10400/jarfile:something'
tags:
  - steam
  - rce
type: command
executor: bash
platforms:
  - Windows
id: 06cf2ef1-a666-4c93-8528-851226731382
created_at: '2025-12-11T06:10:17.641Z'
updated_at: '2025-12-11T06:10:17.641Z'
verified: false
validated: true
submitted: true
---
# steam-openexternalforpid-jarfile

## Command

```bash
steam://openexternalforpid/10400/jarfile:something
```

## Description

Opens an external process using jarfile protocol for a given PID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `10400` | PID | Yes |
| `jarfile:something` | Protocol URI | Yes |

## Examples

### Basic Usage

```bash
steam://openexternalforpid/10400/jarfile:something
```

## Expected Output

Attempts to execute the protocol.

## Related

- [[commands/steam-openexternalforpid-file]]
- [[procedures/Reverse-Engineer-Steam-Binary-for-Undocumented-URIs]]
