---
tags:
  - information-disclosure
  - php
  - pdo
  - path-disclosure
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '[TIMESTAMP]'
procedures:
  - '[[procedures/Trigger-PDO-Quote-Error-for-Path-Disclosure]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:06.173Z'
description: >-
  A single-step attack exploiting improper array parameter handling in PHP's
  phraseChange or phrasemove actions to trigger a PDO::quote() error, resulting
  in information disclosure of server file paths.
id: e869b2fc-051e-4424-8d40-76f043aff85a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Full Path Disclosure via Malformed Array Parameter in PHP Phrase Management

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
    A[Initial Access via Web Request] --> B[Trigger Error and Disclose Paths]
    B --> C[Reconnaissance Complete]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- PHP-based web application with MySQL backend using PDO
- Exposed endpoints for phrase management (e.g., phraseChange or phrasemove actions)
- No authentication required if the endpoint is public

### Initial Access Requirements

- Direct HTTP access to the target web application
- Ability to submit POST requests with custom parameters
- No prior credentials needed if the vulnerability is unauthenticated

## Detailed Attack Procedures

### Step 1: Submit Malformed Parameter to Trigger Error
procedure: [[procedures/Trigger-PDO-Quote-Error-for-Path-Disclosure]]

**Objective**: Exploit the lack of input validation on the phrasekey parameter to pass an array, causing a PDO::quote() error that leaks server file paths in the exception message and stack trace.

**Instructions**: Use [[commands/curl-submit-malformed-phrasekey]] to send a POST request to the vulnerable endpoint with the phrasekey parameter formatted as an array (e.g., phraseChange[phraseKey][11]:test). This simulates submitting a form with nested array data, which the application mishandles.

```bash
curl -X POST 'http://target.com/path/to/endpoint.php' \
  -d 'action=phraseChange&phraseChange[phraseKey][11]=test' \
  -d 'other_params=value'
```

Monitor the response for PHP warnings and PDOException details.

**Expected Output**: HTTP response containing a PHP warning like "Warning: PDO::quote() expects parameter 1 to be string, array given" on line 30 of Database.php, followed by a fatal PDOException on line 53 with a SQL syntax error in the UPDATE phrases query, exposing paths such as "/srv/data/web/vhosts/www.localize.im/htdocs/classes/Database.php".

**Success Indicators**:
- Presence of PDO::quote() warning in response
- Stack trace revealing full server file paths
- SQL syntax error mentioning internal database file locations

## Attack Chain Summary

### Key Achievements

1. Successful trigger of unhandled array input leading to exception
2. Disclosure of sensitive server directory structure (e.g., /srv/data/web/vhosts/...)
3. Potential reconnaissance for further attacks like local file inclusion or path traversal

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---

*Last updated: [TIMESTAMP]*
