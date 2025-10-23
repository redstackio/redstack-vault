---
id: ad0d4649-bfe1-4d29-8f76-333634e86eb5
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:30.721828+00:00'
updated_at: '2023-04-10T20:38:03.895929+00:00'
---

# Code Snippet ad0d4649

**Language**: Powershell

```powershell
crackmapexec smb 192.168.1.100 -u Administrator -p "Password123?" # Password
crackmapexec smb 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0" # NT Hash
export KRB5CCNAME=/tmp/kerberos/admin.ccache; crackmapexec smb 192.168.1.100 -u admin --use-kcache # Kerberos
```


