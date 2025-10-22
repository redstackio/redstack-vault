---
id: 84aebd24-b6bc-4ef6-ac13-34bfcd34e17d
name: Use `proxychains + command" to use the socks proxy
type: command
executor: bash
data: 'proxychains nmap -sTV -n -PN -p 80,22 target-ip -vv

  '
output: null
created_at: '2020-07-14T18:14:35.531603+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Use `proxychains + command" to use the socks proxy

```bash
proxychains nmap -sTV -n -PN -p 80,22 target-ip -vv

```
