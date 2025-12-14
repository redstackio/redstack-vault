---
id: ac-uuid-001
tags:
  - information-disclosure
  - reconnaissance
  - apache
  - htaccess
  - javascript
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Apache
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Retrieve-Public-Htaccess-Configuration-File]]'
  - '[[procedures/Access-Exposed-Sprockets-Js-Source-Code]]'
step_count: 2
techniques:
  - '[[Software]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:18.101Z'
description: >-
  A reconnaissance attack exploiting misconfigurations on a Basecamp subdomain
  to disclose Apache server details and JavaScript source code.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
  - '[[Exploit Public-Facing Application]]'
---
# Information Disclosure via Public .htaccess and Sprockets.js Access on Basecamp Subdomain

Multi-stage attack chain demonstrating reconnaissance through misconfigured public file access on a static subdomain.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Access .htaccess] --> B[Further Recon: Access sprockets.js]
    B --> C[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- Web platform with Apache server
- Publicly accessible subdomain
- No authentication required

### Initial Access Requirements

- Internet access to the target URL
- No credentials needed
- Basic knowledge of URL manipulation

## Detailed Attack Procedures

### Step 1: Retrieve .htaccess File
procedure: [[procedures/Retrieve-Public-Htaccess-Configuration-File]]

**Objective**: Access and download the publicly exposed .htaccess file to disclose server configuration details.

**Instructions**: Use a browser or HTTP client to append /.htaccess to the subdomain URL. Alternatively, execute [[commands/curl-retrieve-htaccess]] to fetch the file contents:

```bash
curl https://_domainkey.launchpad.37signals.com/.htaccess -o htaccess.txt
```

Review the downloaded file for directives like Options +ExecCGI +MultiViews +FollowSymLinks, AddHandler cgi-script .cgi, php_value include_path, and Rewrite rules.

**Expected Output**: A text file containing Apache configuration directives, triggering a download popup in browsers.

**Success Indicators**:
- File downloads successfully without errors
- Contents reveal server configs like CGI handlers and rewrite rules

### Step 2: Access Sprockets.js Source Code
procedure: [[procedures/Access-Exposed-Sprockets-Js-Source-Code]]

**Objective**: Retrieve the sprockets.js file to inspect exposed JavaScript source code, including internal scripts.

**Instructions**: Navigate to the sprockets.js endpoint on the subdomain. Use [[commands/curl-access-sprockets-js]] to download the file:

```bash
curl https://_domainkey.launchpad.37signals.com/sprockets.js -o sprockets.js
```

Examine the file for JavaScript code, such as prototype pollution prevention scripts.

**Expected Output**: JavaScript source code file with client-side scripts visible.

**Success Indicators**:
- File loads without restrictions
- Source code includes internal details like pollution mitigation logic

## Attack Chain Summary

### Key Achievements

1. Exposed Apache .htaccess configuration aiding further reconnaissance
2. Disclosed JavaScript source code, though assessed as non-sensitive
3. Demonstrated low-severity information disclosure on a static site

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Software]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
