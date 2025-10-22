---
id: 3f6c0851-fd6a-4602-8540-3f3632591306
name: Query Windows Registry for Auto Logon Credentials
type: command
executor: command_prompt
data: reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
output: "PS C:\\> reg query \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\Currentversion\\\
  Winlogon\"\n\nHKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\Currentversion\\\
  Winlogon\n    AutoRestartShell    REG_DWORD    0x1\n    Background    REG_SZ   \
  \ 0 0 0\n    CachedLogonsCount    REG_SZ    10\n    DebugServerCommand    REG_SZ\
  \    no\n    DefaultDomainName    REG_SZ    MEGABANK\n    DefaultUserName    REG_SZ\
  \    MEGABANK\\service\n...\n    ShutdownFlags    REG_DWORD    0x80000027\n    DisableLockWorkstation\
  \    REG_DWORD    0x0\n    DefaultPassword    REG_SZ    IcanhasCash!"
created_at: '2020-03-17T23:49:26.705170+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Query Windows Registry for Auto Logon Credentials

```command_prompt
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
```

## Expected Output

```
PS C:\> reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon
    AutoRestartShell    REG_DWORD    0x1
    Background    REG_SZ    0 0 0
    CachedLogonsCount    REG_SZ    10
    DebugServerCommand    REG_SZ    no
    DefaultDomainName    REG_SZ    MEGABANK
    DefaultUserName    REG_SZ    MEGABANK\service
...
    ShutdownFlags    REG_DWORD    0x80000027
    DisableLockWorkstation    REG_DWORD    0x0
    DefaultPassword    REG_SZ    IcanhasCash!
```
