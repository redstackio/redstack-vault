---
data: ls
tags:
  - verification
  - rce
type: command
output: ... me ...
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.346Z'
id: ec14bf47-1020-45f6-a60d-b2d518e02182
verified: false
validated: true
submitted: true
---
# ls-after-rce

## Command

```bash
ls
```

## Description

Verifies RCE by checking for new file 'me'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Current dir | No |

## Examples

### Basic Usage

```bash
ls
```

## Expected Output

' me' file listed.

## Related

- [[commands/curl-trigger-rce]]
