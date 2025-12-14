---
data: whoami
tags:
  - recon
  - rce
type: command
output: █████████ (redacted username)
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.166Z'
id: 8da59fe7-e2d8-4139-8ac4-cd4b45cd457f
verified: false
validated: true
submitted: true
---
# whoami-windows

## Command

```cmd
whoami
```

## Description

Displays the current user identity on a Windows system, useful for confirming privilege level after RCE via webshell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters | No |

## Examples

### Basic Usage

```cmd
whoami
```

### Advanced Usage

```cmd
whoami /user
```

## Expected Output

Current username in DOMAIN\username format, e.g., DOD\iis_apppool.

## Related

- [[Related Procedure: Execute-Commands-via-Uploaded-Webshell]]
