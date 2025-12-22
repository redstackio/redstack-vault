---
data: 'mkdir C:\usr\local\ssl'
tags:
  - directory-creation
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.489Z'
id: 4dabd8b5-cd92-44ac-8a8c-813121306d90
verified: false
validated: true
submitted: true
---
# create-directory-path

## Command

```cmd
mkdir C:\usr\local\ssl
```

## Description

Creates a directory path on Windows, used here to establish insecure OpenSSL directories exploitable by low-priv users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| mkdir | Make directory | Yes |
| Path | Target path like C:\usr\local\ssl | Yes |

## Examples

### Basic Usage

```cmd
mkdir C:\usr\local\ssl
```

### Advanced Usage

```cmd
mkdir C:\usr\local /p
```

## Expected Output

The system cannot find the path specified. (if exists) or silent success.

## Related

- [[Related Procedure]]
