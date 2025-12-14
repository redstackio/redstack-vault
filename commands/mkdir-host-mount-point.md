---
data: mkdir /h
tags:
  - mount
type: command
executor: bash
platforms:
  - Linux
id: b4742338-2174-4aa3-ad41-f4d8388d26f4
created_at: '2025-12-14T04:08:48.075Z'
updated_at: '2025-12-14T04:08:48.075Z'
verified: false
validated: true
submitted: true
---
# Mkdir Host Mount Point

## Command

```bash
mkdir /h
```

## Description

Creates a directory for mounting host volumes in container.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /h | Mount point path | Yes |

## Examples

### Basic Usage

```bash
mkdir /h
```

## Expected Output

Directory created successfully.

## Related

- [[commands/mount-host-storage-volume]]
