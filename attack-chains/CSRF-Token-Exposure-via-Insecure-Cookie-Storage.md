---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: CSRF Token Exposure via Insecure Cookie Storage
tags:
  - csrf
  - cookies
  - web-security
  - misconfiguration
type: attack_chain
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Intercept-HTTP-Requests-to-Reveal-CSRF-Token-in-Cookies]]'
step_count: 1
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:03.669Z'
description: >-
  This attack chain demonstrates the discovery of a security misconfiguration
  where CSRF tokens are stored in cookies, potentially exposing them to theft
  via XSS or network interception, enabling request forgery.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# CSRF Token Exposure via Insecure Cookie Storage

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Intercept Request] --> B[Analyze Token Storage]
    B --> C[Potential Exposure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web proxy tool (e.g., browser developer tools or Burp Suite)

### Target Environment

- Web application with user authentication
- Access to edit endpoints (e.g., statement editing functionality)

### Initial Access Requirements

- Valid user session
- Ability to perform authenticated POST requests
- Network access to the target web app

## Detailed Attack Procedures

### Step 1: Intercept and Analyze Request
procedure: [[procedures/Intercept-HTTP-Requests-to-Reveal-CSRF-Token-in-Cookies]]

**Objective**: Capture an HTTP POST request to an edit endpoint to observe CSRF token storage in cookies.

**Instructions**: Log in to the web application and navigate to the statement editing feature. Use a proxy or browser developer tools to intercept the POST request to the endpoint (e.g., /~[USER ID]/statement.json). Examine the request headers and cookies for the presence of a 'csrf_token' cookie.

**Expected Output**: The request will show a 'csrf_token' cookie with a value (e.g., y44PyqG67bRQljEA5mLK1bez4hgZ8XSD) that matches the X-CSRF-Token header, indicating insecure storage.

**Success Indicators**:
- CSRF token visible in the 'csrf_token' cookie
- Token value matches the X-CSRF-Token header
- No separation between token storage and transmission mechanisms

## Attack Chain Summary

### Key Achievements

1. Identified insecure CSRF token storage in cookies
2. Demonstrated potential for token exposure via cookie compromise
3. Highlighted risk of CSRF bypass if tokens are stolen

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Collection]]

---
*Last updated: 2023-10-01T12:00:00Z*
