---
type: command
executor: powershell
data: SharPersist -t schtaskbackdoor -n "Something Cool" -m remove
tags:
  - persistence
  - removal
platforms:
  - Windows
verified: true
validated: true
---

# sharpersist-remove-schtaskbackdoor-persistence

## Command

```powershell
SharPersist -t schtaskbackdoor -n "Something Cool" -m remove
```

## Description

Removes a previously added schtaskbackdoor persistence entry by name, cleaning up registry artifacts in Cobalt Strike.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t schtaskbackdoor` | Type: Hidden scheduled task backdoor | Yes |
| `-n <name>` | Name of the entry to remove | Yes |
| `-m remove` | Mode to remove the entry | Yes |

## Examples

### Basic Usage

```powershell
SharPersist -t schtaskbackdoor -n "UpdateCheck" -m remove
```

### Advanced Usage

```powershell
SharPersist -t schtaskbackdoor -n "Something Cool" -m remove; SharPersist -t schtaskbackdoor -m list
```

## Expected Output

```
Persistence removed: Something Cool
```

## Related

- [[procedures/Establish-Persistence-Using-SharPersist-in-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
