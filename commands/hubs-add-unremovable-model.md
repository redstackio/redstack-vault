---
id: cmd-hubs-add-unremovable-001
data: >
  |

  /add --no-menu
  https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb
tags:
  - persistent-spawn
  - bypass
type: command
output: Duck object appears and cannot be removed by any user
executor: hubs-chat
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.915Z'
verified: false
validated: true
submitted: true
---
# hubs-add-unremovable-model

## Command

```bash
/add --no-menu https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb
```

## Description

Spawns an unremovable 3D GLB model in Hubs room via chat, using --no-menu flag to disable interaction, bypassing admin restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --no-menu | Flag to prevent interaction menu (makes object undeletable) | Yes |
| URL | Path to GLB model file | Yes |

## Examples

### Basic Usage

```bash
/add --no-menu https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb
```

### Advanced Usage

N/A.

## Expected Output

Duck object appears and cannot be removed by any user.

## Related

- [[commands/hubs-add-model]]
- [[procedures/Spawn-Objects-via-Chat-Bypass]]
