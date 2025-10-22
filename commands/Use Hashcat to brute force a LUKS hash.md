---
id: 9142082d-2c5b-4df4-8d90-65d5dcb11f18
name: Use Hashcat to brute force a LUKS hash
type: command
executor: null
data: hashcat -m 14600 luks.hash rockyou.txt
output: null
created_at: '2019-09-11T22:47:55.950018+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Use Hashcat to brute force a LUKS hash

```bash
hashcat -m 14600 luks.hash rockyou.txt
```
