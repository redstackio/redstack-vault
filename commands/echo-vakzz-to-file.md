---
data: echo vakzz >/tmp/vakzz
tags:
  - file-write
  - rce-demo
type: command
executor: bash
platforms:
  - Linux
id: 3572f023-2839-47ee-8ef8-c25db85d4b4c
created_at: '2025-12-11T03:47:58.202Z'
updated_at: '2025-12-11T03:47:58.202Z'
verified: false
validated: true
submitted: true
---
# echo-vakzz-to-file

## Command

```bash
echo vakzz >/tmp/vakzz
```

## Description

Writes the string 'vakzz' to the file /tmp/vakzz to demonstrate arbitrary command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `vakzz` | String to write | Yes |
| `>/tmp/vakzz` | Redirect to file | Yes |

## Examples

### Basic Usage

```bash
echo vakzz >/tmp/vakzz
```

## Expected Output

Creates /tmp/vakzz file on the server.

## Related

- [[procedures/Upload-Image-to-Trigger-ExifTool-RCE]]
