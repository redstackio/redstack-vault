---
id: proc-gitlab-interact-internal-001
tags:
  - ssrf
  - gitlab
  - discovery
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:47.778Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Interact-with-Internal-Services-via-SSRF

## Summary

This procedure exploits the established SSRF in GitLab to interact with and extract data from unauthenticated internal or local services.

## Description

Once SSRF is triggered, attackers can target services bound to the server's localhost interface, such as metadata endpoints or admin panels on ports other than 22, 80, or 443. Without authentication, this leads to information disclosure (e.g., configs, user data) or further exploitation like RCE if the service is vulnerable. The attack relies on GitLab's response handling to leak internal data.

## Requirements

1. Confirmed SSRF from previous URL submission
2. Enumeration of internal ports/services (e.g., common ports like 8080, 3000)
3. Ability to iterate import attempts without rate limiting

## Defense

Defensive measures and detection strategies:

- Bind internal services only to non-loopback interfaces or use firewalls to block localhost access
- Implement authentication on all local services
- Use WAF rules to detect and block SSRF patterns in application logs

## Objectives

1. Access and read data from internal endpoints
2. Perform discovery of local network/services
3. Achieve information disclosure or pivot to further attacks

## Instructions

### Step 1: Target Specific Endpoints

**Context**: Refine the URL to probe specific paths on internal services.

Modify the import URL to `http://localhost:8080/api/v1/users` or similar, targeting known or guessed endpoints.

> Submit multiple times with variations to map the service.

### Step 2: Extract and Analyze Responses

**Context**: Capture leaked data from GitLab's error or status messages.

After submission, review the project import logs or error output for internal HTTP responses, such as JSON data or HTML snippets.

> Successful interaction shows raw internal content, indicating disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- gitlab
- discovery
- information-disclosure
