---
id: 1b7ae28c-99d2-40d0-9f3a-ef0527569912
name: Display AzureAD status
type: command
executor: ''
data: dsregcmd.exe /status
output: "C:\\ dsregcmd.exe /status\n\n+----------------------------------------------------------------------+\n\
  | SSO State                                                            |\n+----------------------------------------------------------------------+\n\
  \n                AzureAdPrt : YES\n       AzureAdPrtAuthority : https://login.microsoftonline.com/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\n\
  \             EnterprisePrt : NO\n    EnterprisePrtAuthority : NO\n\n+----------------------------------------------------------------------+\n\
  | Device State                                                         |\n+----------------------------------------------------------------------+\n\
  \n             AzureAdJoined : YES\n          EnterpriseJoined : NO\n          \
  \    DomainJoined : NO\n               Device Name : Target-PC"
created_at: '2023-05-25T19:01:32.184127+00:00'
updated_at: '2023-05-25T19:01:32.394531+00:00'
---

# Display AzureAD status

```bash
dsregcmd.exe /status
```

## Expected Output

```
C:\ dsregcmd.exe /status

+----------------------------------------------------------------------+
| SSO State                                                            |
+----------------------------------------------------------------------+

                AzureAdPrt : YES
       AzureAdPrtAuthority : https://login.microsoftonline.com/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
             EnterprisePrt : NO
    EnterprisePrtAuthority : NO

+----------------------------------------------------------------------+
| Device State                                                         |
+----------------------------------------------------------------------+

             AzureAdJoined : YES
          EnterpriseJoined : NO
              DomainJoined : NO
               Device Name : Target-PC
```


