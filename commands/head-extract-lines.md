---
data: head -11 base.txt > attack5.txt
tags:
  - payload
type: command
executor: bash
platforms:
  - Linux
id: a03ef33b-1a9e-4afc-ae8f-f0655f2bf7d7
created_at: '2025-12-13T09:01:22.332Z'
updated_at: '2025-12-13T09:01:22.332Z'
verified: false
validated: true
submitted: true
---
# Head Extract Lines

## Command

```bash
head -11 base.txt > attack5.txt
```

## Description

Copies the first 11 lines of base.txt to attack5.txt.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-11` | Output the first 11 lines | Yes |

## Examples

### Basic Usage

```bash
head -11 base.txt > attack5.txt
```

## Expected Output

attack5.txt created with first 11 lines of base.txt.

## Related

- [[procedures/Craft-Oversized-Trailer-Payload]]
