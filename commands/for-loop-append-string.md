---
data: for i in `seq 8179`; do echo -n "a"; done >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
tags:
  - payload
type: command
executor: bash
platforms:
  - Linux
id: 9ac296d2-5ed3-4848-b6a2-ed43b3aee97b
created_at: '2025-12-13T09:01:22.339Z'
updated_at: '2025-12-13T09:01:22.339Z'
verified: false
validated: true
submitted: true
---
# For Loop Append String

## Command

```bash
for i in `seq 8179`; do echo -n "a"; done >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
```

## Description

Appends 8179 'a' characters to the file using a loop.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `seq 8179` | Generates numbers from 1 to 8179 | Yes |

## Examples

### Basic Usage

```bash
for i in `seq 8179`; do echo -n "a"; done >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
```

## Expected Output

File appended with 8179 'a' characters.

## Related

- [[procedures/Craft-Oversized-Trailer-Payload]]
