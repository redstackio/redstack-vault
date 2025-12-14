---
id: proc-uuid-003
tags:
  - information-disclosure
  - dashboard-access
  - spring-boot
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-dashboard]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:44.404Z'
skill_level: beginner
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Access Spring Boot Admin Dashboard

## Summary

This procedure uses an established session to load and interact with the Spring Boot Admin dashboard, enabling the viewing of application metrics, health status, and potential sensitive configurations for information disclosure.

## Description

Once authenticated, the dashboard provides oversight of registered Spring Boot applications, including endpoints, logs, and environmental variables. This procedure focuses on retrieving and analyzing this data, which could reveal internal architecture or misconfigurations. It applies to web-based admin interfaces and assumes prior login success, with outcomes varying based on the instance's content—though no sensitive data was noted in the original report.

## Requirements

1. Valid session cookies from successful login
2. Access to the dashboard URI (e.g., /admin/applications)
3. Tool for authenticated HTTP requests

## Defense

Defensive measures and detection strategies:

- Disable or remove Spring Boot Admin in production unless necessary
- Encrypt and restrict dashboard data exposure
- Implement session timeouts and audit dashboard access logs

## Objectives

1. Load the administrative dashboard with valid credentials
2. Collect application information for reconnaissance or disclosure
3. Assess the instance for further vulnerabilities

## Instructions

### Step 1: Load Dashboard with Session

**Context**: Use the authentication cookie to access protected views.

**Command** ([[commands/curl-access-dashboard]]):
```bash
curl -b cookies.txt http://target.com/admin/applications
```

> This fetches the applications list. Parse the HTML/JSON for details like instance names, health, and metrics.

### Step 2: Review Exposed Information

**Context**: Analyze dashboard content for valuable data.

Inspect the output for application endpoints, JVM info, or logs. In a browser, interact with tabs for deeper views.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-access-dashboard]]

## Tools Used

- [[tools/curl]]

## Tags

- information-disclosure
- dashboard-access
- spring-boot
