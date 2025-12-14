---
id: echo-eicar
data: >-
  echo|set
  /p="X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*" >
  %userprofile%\Desktop\eicar\eicar.bat
tags:
  - av-trigger
  - file-write
type: command
output: File eicar.bat created with EICAR content
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.726Z'
verified: false
validated: true
submitted: true
---
# echo-write-eicar-string

## Command

```cmd
echo|set /p="X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*" > %userprofile%\Desktop\eicar\eicar.bat
```

## Description

Writes the standard EICAR antivirus test string to a batch file, triggering detection by Acronis True Image AV.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo|set /p= | Outputs string without newline | Yes |
| "X5O!...$H+H*" | EICAR test string | Yes |
| > | Redirect to file | Yes |
| %userprofile%\Desktop\eicar\eicar.bat | Target file path | Yes |

## Examples

### Basic Usage

```cmd
echo|set /p="X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*" > test.bat
```

### Advanced Usage

Use in scripts for automated AV testing.

## Expected Output

File created; AV alert may appear immediately.

## Related

- [[commands/echo-modify-to-calc]]
