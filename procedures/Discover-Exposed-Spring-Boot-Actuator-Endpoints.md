---
tags:
  - spring-boot
  - actuator
  - misconfiguration
  - discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: c8cb8363-1a11-4a75-bd7b-1b9a50197ecc
created_at: '2025-12-11T03:47:47.674Z'
updated_at: '2025-12-11T03:47:47.674Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Discover Exposed Spring Boot Actuator Endpoints

## Summary

This procedure involves identifying publicly accessible Spring Boot Actuator endpoints such as /heapdump and /env that lack proper access controls, allowing unauthorized users to retrieve sensitive application data.

## Description

In Spring Boot applications, Actuator endpoints provide monitoring and management capabilities. When misconfigured, these can be exposed publicly, leading to leakage of heap dumps and environment variables. This procedure outlines steps to discover such exposures in sensitive web applications.

## Requirements

1. Public network access to the target web application
2. Basic HTTP client like curl
3. Knowledge of common Actuator endpoint paths

## Defense

Defensive measures and detection strategies:

- Implement strict access controls and authentication for Actuator endpoints
- Monitor HTTP logs for unauthorized access attempts to /actuator paths

## Objectives

1. Confirm public accessibility of sensitive endpoints
2. Identify potential information leakage vectors
3. Document endpoints for further exploitation

## Instructions

### Step 1: Probe Common Actuator Endpoints

**Context**: Send HTTP requests to known Actuator paths to check for public exposure.

**Command** ([[commands/curl-access-actuator-endpoint]]):
```bash
curl -v https://target-app.com/actuator/heapdump
```

> This command attempts to access the heapdump endpoint; expect a successful response with heap data if exposed.

### Step 2: Verify Environment Endpoint

**Context**: Check the /env endpoint for environment variable exposure.

**Command** ([[commands/curl-access-actuator-endpoint]]):
```bash
curl -v https://target-app.com/actuator/env
```

> Look for JSON output containing sensitive environment variables like database credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-access-actuator-endpoint]]

## Tools Used

- #curl

## Tags

- #spring-boot
- [[commands/curl-access-actuator-endpoint]]
