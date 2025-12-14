---
tags:
  - information-disclosure
  - wordpress
  - php
  - full-path-disclosure
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
  - '[[procedures/Trigger-Full-Path-Disclosure-in-Podpress-Plugin]]'
step_count: 1
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:06.294Z'
description: >-
  A reconnaissance attack exploiting a syntax error in the Podpress plugin's
  write.php file to disclose the server's full file path and running user on a
  WordPress site.
skill_level: beginner
impact_level: medium
id: 1a4fbd38-d4bd-4439-b321-20e61c358943
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Full Path Disclosure via WordPress Podpress Plugin

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
    A[Reconnaissance] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-access-vulnerable-endpoint]]

### Target Environment

- Web platform with WordPress
- PHP-enabled server
- Accessible plugin directory

### Initial Access Requirements

- Public network access to the target URL
- No authentication required

## Detailed Attack Procedures

### Step 1: Trigger Path Disclosure
procedure: [[procedures/Trigger-Full-Path-Disclosure-in-Podpress-Plugin]]

**Objective**: Access the vulnerable PHP file to disclose the server's full file path and running user, providing reconnaissance data for potential further attacks.

**Instructions**: Use [[commands/curl-access-vulnerable-endpoint]] to directly access the write.php file in the Podpress plugin directory:

```bash
curl -s http://smarthistory.khanacademy.org/blog/wp-content/plugins/podpress/getid3/write.php
```

This request triggers the syntax error or misconfiguration in the file, causing it to output sensitive server information.

**Expected Output**: The response will include the absolute server path (e.g., "/var/www/html/...") and the user account (e.g., "www-data" or similar) under which the web server runs.

**Success Indicators**:
- Server path revealed in the output
- Running user account disclosed
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Obtained server's absolute file path for potential path traversal or local file inclusion attacks.
2. Identified the web server user, aiding in privilege escalation planning.
3. Demonstrated information disclosure without authentication.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
