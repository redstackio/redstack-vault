---
tags:
  - tomcat
  - misconfiguration
  - authentication-bypass
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-tomcat-endpoints]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Discover-and-Access-Exposed-Tomcat-Management-Interfaces]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  A misconfiguration in Apache Tomcat exposes administrative endpoints without
  authentication, allowing unauthorized access to server management functions.
skill_level: beginner
impact_level: high
id: 61b117f0-1892-404a-8fac-c16c94055309
created_at: '2025-12-14T17:31:19.726Z'
updated_at: '2025-12-14T17:31:19.726Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Access to Apache Tomcat Admin Interfaces via Misconfiguration

## Overview

This attack chain demonstrates how a misconfiguration in an Apache Tomcat server can expose sensitive administrative endpoints like /admin and /manager without requiring authentication. In the reported incident, a host in a pilot environment was vulnerable, allowing unauthorized users to access server management and deployment capabilities. The chain focuses on reconnaissance to identify the exposure and subsequent unauthorized access, highlighting risks in web application server configurations. The vulnerability was rectified by restricting endpoint access, but it underscores the need for proper authentication controls on admin interfaces.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover Exposed Endpoints] --> B[Initial Access: Unauthorized Admin Access]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/curl-check-tomcat-endpoints]]

### Target Environment

- Apache Tomcat server (version unspecified, but typically 7.x-10.x)
- Exposed web service on standard HTTP/HTTPS port (e.g., 8080)
- Network access to the target host

### Initial Access Requirements

- No credentials required due to misconfiguration
- Direct network connectivity to the pilot or production environment
- No prior access needed; public-facing or internally accessible host

## Detailed Attack Procedures

### Step 1: Reconnaissance and Unauthorized Access
procedure: [[procedures/Discover-and-Access-Exposed-Tomcat-Management-Interfaces]]

**Objective**: Identify and gain unauthorized access to Tomcat's /admin and /manager endpoints to perform server administration tasks.

**Instructions**: Begin by enumerating common Tomcat paths on the target host using [[commands/curl-check-tomcat-endpoints]] to probe for exposure:

```bash
curl -s http://target-host:8080/admin | grep -i "tomcat"
```

If the endpoint responds with Tomcat management content (e.g., login page or dashboard without auth prompt), access it directly in a browser by navigating to http://target-host:8080/admin or http://target-host:8080/manager. No credentials are needed due to the misconfiguration, allowing immediate interaction with deployment and configuration tools.

**Expected Output**: HTTP response containing Tomcat admin interface elements, such as HTML forms for server status or application deployment, without authentication challenges.

**Success Indicators**:
- 200 OK response from /admin or /manager without redirect to login
- Visible admin dashboard or management options in browser
- Ability to view server information or deploy applications

## Attack Chain Summary

### Key Achievements

1. Identified misconfigured Tomcat endpoints during reconnaissance
2. Gained unauthorized access to administrative functions
3. Highlighted potential for full server compromise via deployment capabilities

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
