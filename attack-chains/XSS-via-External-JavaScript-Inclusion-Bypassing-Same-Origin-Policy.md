---
id: ac-uuid-1234
tags:
  - xss
  - external-scripts
  - dom-manipulation
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-and-Exploit-External-JavaScript-XSS]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:13.896Z'
description: >-
  Demonstrates how including JavaScript from external domains on a website can
  lead to XSS by allowing third-party scripts to manipulate the DOM, potentially
  injecting malicious code if the external source is compromised.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS via External JavaScript Inclusion Bypassing Same-Origin Policy

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify External Scripts] --> B[Exploit DOM Control]
    B --> C[Inject Malicious Code]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser Developer Tools

### Target Environment

- Web platform
- Publicly accessible website
- No specific services/ports required beyond HTTP/HTTPS

### Initial Access Requirements

- Network access to the target website
- No credentials needed for public pages
- Prior access not required

## Detailed Attack Procedures

### Step 1: Identify and Exploit External JavaScript
procedure: [[procedures/Identify-and-Exploit-External-JavaScript-XSS]]

**Objective**: Locate external JavaScript inclusions on the target website and demonstrate how they bypass the same-origin policy to enable XSS attacks.

**Instructions**: Open the target website in a browser and use developer tools to inspect the page source for script tags with external src attributes. For example, fetch the page using curl and grep for script sources:

```bash
curl -s https://stellar.org | grep -i '<script src='
```

Verify the external domains are unrelated to the site owner. If compromised, these scripts can manipulate the DOM.

**Expected Output**: List of external script URLs, e.g., scripts from analytics providers.

**Success Indicators**:
- External script sources identified
- Confirmation of third-party domain control over DOM

## Attack Chain Summary

### Key Achievements

1. Identified external JavaScript inclusions bypassing same-origin policy
2. Demonstrated potential for malicious code injection via compromised third-party servers
3. Highlighted risks to web application integrity

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
