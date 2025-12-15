---
id: ac-wordpress-outdated-exploitation
tags:
  - wordpress
  - information-disclosure
  - stored-xss
  - outdated-software
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Reconnaissance-of-WordPress-Version]]'
  - '[[procedures/Exploit-WordPress-REST-API-Info-Disclosure]]'
  - '[[procedures/Exploit-WordPress-Theme-Upload-Stored-XSS]]'
step_count: 3
techniques:
  - '[[Software]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:10.976Z'
description: >-
  Attack chain exploiting an outdated WordPress 4.6.2 installation on a
  public-facing website to disclose user information via REST API and inject
  stored XSS through malicious theme uploads.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Software]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Information Disclosure and Stored XSS via Outdated WordPress 4.6.2

Multi-stage attack chain demonstrating exploitation of an outdated WordPress 4.6.2 installation, as identified on Nextcloud's website, leading to user information disclosure via the REST API and stored XSS through malicious theme uploads. The chain begins with reconnaissance to confirm the vulnerable version, followed by direct exploitation of known vulnerabilities documented in WPVulnDB, potentially allowing attackers to extract sensitive user data or execute persistent JavaScript payloads.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Identify Outdated WordPress] --> B[Execution: Exploit REST API for Info Disclosure]
    B --> C[Execution: Stored XSS via Theme Upload]
    C --> D[Objective: Data Exfiltration and Persistence]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for manual testing
- curl for API requests

### Target Environment

- Web platform with WordPress 4.6.2
- Publicly accessible website
- No authentication required for initial recon and REST API access

### Initial Access Requirements

- Internet access to the target site
- No prior credentials needed
- Knowledge of WPVulnDB for vulnerability confirmation

## Detailed Attack Procedures

### Step 1: Reconnaissance of WordPress Version
procedure: [[procedures/Reconnaissance-of-WordPress-Version]]

**Objective**: Identify the WordPress version and confirm vulnerability to information disclosure and XSS issues listed in WPVulnDB.

**Instructions**: Inspect the website's technology stack using browser tools or online scanners to detect WordPress 4.6.2. Reference WPVulnDB for CVEs affecting this version, such as REST API user enumeration without authentication.

**Expected Output**: Confirmation of version 4.6.2 and associated vulnerabilities.

**Success Indicators**:
- Version string visible in source code or generator headers
- Vulnerabilities matched in WPVulnDB

### Step 2: Exploit WordPress REST API for Information Disclosure
procedure: [[procedures/Exploit-WordPress-REST-API-Info-Disclosure]]

**Objective**: Leverage the unauthenticated REST API in WordPress 4.6.2 to disclose user information, including usernames and potentially emails.

**Instructions**: Use curl to query the REST API endpoint for users. In WordPress 4.6.2, the /wp-json/wp/v2/users endpoint exposes user data without authentication due to missing permission checks.

Execute [[commands/curl-rest-api-query]] to fetch user list:

```bash
curl -s https://target.com/wp-json/wp/v2/users | jq '.[].name'
```

**Expected Output**: JSON response listing user details like IDs, names, and links.

**Success Indicators**:
- Usernames and metadata returned in JSON
- No 401/403 errors indicating public access

### Step 3: Exploit WordPress Theme Upload for Stored XSS
procedure: [[procedures/Exploit-WordPress-Theme-Upload-Stored-XSS]]

**Objective**: Upload a malicious theme ZIP containing XSS payload to achieve stored XSS, executable when admins install or view the theme.

**Instructions**: If admin access is obtained (e.g., via social engineering or other means), navigate to the theme installer. Craft a ZIP with a malicious PHP file embedding JavaScript. The lack of validation in class-theme-installer-skin.php allows payload injection.

Use browser or curl to simulate upload, but requires auth. For testing, assume dashboard access and upload a ZIP with <script>alert('XSS')</script> in a theme file.

**Expected Output**: Theme uploaded successfully, XSS triggers on admin view.

**Success Indicators**:
- Theme appears in admin dashboard
- Alert or payload executes on page load

## Attack Chain Summary

### Key Achievements

1. Confirmed outdated WordPress version vulnerable to multiple issues
2. Disclosed user information via public REST API
3. Injected persistent XSS for potential session hijacking or further exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Software]] Gather Victim Host Information: Software
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] Command and Scripting Interpreter: JavaScript

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
