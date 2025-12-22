---
id: 3e17ab5e-7693-41d6-bc5c-65631261059f
name: cmd-list-directory-with-ads
type: command
executor: command_prompt
data: dir /R $_TARGET_PATH
output: |-
  C:\temp>dir /R
   Volume in drive C has no label.
   Volume Serial Number is E03E-1CF0

   Directory of C:\temp

  11/22/2019  09:44 AM    <DIR>          .
  11/22/2019  09:44 AM    <DIR>          ..
  11/22/2019  09:44 AM             1,032 id_rsa
  11/22/2019  09:45 AM                24 normal.txt
                                   1,032 normal.txt:secret:$DATA
                 2 File(s)          1,056 bytes
                 2 Dir(s)  26,816,774,144 bytes free
created_at: '2019-11-22T18:04:45.283994+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - file-system
  - ads
  - enumeration
verified: true
validated: true
---

# cmd-list-directory-with-ads

## Command

```command_prompt
dir /R $_TARGET_PATH
```

## Description

This command lists the contents of a directory or file path, including any Alternate Data Streams (ADS) attached to files on NTFS volumes. It is used to discover hidden streams that are not visible in standard file listings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_TARGET_PATH` | The directory or file path to list (e.g., `C:\temp` or `C:\temp\file.txt`) | Yes |
| `/R` | Switch to display ADS streams recursively | Yes (built-in) |

## Examples

### Basic Usage

```command_prompt
dir /R C:\temp
```

### Advanced Usage

```command_prompt
dir /R C:\Users\Public
```

## Expected Output

```
C:\temp>dir /R
 Volume in drive C has no label.
 Volume Serial Number is E03E-1CF0

 Directory of C:\temp

11/22/2019  09:44 AM    <DIR>          .
11/22/2019  09:44 AM    <DIR>          ..
11/22/2019  09:44 AM             1,032 id_rsa
11/22/2019  09:45 AM                24 normal.txt
                                 1,032 normal.txt:secret:$DATA
               2 File(s)          1,056 bytes
               2 Dir(s)  26,816,774,144 bytes free
```

Look for lines like `filename:streamname:$DATA` to identify ADS.

## Related

- [[procedures/Extract-Alternate-Data-Stream-from-File]]
