---
type: command
executor: powershell
data: SharPersist -t service -n "Some Service" -m remove
tags:
  - persistence
  - removal
platforms:
  - Windows
verified: true
validated: true
---

# sharpersist-remove-service-persistence

## Command

```powershell
SharPersist -t service -n "Some Service" -m remove
```

## Description

Deletes a SharPersist-created Windows service, stopping it first to remove persistence cleanly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t service` | Type: Windows service | Yes |
| `-n <name>` | Service name to remove | Yes |
| `-m remove` | Mode to remove the service | Yes |

## Examples

### Basic Usage

```powershell
SharPersist -t service -n "DiagTrack" -m remove
```

### Advanced Usage

```powershell
SharPersist -t service -n "Some Service" -m remove; sc delete "Some Service"
```

## Expected Output

```
Service stopped and removed: Some Service
```

## Related

- [[procedures/Establish-Persistence-Using-SharPersist-in-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
