---
id: ad82ad79-adb8-4923-a48e-fae704b8baf3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:38.436756+00:00'
updated_at: '2023-04-10T20:24:07.408918+00:00'
---

# Code Snippet ad82ad79

**Language**: Powershell

```powershell
curl http://169.254.169.254/metadata/v1/id
http://169.254.169.254/metadata/v1.json
http://169.254.169.254/metadata/v1/ 
http://169.254.169.254/metadata/v1/id
http://169.254.169.254/metadata/v1/user-data
http://169.254.169.254/metadata/v1/hostname
http://169.254.169.254/metadata/v1/region
http://169.254.169.254/metadata/v1/interfaces/public/0/ipv6/address

All in one request:
curl http://169.254.169.254/metadata/v1.json | jq
```
