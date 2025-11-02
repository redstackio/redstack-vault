---
id: 4cecc3ce-6a75-4a3d-8e6f-546aedee989e
name: vaultcmd.exe List Stored Windows Credentials
type: command
executor: command_prompt
data: vaultcmd.exe /listcreds:"Windows Credentials"
output: 'C:\>vaultcmd.exe /listcreds:"Windows Credentials"

  Credentials in vault: Windows Credentials


  Credential schema: Windows Domain Password Credential

  Resource: Domain:target=dc.domain.example

  Identity: Administrator

  Hidden: No

  Roaming: No

  Property (schema element id,value): (100,3)'
created_at: '2019-12-11T23:10:14.010968+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[vaultcmd]]'
---

# vaultcmd.exe List Stored Windows Credentials

```command_prompt
vaultcmd.exe /listcreds:"Windows Credentials"
```

## Expected Output

```
C:\>vaultcmd.exe /listcreds:"Windows Credentials"
Credentials in vault: Windows Credentials

Credential schema: Windows Domain Password Credential
Resource: Domain:target=dc.domain.example
Identity: Administrator
Hidden: No
Roaming: No
Property (schema element id,value): (100,3)
```


