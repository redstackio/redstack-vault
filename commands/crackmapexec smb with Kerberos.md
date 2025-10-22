---
id: fa9e2f53-5837-425d-b627-8fab6436b183
name: crackmapexec smb with Kerberos
type: command
executor: bash
data: export KRB5CCNAME=/tmp/kerberos/admin.ccache; crackmapexec smb 192.168.1.100
  -u admin --use-kcache
output: null
created_at: '2023-04-06T03:56:30.722082+00:00'
updated_at: '2023-04-10T20:38:03.882727+00:00'
---

# crackmapexec smb with Kerberos

```bash
export KRB5CCNAME=/tmp/kerberos/admin.ccache; crackmapexec smb 192.168.1.100 -u admin --use-kcache
```
