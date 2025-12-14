---
id: proc-838635-001
tags:
  - spring-boot
  - actuator
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Spring Boot
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:31:52.925Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Exposed-Spring-Actuator-Endpoints

## Summary

This procedure identifies publicly accessible Spring Boot Actuator endpoints such as /heapdump and /env, which are misconfigured without authentication, enabling reconnaissance of sensitive application internals in web-based environments.

## Description

Spring Boot Actuator provides production-ready features for monitoring and management, but by default, endpoints like /heapdump (memory dumps) and /env (environment variables) can be exposed if not secured. In this scenario, targeting sensitive applications, the lack of access controls allows attackers to probe and confirm exposure without credentials. Prerequisites include knowledge of the target URL and basic HTTP probing capabilities. Expected outcomes include confirmation of endpoint availability, setting the stage for data exfiltration.

## Requirements

1. Network access to the target Spring Boot application (e.g., public-facing URL)
2. HTTP client like browser or curl for probing
3. No authentication required due to misconfiguration

## Defense

Defensive measures and detection strategies:

- Enable Spring Security on Actuator endpoints with role-based access (e.g., management endpoints restricted to ADMIN)
- Monitor access logs for probes to /actuator/* paths and alert on unauthorized 200 responses
- Use web application firewalls (WAF) to block access to sensitive endpoints

## Objectives

1. Confirm exposure of /heapdump and /env without authentication
2. Assess the application's sensitivity based on accessible data
3. Prepare for subsequent leakage exploitation

## Instructions

### Step 1: Probe for Actuator Base Path

**Context**: Check if the Actuator module is enabled by accessing the root /actuator endpoint, which lists available endpoints if exposed.

**Command** (using curl to test accessibility):
```bash
curl -v https://target-app.com/actuator
```

> This command sends a GET request to /actuator. A successful response (200 OK) with a JSON array of endpoints indicates exposure. Look for /heapdump and /env in the list.

### Step 2: Verify Specific Endpoints

**Context**: Directly probe the sensitive endpoints to confirm public access.

**Command** (test /env endpoint):
```bash
curl https://target-app.com/actuator/env
```

> Expect a JSON response with environment properties. If it returns without auth challenge, the endpoint is vulnerable. Repeat for /heapdump, which should return a binary file.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- None (uses standard HTTP requests)

## Tools Used

- None

## Tags

- [[spring-boot]]
- [[actuator]]
- [[Reconnaissance]]
