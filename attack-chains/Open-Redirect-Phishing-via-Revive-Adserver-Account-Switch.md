---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - open-redirect
  - phishing
  - revive-adserver
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Authenticate-to-Revive-Adserver-Admin]]'
  - '[[procedures/Exploit-Open-Redirect-in-Account-Switch]]'
step_count: 2
techniques:
  - '[[T1566.001]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.511Z'
description: >-
  Attack chain exploiting an open redirect vulnerability in Revive Adserver's
  account switch functionality to facilitate phishing by redirecting
  authenticated users to malicious external sites.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect Phishing via Revive Adserver Account Switch

Multi-stage attack chain demonstrating exploitation of an open redirect in Revive Adserver to trick users into visiting malicious sites for phishing.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Authenticate] --> B[Execution: Trigger Redirect]
    B --> C[Objective: Phishing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-open-redirect-test]]

### Target Environment

- Revive Adserver installation (PHP-based web application)
- Required services/ports: HTTP/HTTPS on standard ports, test port 12345 for local validation
- Network access requirements: Direct access to the admin interface

### Initial Access Requirements

- Valid user credentials for Revive Adserver
- Network position: Internal or external access to the web app
- Prior access needed: None, but authentication required

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Authenticate-to-Revive-Adserver-Admin]]

**Objective**: Gain authenticated access to the Revive Adserver admin interface to enable interaction with the vulnerable endpoint.

**Instructions**: Log in using valid credentials via the web interface or API. Verify session establishment by accessing protected admin pages.

**Expected Output**: Successful login redirect to the dashboard, with session cookies set.

**Success Indicators**:
- Access to /www/admin/ paths granted
- No authentication errors

### Step 2: Execution
procedure: [[procedures/Exploit-Open-Redirect-in-Account-Switch]]

**Objective**: Craft and trigger a malicious redirect URL to an external attacker-controlled site, enabling phishing.

**Instructions**: Construct the vulnerable URL with a malicious return_url parameter pointing to an attacker site (e.g., http://evil.com/phish). Use [[commands/curl-open-redirect-test]] to test the redirect:

```bash
curl -L -v "http://target.com/www/admin/account-switch.php?return_url=http://127.0.0.1:12345/test" --cookie "session=your_session_cookie"
```

Observe the 302 redirect to the arbitrary URL. In a real attack, obfuscate with similar domains or parameters to lure the victim.

**Expected Output**: HTTP 302 response redirecting to the specified return_url without validation.

**Success Indicators**:
- Redirect to external/malicious URL confirmed
- No domain whitelisting enforced

## Attack Chain Summary

### Key Achievements

1. Authenticated access to vulnerable endpoint
2. Unrestricted redirection to arbitrary domains
3. Enabled phishing for credential theft or further attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment (adapted for link-based phishing via redirect)
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T12:00:00Z*
