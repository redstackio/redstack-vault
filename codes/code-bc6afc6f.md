---
id: bc6afc6f-63b5-407f-98e3-27fe8f3bd343
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:22.694771+00:00'
updated_at: '2023-04-10T20:25:19.586644+00:00'
---

# Code Snippet bc6afc6f

**Language**: Powershell

```powershell
pacman -Sy sshuttle
apt-get install sshuttle
sshuttle -vvr user@10.10.10.10 10.1.1.0/24
sshuttle -vvr username@pivot_host 10.2.2.0/24 

# using a private key
$ sshuttle -vvr root@10.10.10.10 10.1.1.0/24 -e "ssh -i ~/.ssh/id_rsa" 

# -x == exclude some network to not transmit over the tunnel
# -x x.x.x.x.x/24
```
