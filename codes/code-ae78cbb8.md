---
id: ae78cbb8-aa6b-42ca-98a6-608af7f4edc3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.904099+00:00'
updated_at: '2023-04-10T20:25:09.489470+00:00'
---

# Code Snippet ae78cbb8

**Language**: Powershell

```powershell
nmap -sn -n --disable-arp-ping 192.168.1.1-254 | grep -v "host down"
-sn : Disable port scanning. Host discovery only.
-n : Never do DNS resolution
```


