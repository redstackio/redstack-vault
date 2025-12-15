---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - open-redirect
  - phishing
  - revive-adserver
  - bypass
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
  - >-
    [[procedures/Bypass-Open-Redirect-Filter-in-Revive-Adserver-with-Multiple-Slashes]]
step_count: 1
techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.600Z'
description: >-
  This attack chain exploits an open redirect vulnerability in Revive Adserver
  by bypassing the return_url filter with multiple slashes, enabling redirection
  of authenticated users to external malicious sites for phishing.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect Bypass in Revive Adserver Using Multiple Slashes for Phishing

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Admin Endpoint] --> B[Bypass Filter and Redirect]
    B --> C[Phishing Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- Web platform running Revive Adserver (PHP-based)
- Access to /www/admin/campaign-modify.php endpoint
- Authentication as an admin user

### Initial Access Requirements

- Valid credentials for Revive Adserver admin panel
- Network access to the target server
- No prior access beyond authentication needed

## Detailed Attack Procedures

### Step 1: Bypass Open Redirect and Trigger Phishing
procedure: [[procedures/Bypass-Open-Redirect-Filter-in-Revive-Adserver-with-Multiple-Slashes]]

**Objective**: Craft a malicious return_url parameter to bypass the filter and redirect the victim to an external phishing site, luring them under the guise of a legitimate redirect.

**Instructions**: Authenticate to the Revive Adserver admin panel, then access the campaign-modify.php endpoint with a crafted return_url using multiple slashes (////) prefixed to the target domain. Use [[commands/curl-test-open-redirect]] to simulate and verify the redirect:

```bash
curl -X GET "http://target.com/www/admin/campaign-modify.php?clientid=&campaignid=&returnurl=%2F%2F%2F%2Fhackerone.com" -i
```

Follow up by sending the crafted URL to the victim via email or link, ensuring they are authenticated.

**Expected Output**: HTTP response with a 302 redirect (Location header pointing to /////hackerone.com, which resolves to external site).

**Success Indicators**:
- Redirect Location header shows external domain
- Browser or curl follows to malicious site
- No filter blocking observed

## Attack Chain Summary

### Key Achievements

1. Successful bypass of return_url filter using multiple slashes
2. Redirection to arbitrary external domain
3. Enablement of phishing attacks on authenticated users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T12:00:00Z*
