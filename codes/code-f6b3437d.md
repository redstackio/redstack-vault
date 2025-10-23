---
id: f6b3437d-f33f-4697-8bbf-bf5027787070
type: code
language: ''
verified: false
created_at: '2023-02-18T22:52:32.341364+00:00'
updated_at: '2023-03-13T19:50:21.945040+00:00'
---

# Code Snippet f6b3437d

```
Syntax
      cmdkey [{/add:TargetName|/generic:TargetName}]
         {/smartcard|/user:UserName [/pass:Password]}
            [/delete{:TargetName|/ras}]
               /list:TargetName

Key:
   /add            Add a user name and password to the list.

   TargetName      The computer or domain name that this entry will be associated with.

   /generic        Add generic credentials to the list (used by RDC).

   /smartcard      Retrieve the credential from a smart card.

   /user:UserName  The user or account name to store with this entry.
                   If UserName is not supplied, it will be requested.

   /pass:Password  The password to store with this entry. If Password is not supplied, it will be requested.

   /delete:        Delete a user name and password from the list.
                   If TargetName is specified, that entry will be deleted.
                   If /ras is specified, the stored remote access entry will be deleted.

   /list           Display the list of stored user names and credentials.
                   If TargetName is not specified, all stored user names and credentials will be listed.
```


