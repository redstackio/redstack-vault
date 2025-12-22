---
id: 23ee6634-7da7-4795-9886-62025207e609
type: command
executor: bash
data: python3 -m http.server $_PORT
output: |-
  root@kali:~# python3 -m http.server 80
  Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
created_at: '2019-10-29T22:25:12.708225+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - web
  - hosting
verified: true
validated: true
---

# python3-launch-http-server

## Command

```bash
python3 -m http.server $_PORT
```

## Description

Starts a simple HTTP server in the current directory using Python 3, ideal for quickly hosting files for download in attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m http.server | Run HTTP server module | Yes |
| $_PORT | Listening port (default 8000) | No |

## Examples

### Basic Usage

```bash
python3 -m http.server 80
```

### Bind to Interface

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

## Expected Output

Serving HTTP on 0.0.0.0 port 80, with logs of requests.

## Related

- [[procedures/Upgrade-Web-RCE-to-Reverse-Shell-on-Linux]]
- [[tools/Python]]
