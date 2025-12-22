---
type: procedure
description: >-
  Query the Spring Boot Actuator /health endpoint to gather information about
  the application's status and environment.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - insecure-management-interface
  - springboot-actuator
  - web-recon
commands:
  - '[[commands/curl-get-springboot-health]]'
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Enumerate-Spring-Boot-Actuator-Health-Endpoint

## Summary

This procedure demonstrates how to query the Spring Boot Actuator /health endpoint to retrieve the health status of a Spring Boot application. Attackers can use this exposed endpoint to gather information about the application's components, database connections, and overall environment without authentication, potentially revealing vulnerabilities or internal details for further exploitation.

## Description

Spring Boot Actuator is a feature that exposes production-ready endpoints for monitoring and managing applications. The /health endpoint, if not secured, returns a JSON response indicating the application's health status (e.g., UP or DOWN) and details about integrated components like databases or disk space. This can be accessed over the network via a simple HTTP GET request. In an attack scenario, this reconnaissance step helps identify live services, software versions, and potential weak points in web applications deployed on cloud or on-premises environments. The procedure assumes the endpoint is exposed on the default port 8080 but can be adapted. Success provides passive intelligence without triggering alerts, aiding in mapping the attack surface.

## Requirements

1. Network access to the target Spring Boot application (e.g., via direct IP or domain resolution).
2. Tools like curl installed on the attacker's machine for HTTP requests.
3. Knowledge of the target's base URL and port (default: http://target:8080).

## Defense

Defensive measures and detection strategies:

- Disable the /health endpoint entirely or restrict it to internal networks using Spring Boot configuration (management.endpoints.web.exposure.include=).
- Implement authentication and authorization, such as Spring Security, requiring API keys or roles to access actuator endpoints.
- Monitor HTTP access logs for repeated or anomalous requests to /actuator/* paths, using tools like ELK Stack or WAF rules to alert on unauthenticated probes.
- Use network segmentation to limit exposure of management interfaces to trusted IPs.

## Objectives

1. Retrieve the health status and component details of the Spring Boot application.
2. Identify potential vulnerabilities, such as outdated dependencies or misconfigurations revealed in the response.
3. Gather environmental intelligence to support subsequent attack steps, like targeting exposed services.

## Instructions

### Step 1: Query the Health Endpoint

**Context**: Send an HTTP GET request to the /health endpoint to fetch the application's status. This step verifies if the endpoint is exposed and retrieves basic information without authentication. Use curl for simplicity, ensuring verbose output to inspect headers and response.

**Command** ([[commands/curl-get-springboot-health]]):
```bash
curl -X GET http://$_TARGET:$_PORT/health -v
```

> This command performs a GET request to the /health path. The -v flag provides verbose details, including response headers. Replace $_TARGET with the application's IP or hostname and $_PORT with the listening port (default 8080). If successful, the response will be a JSON object showing the status and details of health indicators.
