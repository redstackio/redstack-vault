---
id: 29fcbb63-0159-41e1-b9af-e4ece46ce53c
name: access-smb-share-c-drive
type: command
executor: bash
data: ls \\PC1.purple.lab\c$
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - smb
  - lateral-movement
verified: true
validated: true
---

# access-smb-share-c-drive

## Command

```bash
ls \\PC1.purple.lab\c$
```

## Description

Lists contents of the remote C$ admin share using impersonated credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| \\PC1.purple.lab\c$ | SMB share path | Yes |

## Examples

### Basic Usage

```bash
ls \\target.domain.com\c$
```

## Expected Output

Directory listing: files and folders in C$.

## Related

- [[procedures/WebDAV-Relay-Attack]]
