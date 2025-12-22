---
id: a11d8b59-39da-432c-8385-484c19bb8c17
name: access-remote-directory-with-dir
type: command
executor: cmd
data: dir \\dc.domain.com\c$
output: null
created_at: '2023-04-06T03:56:07.695482+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - smb
  - access
verified: true
validated: true
---

# access-remote-directory-with-dir

## Command

```cmd
dir \\dc.domain.com\c$
```

## Description

Accesses a remote admin share (C$) via SMB using an injected Kerberos ticket for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| \\target\share | UNC path to remote share (e.g., \\dc.domain.com\c$) | Yes |

## Examples

### Basic Usage

```cmd
dir \\10.10.10.10\ADMIN$
```

## Expected Output

Directory listing of files/folders in the share, confirming access.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
