---
id: 5409414a-d84c-40b4-bc1d-ea68fb61edc3
name: 7z-extract-password-protected-zip
type: command
executor: bash
data: 7z x $_FILENAME.zip
output: >-
  root@kali:~# 7z backup.zip


  7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21

  p7zip Version 16.02 (locale=en_US.utf8,Utf16=on,HugeFiles=on,64 bits,3 CPUs
  Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (806EA),ASM,AES-NI)


  Scanning the drive for archives:

  1 file, 10320 bytes (11 KiB)


  Extracting archive: backup.zip

  --

  Path = backup.zip

  Type = zip

  Physical Size = 10320



  Enter password (will not be echoed):

  Everything is Ok


  Size:       294320

  Compressed: 10320
created_at: '2019-12-13T22:09:49.766527+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - extract
  - compression
verified: true
validated: true
---

# 7z-extract-password-protected-zip

## Command

```bash
7z x $_FILENAME.zip
```

## Description

This command uses 7-Zip to extract a password-protected ZIP archive that employs AES encryption. It is essential for scenarios where standard tools like 'unzip' fail due to lack of AES support. The extraction process prompts for the password securely and outputs the contents to the current directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILENAME | Path to the ZIP archive file (e.g., backup.zip) | Yes |

Note: The command interactively prompts for the password with 'Enter password (will not be echoed):'. For non-interactive use, append '-p$_PASSWORD' (e.g., 7z x $_FILENAME.zip -p$_PASSWORD), but this exposes the password in process lists.

## Examples

### Basic Usage

```bash
7z x encrypted.zip
```

Enter the password when prompted to extract files.

### Advanced Usage

```bash
7z x encrypted.zip -psecretpass -o/output/dir
```

Extracts to a specified output directory with password provided non-interactively.

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# 7z backup.zip

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.utf8,Utf16=on,HugeFiles=on,64 bits,3 CPUs Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 10320 bytes (11 KiB)

Extracting archive: backup.zip
--
Path = backup.zip
Type = zip
Physical Size = 10320


Enter password (will not be echoed):
Everything is Ok

Size:       294320
Compressed: 10320
```

Success is indicated by 'Everything is Ok' and extracted files appearing in the directory.

## Related

- [[tools/p7zip]]
