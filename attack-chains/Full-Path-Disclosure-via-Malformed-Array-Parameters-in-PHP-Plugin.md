---
tags:
  - information-disclosure
  - path-disclosure
  - php
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Inspect-Element]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Path-Disclosure-via-Malformed-URL-Parameter]]'
  - '[[procedures/Modify-Form-Fields-for-PHP-Error-Disclosure]]'
step_count: 2
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.333Z'
description: >-
  A multi-step attack exploiting a Full Path Disclosure vulnerability in the
  basic-google-maps-placemarks plugin by submitting malformed array parameters
  to trigger PHP errors revealing server file paths.
skill_level: beginner
impact_level: medium
id: 1a994b82-1b59-4edb-ba10-f8fe820c2deb
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Full Path Disclosure via Malformed Array Parameters in PHP Plugin

Multi-stage attack chain demonstrating exploitation of a Full Path Disclosure (FPD) vulnerability in the basic-google-maps-placemarks plugin, where malformed array parameters trigger PHP errors that reveal sensitive server paths, aiding in filesystem mapping for further attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Vulnerable Endpoint] --> B[Trigger PHP Error]
    B --> C[Disclose Server Paths]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]
- [[tools/Inspect-Element]]

### Target Environment

- Web platform with PHP backend
- basic-google-maps-placemarks plugin installed
- Access to index.php endpoint

### Initial Access Requirements

- Public network access to the target web application
- No credentials required
- Browser with developer tools

## Detailed Attack Procedures

### Step 1: Access Vulnerable Endpoint with Malformed Parameter
procedure: [[procedures/Trigger-Path-Disclosure-via-Malformed-URL-Parameter]]

**Objective**: Submit a malformed array parameter to the index.php endpoint to trigger a PHP parsing error or notice that discloses the server path.

**Instructions**: Open Firefox and navigate directly to the vulnerable URL with the injected parameter. For example, append `step[]=4'` to the query string, where the single quote and array syntax causes a syntax error in PHP array handling.

**Expected Output**: A PHP error message displayed in the browser, such as a notice about an undefined array index, including the full server path to the webroot or affected files (e.g., `/var/www/html/path/to/index.php on line X`).

**Success Indicators**:
- Error message appears in the browser
- Full file path is visible in the error output
- Path reveals filesystem structure like `/home/user/public_html/`

### Step 2: Modify Form Fields to Trigger Disclosure
procedure: [[procedures/Modify-Form-Fields-for-PHP-Error-Disclosure]]

**Objective**: Use browser developer tools to alter form input values in the plugin, appending empty array syntax to induce PHP notices that leak additional path information.

**Instructions**: Load the basic-google-maps-placemarks plugin page in Firefox, open Inspect Element, locate a form field (e.g., an input for placemark data), and modify its value by appending `[]` (empty array). Submit the form to trigger the error.

**Expected Output**: PHP warning or notice in the response, disclosing paths similar to the first step, potentially revealing plugin-specific file locations.

**Success Indicators**:
- Modified form submission results in error
- Additional paths disclosed, confirming filesystem mapping
- No successful form processing; error halts execution

## Attack Chain Summary

### Key Achievements

1. Successful triggering of PHP errors via URL manipulation
2. Path disclosure enabling filesystem reconnaissance
3. Potential setup for chained attacks like local file inclusion

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
