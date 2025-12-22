---
id: echo-calc
data: echo calc > %userprofile%\Desktop\eicar\eicar.bat
tags:
  - payload-modify
  - file-overwrite
type: command
output: File contents replaced with 'calc'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.721Z'
verified: false
validated: true
submitted: true
---
# echo-modify-to-calc

## Command

```cmd
echo calc > %userprofile%\Desktop\eicar\eicar.bat
```

## Description

Overwrites the contents of the batch file with a simple command to launch Calculator, serving as a proof-of-concept payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo calc | Outputs 'calc' string | Yes |
| > | Overwrite redirect | Yes |
| %userprofile%\Desktop\eicar\eicar.bat | Target file | Yes |

## Examples

### Basic Usage

```cmd
echo calc > test.bat
```

### Advanced Usage

```cmd
echo malicious_command > payload.bat
```

## Expected Output

File overwritten; contents now 'calc'.

## Related

- [[commands/echo-write-eicar-string]]
