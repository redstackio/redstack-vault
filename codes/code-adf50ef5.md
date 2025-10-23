---
id: adf50ef5-a870-4c5f-93cc-34a993073e8b
type: code
language: Bash
verified: false
created_at: '2020-07-14T19:07:50.931656+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet adf50ef5

**Language**: Bash

```bash

$users = Get-MsolUser; foreach($user in $users){$props = @();$user | Get-Member | foreach-object{$props+=$_.Name}; foreach($prop in $props){if($user.$prop -like "*password*"){Write-Output ("[*]" + $user.UserPrincipalName + "[" + $prop + "]" + " : " + $user.$prop)}}}

```


