---
id: cmd-mkdir-c-usr-local-ssl-001
data: 'mkdir c:\usr\local\ssl'
tags:
  - directory-creation
type: command
output: Directory created successfully.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.183Z'
verified: false
validated: true
submitted: true
---
# mkdir-create-c-usr-local-ssl

## Command

```cmd
mkdir c:\usr\local\ssl
```

## Description

Creates the ssl subdirectory to host the malicious openssl.cnf for curl's OPENSSLDIR exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `c:\usr\local\ssl` | Target path | Yes |

## Examples

### Basic Usage

```cmd
mkdir c:\usr\local\ssl
```

## Expected Output

Directory created successfully.

## Related

- [[commands/mkdir-create-c-usr-local]]
