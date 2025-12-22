---
id: 23ee6634-7da7-4795-9886-62025207e609
name: python3-launch-simple-http-server
type: command
executor: bash
data: python3 -m http.server $_PORT
output: |-
  root@kali:~# python3 -m http.server 8000
  Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
created_at: '2019-10-29T22:25:12.708225+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - http-server
  - file-host
verified: true
validated: true
---

# python3-launch-simple-http-server

## Command

```bash
python3 -m http.server $_PORT
```

## Description

Starts a simple HTTP server to host files for target download.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m http.server | Module run | Yes |
| $_PORT | Listening port (default 8000) | No |

## Examples

### On Port 80

```bash
python3 -m http.server 80
```

## Expected Output

'Serving HTTP on 0.0.0.0 port $_PORT'.

## Related

- [[procedures/upgrade-website-rce-to-reverse-shell-on-linux]]
