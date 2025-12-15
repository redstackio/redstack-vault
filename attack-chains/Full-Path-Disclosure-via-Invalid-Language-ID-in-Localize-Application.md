---
tags:
  - information-disclosure
  - path-disclosure
  - php
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
  - '[[procedures/Trigger-Full-Path-Disclosure-via-Invalid-Language-ID]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:06.156Z'
description: >-
  A reconnaissance attack exploiting an unhandled PHP exception in the Localize
  web application to disclose internal server file paths through a malformed
  URL.
skill_level: beginner
impact_level: medium
id: c3ac21d6-6913-42bf-a1df-061374762d04
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Full Path Disclosure via Invalid Language ID in Localize Application

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
    A[Reconnaissance: Access Malformed URL] --> B[Information Disclosure: Extract Server Paths]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-access-invalid-language-url]]

### Target Environment

- Web platform with PHP backend
- Access to public-facing Localize application endpoint
- No authentication required

### Initial Access Requirements

- Internet access to the target URL
- No prior credentials or network position needed

## Detailed Attack Procedures

### Step 1: Trigger Path Disclosure
procedure: [[procedures/Trigger-Full-Path-Disclosure-via-Invalid-Language-ID]]

**Objective**: Access the language selection endpoint with an invalid ID to provoke a PHP exception and reveal internal server file paths.

**Instructions**: Use [[commands/curl-access-invalid-language-url]] to send a request to the malformed URL:

```bash
curl "https://www.localize.im/projects/3t/languages/4xX"
```

Alternatively, navigate directly to the URL in a web browser.

**Expected Output**: An HTTP response containing a PHP fatal error message, including stack trace details like "/srv/data/web/vhosts/www.localize.im/htdocs/classes/Language.php".

**Success Indicators**:
- Error page displays full server paths
- Stack trace includes absolute file system locations

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of internal server paths without authentication
2. Identification of PHP application structure for further reconnaissance
3. Mapping of file system layout to aid potential escalation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
