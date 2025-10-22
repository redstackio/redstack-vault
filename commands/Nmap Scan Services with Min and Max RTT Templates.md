---
id: 91b4e18e-51e2-4f8c-b715-91c433317c05
name: Nmap Scan Services with Min and Max RTT Templates
type: command
executor: bash
data: nmap -p- --min-rtt-timeout 5ms --max-rtt-timeout 100ms $_TARGET_IP
output: null
created_at: '2019-11-13T01:16:38.401502+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Scan Services with Min and Max RTT Templates

```bash
nmap -p- --min-rtt-timeout 5ms --max-rtt-timeout 100ms $_TARGET_IP
```
