---
id: 6815e39d-f161-42e0-b7fc-2d16d9d1a564
name: Get domain user info
type: command
executor: bash
data: 'Get-NetUser [-UserName john] Get-NetUser -Domain | Select-Object objectsid,lockouttime,samaccounttype,accountexpires,objectclass,useraccountcontrol,@{Name=''memberof'';Expression={[string]::join(";",($_.memberof))}},info,distinguishedname,adspath,cn,pwdlastset,objectguid,whencreated,description,samaccountname,usnchanged,name|
  export-csv userprops_members.csv

  '
output: null
created_at: '2020-07-14T18:21:07.165474+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get domain user info

```bash
Get-NetUser [-UserName john] Get-NetUser -Domain | Select-Object objectsid,lockouttime,samaccounttype,accountexpires,objectclass,useraccountcontrol,@{Name='memberof';Expression={[string]::join(";",($_.memberof))}},info,distinguishedname,adspath,cn,pwdlastset,objectguid,whencreated,description,samaccountname,usnchanged,name| export-csv userprops_members.csv

```


