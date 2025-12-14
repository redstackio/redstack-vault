---
id: cmd-mkdir-c-stage-001
data: 'mkdir c:\stage'
tags:
  - directory-creation
type: command
output: Directory created successfully.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.177Z'
verified: false
validated: true
submitted: true
---
# mkdir-create-c-stage

## Command

```cmd
mkdir c:\stage
```

## Description

Creates a staging directory for the malicious DLL referenced in openssl.cnf during curl vuln exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `c:\stage` | Target path | Yes |

## Examples

### Basic Usage

```cmd
mkdir c:\stage
```

## Expected Output

Directory created successfully.

## Related

- [[commands/copy-calc-dll-to-stage]]
