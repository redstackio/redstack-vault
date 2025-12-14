---
tags:
  - open-redirect
  - phishing
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
procedures:
  - '[[procedures/Test-Open-Redirect-with-Benign-URL]]'
  - '[[procedures/Exploit-Open-Redirect-with-Malicious-URL]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
description: >-
  Exploits an unvalidated open redirect vulnerability in the redirect.php
  endpoint on reviewnic.com to redirect users to malicious sites, enabling
  phishing, malware delivery, and reputation damage.
skill_level: beginner
impact_level: medium
id: 9681d4a2-1ebc-4e92-8f64-b25c8ac8a8c0
created_at: '2025-12-14T17:24:23.199Z'
updated_at: '2025-12-14T17:24:23.199Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Phishing via Unvalidated Open Redirect in redirect.php

Multi-stage attack chain demonstrating exploitation of an open redirect vulnerability to trick users into visiting malicious sites under the guise of a legitimate domain.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Test Benign Redirect] --> B[Exploit with Malicious URL]
    B --> C[Phishing Success]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/curl-open-redirect-test]]

### Target Environment

- Web platform
- Public access to https://reviewnic.com/redirect.php
- No authentication required

### Initial Access Requirements

- Internet access
- No prior credentials or network position needed

## Detailed Attack Procedures

### Step 1: Test Open Redirect with Benign URL
procedure: [[procedures/Test-Open-Redirect-with-Benign-URL]]

**Objective**: Verify the open redirect vulnerability by confirming that the endpoint redirects to a trusted external site without validation.

**Instructions**: Use a web browser or curl to access the endpoint with a benign URL parameter. For example, execute [[commands/curl-open-redirect-test]] with the benign target:

```bash
curl -L "https://reviewnic.com/redirect.php?url=http://bing.com"
```

Follow the redirect manually in a browser if using curl, or directly visit the URL.

**Expected Output**: Successful HTTP redirect (e.g., 302 status) to http://bing.com, confirming the endpoint accepts and follows arbitrary URLs.

**Success Indicators**:
- Browser or curl follows to bing.com
- No error or validation blocking the redirect

### Step 2: Exploit Open Redirect with Malicious URL
procedure: [[procedures/Exploit-Open-Redirect-with-Malicious-URL]]

**Objective**: Redirect users to a controlled malicious site to conduct phishing or deliver malware, leveraging the trusted domain for deception.

**Instructions**: Modify the URL parameter to point to an attacker-controlled site. Craft a link like https://reviewnic.com/redirect.php?url=http://evilsite-of-attacker.com and distribute it via email, social engineering, or ads. Test with [[commands/curl-open-redirect-exploit]]:

```bash
curl -L "https://reviewnic.com/redirect.php?url=http://evilsite-of-attacker.com"
```

In a real attack, embed this link in phishing emails or posts to trick victims into clicking, leading them to the malicious site for credential theft.

**Expected Output**: Redirect to the attacker's site, where phishing pages or malware can be hosted.

**Success Indicators**:
- Victim redirected to malicious domain
- Potential capture of credentials or malware infection

## Attack Chain Summary

### Key Achievements

1. Confirmed open redirect vulnerability without validation
2. Enabled redirection to arbitrary external sites
3. Facilitated phishing attacks by masquerading as legitimate redirects

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: [TIMESTAMP]*
