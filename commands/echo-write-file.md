---
data: echo vakzz >/tmp/vakzz
tags:
  - file-creation
type: command
executor: bash
platforms:
  - Linux
id: e477c520-6906-4b98-bc0f-3e5ee2171d21
created_at: '2025-12-11T06:10:22.440Z'
updated_at: '2025-12-11T06:10:22.440Z'
verified: false
validated: true
submitted: true
---
# echo-write-file

## Command

```bash
echo vakzz >/tmp/vakzz
```

## Description

Writes the string 'vakzz' to the file /tmp/vakzz, used to prove code execution in the GitLab RCE PoC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `>/tmp/vakzz` | Redirects output to file | Yes |

## Examples

### Basic Usage

```bash
echo vakzz >/tmp/vakzz
```

## Expected Output

File /tmp/vakzz created with content 'vakzz'.

## Related

- [[commands/perl-qx-execute-shell]]
- [[procedures/Create-GitLab-Snippet-and-Upload-Malicious-File]]
