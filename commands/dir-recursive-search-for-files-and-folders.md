---
id: 1905bafa-2be4-4c39-a837-1e5809b1f180
type: command
executor: command_prompt
data: dir /s "$_FILENAME"
output: |-
  C:\Users>dir /s "secrets.txt"
   Volume in drive C has no label.
   Volume Serial Number is 8A74-7377

   Directory of C:\Users\Bob\Desktop

  11/26/2019  08:19 AM             1,328 secrets.txt
                 1 File(s)         1,328 bytes

       Total Files Listed:
                 1 File(s)              8 bytes
                 0 Dir(s)  34,972,065,792 bytes free
created_at: '2019-11-26T16:37:00.743722+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - file-search
  - discovery
verified: true
validated: true
---

# dir-recursive-search-for-files-and-folders

## Command

```command_prompt
dir /s "$_FILENAME"
```

## Description

This command performs a recursive search for a specified file or pattern across the entire directory tree starting from the current directory. It is useful for discovering sensitive files like configuration files, credentials, or logs during reconnaissance or post-exploitation activities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILENAME | The name or pattern of the file to search for (e.g., "secrets.txt" or "*.conf") | Yes |
| /s | Enables recursive search through all subdirectories | Yes |

## Examples

### Basic Usage

Search for a file named "secrets.txt" recursively:

```command_prompt
dir /s "secrets.txt"
```

### Advanced Usage

Search for all configuration files:

```command_prompt
dir /s "*.conf"
```

## Expected Output

```
C:\Users>dir /s "secrets.txt"
 Volume in drive C has no label.
 Volume Serial Number is 8A74-7377

 Directory of C:\Users\Bob\Desktop

11/26/2019  08:19 AM             1,328 secrets.txt
               1 File(s)         1,328 bytes

     Total Files Listed:
               1 File(s)              8 bytes
               0 Dir(s)  34,972,065,792 bytes free
```

The output includes the volume information, directory paths where matches are found, file details (size, date modified), and a summary of total files and directories.

## Related

- [[tools/dir]]
- [[procedures/Enumerate-Filesystem-for-Sensitive-Data]]
