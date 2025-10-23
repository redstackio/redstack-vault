---
id: ef7a4996-bb61-42a2-9872-3053bb0cb10b
name: Convert UTF-8 encoded XML file to UTF-16BE
type: command
executor: bash
data: cat utf8exploit.xml | iconv -f UTF-8 -t UTF-16BE > utf16exploit.xml
output: null
created_at: '2023-04-06T03:56:44.518806+00:00'
updated_at: '2023-04-10T20:24:43.882810+00:00'
---

# Convert UTF-8 encoded XML file to UTF-16BE

```bash
cat utf8exploit.xml | iconv -f UTF-8 -t UTF-16BE > utf16exploit.xml
```


