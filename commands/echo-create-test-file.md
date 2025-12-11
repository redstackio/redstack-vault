---
data: echo hello > /tmp/ggg
tags:
  - file-creation
type: command
executor: bash
platforms:
  - Linux
id: cc2822af-9570-46c2-a7e3-1ee3b4c88379
created_at: '2025-12-11T03:47:39.418Z'
updated_at: '2025-12-11T03:47:39.418Z'
verified: false
validated: true
submitted: true
---
# echo-create-test-file

## Command

```bash
echo hello > /tmp/ggg
```

## Description

Creates a test file with specified content in /tmp for exploitation testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `hello` | Content to write | Yes |
| `> /tmp/ggg` | Output redirection to file | Yes |

## Examples

### Basic Usage

```bash
echo hello > /tmp/ggg
```

## Expected Output

No output; creates file /tmp/ggg with 'hello'.

## Related
- [[procedures/Bypass-Package-Upload-Validation-for-File-Read]]
- [[procedures/Exploit-Wiki-Attachments-for-Arbitrary-File-Access]]
