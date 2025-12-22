---
id: cmd-hubs-add-youtube-001
data: |
  |
  /add --no-menu https://www.youtube.com/watch?v=dQw4w9WgXcQ
tags:
  - media-embed
  - disruption
  - bypass
type: command
output: >-
  Video plays continuously in the room; cannot be stopped, removed, or limited;
  can be spawned multiple times
executor: hubs-chat
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.913Z'
verified: false
validated: true
submitted: true
---
# hubs-add-youtube-video

## Command

```bash
/add --no-menu https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Description

Embeds an unremovable YouTube video in Hubs room via chat, bypassing restrictions; video plays on loop for disruption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --no-menu | Flag to prevent interaction menu (makes video undeletable) | Yes |
| URL | YouTube video URL | Yes |

## Examples

### Basic Usage

```bash
/add --no-menu https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Advanced Usage

Repeat for multiple instances.

## Expected Output

Video plays continuously in the room; cannot be stopped, removed, or limited; can be spawned multiple times.

## Related

- [[commands/hubs-add-unremovable-model]]
- [[procedures/Spawn-Objects-via-Chat-Bypass]]
