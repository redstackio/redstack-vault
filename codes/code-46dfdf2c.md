---
id: 46dfdf2c-5fbc-42f1-9fac-6c10e4d33645
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:06.368796+00:00'
updated_at: '2023-04-10T20:26:29.958128+00:00'
---

# Code Snippet 46dfdf2c

**Language**: Powershell

```powershell
crackmapexec ldap 10.10.10.10 -u username -p password --admin-count
# or
python ldapdomaindump.py -u example.com\john -p pass123 -d ';' 10.10.10.10
jq -r '.[].attributes | select(.adminCount == [1]) | .sAMAccountName[]' domain_users.json
# or
Get-ADUser -LDAPFilter "(objectcategory=person)(samaccountname=*)(admincount=1)"
Get-ADGroup -LDAPFilter "(objectcategory=group) (admincount=1)"
# or
([adsisearcher]"(AdminCount=1)").findall()
```
