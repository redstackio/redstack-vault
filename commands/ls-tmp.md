---
data: ls /tmp/
tags:
  - file-listing
type: command
executor: bash
platforms:
  - Linux
id: 4588a9b2-46ec-466b-bb65-7c8098fd8b93
created_at: '2025-12-11T03:47:47.796Z'
updated_at: '2025-12-11T03:47:47.796Z'
verified: false
validated: true
submitted: true
---
# ls .tmp

## Command

```bash
ls /tmp/
```

## Description

Lists files in the /tmp/ directory, used before and after exploit to verify file creation by RCE payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/tmp/` | Directory to list | Yes |

## Examples

### Basic Usage

```bash
ls /tmp/
```

## Expected Output

List of files, e.g., ks-script-esd4my7v ks-script-eusq_sc5.

## Related

- [[procedures/Execute-Headless-Chromium-Exploit]]
- [[commands/cat-exploit-file]]
