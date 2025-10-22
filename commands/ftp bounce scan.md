---
id: f3cab64c-f5bf-4c32-a278-63e0220644af
name: ftp bounce scan
type: command
executor: bash
data: 'nmap -P0 -n -b username:password@target-ip target2-ip --proxies socks4://proxy-ip:1080
  -vvvv

  '
output: null
created_at: '2020-07-14T18:14:50.436870+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# ftp bounce scan

```bash
nmap -P0 -n -b username:password@target-ip target2-ip --proxies socks4://proxy-ip:1080 -vvvv

```
