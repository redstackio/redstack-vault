---
id: dc7a7074-a036-4c7b-b8b8-e282ffae95ce
name: wget-crawl-web-app-recursively
type: command
executor: bash
data: >-
  wget --recursive --html-extension --convert-links
  --restrict-file-names=windows --no-parent http://$_TARGET_IP
output: |-
  root@kali:~# wget --recursive ... http://10.10.10.10/
  --2019-10-09 14:23:57--  http://10.10.10.10/  
  ... Downloaded: 85 files, 2.2M ...
created_at: '2019-10-09T18:38:08.462994+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - crawl
  - download
verified: true
validated: true
---

# wget-crawl-web-app-recursively

## Command

```bash
wget --recursive --html-extension --convert-links --restrict-file-names=windows --no-parent http://$_TARGET_IP
```

## Description

Recursively downloads a web site to local mirror for offline analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --recursive | Follow links | Yes |
| --html-extension | Add .html to files | Yes |
| --convert-links | Make local | Yes |
| --restrict-file-names=windows | Sanitize names | Yes |
| --no-parent | Don't ascend | Yes |
| http://$_TARGET_IP | Starting URL | Yes |

## Examples

### Mirror Site

```bash
wget --recursive --no-parent http://10.10.10.10/
```

## Expected Output

Progress of downloaded files and total stats.

## Related

- [[procedures/enumerate-web-cms-for-usernames-and-passwords]]
