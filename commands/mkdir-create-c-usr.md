---
id: cmd-mkdir-c-usr-001
data: 'mkdir c:\usr'
tags:
  - directory-creation
type: command
output: The system output or stderr if the directory already exists.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.217Z'
verified: false
validated: true
submitted: true
---
# mkdir-create-c-usr

## Command

```cmd
mkdir c:\usr
```

## Description

Creates the root directory c:\usr as part of the OPENSSLDIR path exploitation in curl on Windows, allowing low-priv users to build the insecure config location.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `c:\usr` | Target path for the usr directory | Yes |

## Examples

### Basic Usage

```cmd
mkdir c:\usr
```

### Advanced Usage

N/A for this simple mkdir.

## Expected Output

Directory created successfully, or error if permissions denied.

## Related

- [[commands/mkdir-create-c-usr-local]]
