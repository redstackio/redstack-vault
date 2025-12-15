---
id: proc-001
tags:
  - spring-boot
  - actuator
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-endpoint]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.365Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Spring-Boot-Actuator-Heapdump-Endpoint

## Summary

This procedure involves directly accessing the exposed /actuator/heapdump endpoint in a misconfigured Spring Boot application to trigger the generation and exposure of a server memory dump.

## Description

In Spring Boot applications, actuator endpoints provide management and monitoring features. When misconfigured without authentication, the heapdump endpoint allows unauthorized users to download the JVM heap, which contains all in-memory data including sensitive strings and objects. This targets domains like my.stripo.email or plugins.stripo.email, leading to immediate data exposure upon access.

## Requirements

1. Public internet access to the target domain
2. Knowledge of the actuator path (e.g., /actuator/heapdump)
3. Web browser or curl tool for HTTP requests

## Defense

Defensive measures and detection strategies:

- Restrict actuator endpoints to localhost or authenticated access via Spring Security
- Monitor access logs for /actuator/heapdump requests and alert on unauthorized attempts
- Use web application firewalls (WAF) to block exposure of sensitive paths

## Objectives

1. Gain unauthorized access to server memory contents
2. Initiate download of heap dump for further analysis
3. Identify misconfigurations in public-facing Java applications

## Instructions

### Step 1: Identify Target Endpoint

**Context**: Determine the full URL of the actuator endpoint through reconnaissance or known paths.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl -I https://my.stripo.email/cabinet/stripeapi/actuator/heapdump
```

> This HEAD request checks if the endpoint is accessible, expecting a 200 OK response indicating exposure.

### Step 2: Trigger Full Access

**Context**: Proceed to full GET request to start the download process.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl https://plugins.stripo.email/actuator/heapdump > heapdump.hprof
```

> The server generates and streams the heap dump, which is saved locally for analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-endpoint]]

## Tools Used


## Tags

- [[spring-boot]]
- [[actuator]]
