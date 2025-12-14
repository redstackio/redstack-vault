---
tags:
  - open-redirect
  - phishing
  - revive-adserver
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Identify-Revive-Adserver-Tracking-Scripts]]'
  - '[[procedures/Test-Open-Redirect-Parameters]]'
  - '[[procedures/Demonstrate-Open-Redirect-Impact]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
description: >-
  This attack chain exploits a design flaw in Revive Adserver's impression and
  click tracking scripts, allowing arbitrary redirects to malicious URLs via
  unvalidated parameters, enabling phishing from trusted domains.
skill_level: beginner
impact_level: high
id: 8c0abd97-1052-4d2e-9f80-d31c9c65d72f
created_at: '2025-12-14T17:24:23.037Z'
updated_at: '2025-12-14T17:24:23.037Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Open Redirect in Revive Adserver ck.php and lg.php for Phishing Attacks

Multi-stage attack chain demonstrating exploitation of an open redirect vulnerability in Revive Adserver, a PHP-based ad serving platform. The flaw, present since early versions, allows attackers to craft URLs that redirect users from trusted ad server domains to malicious sites, facilitating phishing, malware distribution, or drive-by downloads without user awareness.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Tracking Scripts] --> B[Test Redirect Parameters]
    B --> C[Demonstrate Malicious Redirect]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/curl-test-open-redirect]] for testing redirects

### Target Environment

- Revive Adserver instance (PHP-based web application)
- Accessible web server hosting ck.php or lg.php
- No specific ports beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Public access to the Revive Adserver domain
- No credentials required
- Ability to craft and visit URLs

## Detailed Attack Procedures

### Step 1: Identify Tracking Scripts
procedure: [[procedures/Identify-Revive-Adserver-Tracking-Scripts]]

**Objective**: Locate the vulnerable ck.php and lg.php endpoints used for ad impression and click tracking in Revive Adserver.

**Instructions**: Inspect the target website for ad-related URLs or directly access common paths like /ck.php or /lg.php on the ad server domain. These scripts handle tracking and accept redirect parameters.

**Expected Output**: Confirmation of script accessibility, e.g., a tracking response or redirect prompt.

**Success Indicators**:
- Scripts respond to requests
- Parameters like dest are accepted

### Step 2: Test Open Redirect Parameters
procedure: [[procedures/Test-Open-Redirect-Parameters]]

**Objective**: Verify the open redirect by supplying arbitrary URLs to dest, oadest, or ct0 parameters in ck.php or lg.php.

**Instructions**: Use [[commands/curl-test-open-redirect]] to send a request with a test URL:

```bash
curl -L "http://target.com/ck.php?dest=http://example.com/test"
```

Observe the final redirect location in the response headers or output.

**Expected Output**: HTTP 302 redirect to the supplied URL without validation.

**Success Indicators**:
- Redirect occurs to external domain
- No error or blocking

### Step 3: Demonstrate Impact
procedure: [[procedures/Demonstrate-Open-Redirect-Impact]]

**Objective**: Show how the redirect can lead to phishing by crafting a malicious URL on a trusted domain.

**Instructions**: Replace the test URL with a phishing site, e.g., http://target.com/ck.php?dest=http://malicious-phish.com. Visit in a browser to simulate user flow.

**Expected Output**: Seamless redirect to the malicious site, potentially without user notice.

**Success Indicators**:
- User redirected to attacker-controlled site
- Trusted domain masks the redirect

## Attack Chain Summary

### Key Achievements

1. Identified exploitable tracking scripts in Revive Adserver
2. Confirmed lack of URL validation in redirect parameters
3. Enabled phishing attacks via trusted domain redirects

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
