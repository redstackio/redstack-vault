---
id: c26a68ff-1902-416c-805b-3bd0239ac833
name: Nmap Service Scan with Initial RTT Timeout Template
type: command
executor: bash
data: nmap -p- --initial-rtt-timeout 50ms $_TARGET_IP
output: null
created_at: '2019-11-13T01:16:38.415796+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Service Scan with Initial RTT Timeout Template

```bash
nmap -p- --initial-rtt-timeout 50ms $_TARGET_IP
```


