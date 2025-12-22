---
type: command
executor: cmd
data: dir $_EXFIL_PATH
output: null
platforms:
  - Windows
tags:
  - verification
  - file-list
verified: true
validated: true
---

# dir-list-exfil-directory

## Command

```cmd
dir $_EXFIL_PATH
```

## Description

Lists the contents of the specified exfiltration directory to verify file extraction success, such as confirming the presence of ntds.dit after a shadow copy operation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_EXFIL_PATH | Path to the exfiltration directory (e.g., C:\exfil) | Yes |

## Examples

### Basic Usage

```cmd
dir C:\exfil
```

### Advanced Usage

With silent output redirection:

```cmd
dir C:\exfil > exfil_contents.txt
```

## Expected Output

 Volume in drive C is Windows
 Directory of C:\exfil

04/10/2023  20:26    <DIR>          .
04/10/2023  20:26    <DIR>          ..
04/10/2023  20:26         2,048,000 ntds.dit
               1 File(s)      2,048,000 bytes

Success: ntds.dit listed with non-zero size.

## Related

- [[procedures/Dump-AD-Domain-Credentials-with-DiskShadow]]
