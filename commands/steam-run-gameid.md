---
data: 'steam://run/[GAMEID]'
tags:
  - steam
  - execution
type: command
executor: bash
platforms:
  - Windows
id: 53ceb942-3d4b-4e99-8b38-c15ff483b7e1
created_at: '2025-12-14T00:11:25.276Z'
updated_at: '2025-12-14T00:11:25.276Z'
verified: false
validated: true
submitted: true
---
# steam-run-gameid

## Command

```bash
steam://run/[GAMEID]
```

## Description

Runs an installed game without confirmation, exploited via XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gameid` | ID of the game | Yes |

## Examples

### Basic Usage

```bash
steam://run/12345
```

## Expected Output

Launches the specified game.

## Related

- [[procedures/Achieving-RCE-via-Openexternalforpid]]
