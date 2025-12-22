---
id: cmd-uuid-1
data: echo vakzz >/tmp/vakzz
tags:
  - file-write
  - rce-poc
type: command
output: File /tmp/vakzz created with content 'vakzz'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.932Z'
verified: false
validated: true
submitted: true
---
# echo-vakzz-file-write

## Command

```bash
echo vakzz >/tmp/vakzz
```

## Description

This command writes the string 'vakzz' to a file in /tmp, demonstrating basic file write capability from an RCE payload injected via Perl qx{} in ExifTool.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| vakzz | Content to write | Yes |
| /tmp/vakzz | Target file path | Yes |

## Examples

### Basic Usage

```bash
echo vakzz >/tmp/vakzz
```

### Advanced Usage

```bash
echo 'test content' > /tmp/testfile
```

## Expected Output

No stdout; file created at /tmp/vakzz containing 'vakzz'. Verify with `cat /tmp/vakzz`.

## Related

- [[commands/id-display-user]]
- [[procedures/Verify-RCE-Impact-with-File-Write-or-Reverse-Shell]]
