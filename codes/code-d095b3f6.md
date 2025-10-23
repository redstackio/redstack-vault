---
id: d095b3f6-ca32-495f-9748-a64a46ef808b
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:16.301432+00:00'
updated_at: '2023-04-10T20:36:21.480931+00:00'
---

# Code Snippet d095b3f6

**Language**: Powershell

```powershell
systemctl disable systemd-resolved
systemctl stop systemd-resolved
rm /etc/resolv.conf
echo "nameserver 8.8.8.8" >  /etc/resolv.conf
echo "nameserver 8.8.4.4" >>  /etc/resolv.conf
```


