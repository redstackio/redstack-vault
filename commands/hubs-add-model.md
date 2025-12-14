---
id: cmd-hubs-add-model-001
data: >
  |

  /add
  https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb
tags:
  - object-spawn
  - bypass
type: command
output: Duck object appears in the room; can be deleted by users via menu
executor: hubs-chat
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.919Z'
verified: false
validated: true
submitted: true
---
# hubs-add-model

## Command

```bash
/add https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb
```

## Description

This Hubs chat command spawns a 3D GLB model (duck) in the room, bypassing disabled creation permissions due to absent server validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Path to GLB model file | Yes |

## Examples

### Basic Usage

```bash
/add https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb
```

### Advanced Usage

N/A; simple URL parameter.

## Expected Output

Duck object appears in the room; can be deleted by users via menu.

## Related

- [[commands/hubs-add-unremovable-model]]
- [[procedures/Spawn-Objects-via-Chat-Bypass]]
