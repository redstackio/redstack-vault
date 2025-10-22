---
id: 25bcace8-e188-448b-acda-5a2503bcaad6
name: Crack NTP hashes with hashcat
type: command
executor: bash
data: hashcat -m 31300 ntp-hashes.txt
output: null
created_at: '2023-04-06T03:56:05.039565+00:00'
updated_at: '2023-04-10T20:36:14.046391+00:00'
---

# Crack NTP hashes with hashcat

```bash
hashcat -m 31300 ntp-hashes.txt
```
