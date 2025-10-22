---
id: 47c83268-2133-4772-9fea-a7ffcbe26906
name: proxychains
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:35.926862+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# proxychains

# a dynamic ssh tunnel is needed

search ssh

**Command** ([[Use `proxychains + command" to use the socks proxy]]):

```bash
proxychains nmap -sTV -n -PN -p 80,22 target-ip -vv

```

Double pivot works the same, but you create the 2nd ssh tunnel via proxychains and a different dynamic port.

After the tunnel is up, you can comment out the first socks entry in proxychains config.
