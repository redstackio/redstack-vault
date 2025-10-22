---
id: f5dd1b88-6516-4c95-ba96-ccc3ed7de4f2
name: Crack Password Hashes with Hashcat
type: command
executor: bash
data: hashcat -m 5600 -a 0 hash.txt crackstation.txt
output: null
created_at: '2023-04-06T03:56:05.301063+00:00'
updated_at: '2023-04-10T20:25:44.766232+00:00'
---

# Crack Password Hashes with Hashcat

```bash
hashcat -m 5600 -a 0 hash.txt crackstation.txt
```
