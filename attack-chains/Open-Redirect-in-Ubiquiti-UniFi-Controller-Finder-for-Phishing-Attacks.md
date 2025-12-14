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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Open-Redirect-in-UniFi-Controller-Finder]]'
step_count: 1
techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.628Z'
description: >-
  A phishing attack leveraging an open redirect vulnerability in the UniFi
  Controller Finder feature on unifi.ubnt.com, allowing redirection to malicious
  sites without validation.
skill_level: beginner
impact_level: medium
id: 52b1942b-d27d-4910-9ad2-3038d5cc535a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect in Ubiquiti UniFi Controller Finder for Phishing Attacks

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect vulnerability to enable phishing.

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
    A[Initial Access via Phishing Link] --> B[Redirection to Malicious Site]
    B --> C[User Interaction on Malicious Domain]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[Burp Suite]] for testing

### Target Environment

- Web platform
- Access to unifi.ubnt.com Controller Finder feature
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- No credentials required
- Public network access to unifi.ubnt.com
- Ability to craft and distribute URLs

## Detailed Attack Procedures

### Step 1: Craft and Distribute Phishing Redirect Link
procedure: [[procedures/Exploit-Open-Redirect-in-UniFi-Controller-Finder]]

**Objective**: Exploit the open redirect parameter in the Controller Finder to redirect users to a malicious phishing site, tricking them into providing credentials or downloading malware.

**Instructions**: Identify the vulnerable endpoint in the Controller Finder, which accepts a redirect parameter (e.g., 'url') without validation. Craft a malicious URL like `https://unifi.ubnt.com/controller-finder?redirect=https://malicious-site.com/phish`. Distribute this link via email, social engineering, or other phishing vectors. When a user clicks it, the application redirects them to the malicious domain without warning.

To test the vulnerability manually, use a browser or curl to verify the redirect:

```bash
curl -L -I "https://unifi.ubnt.com/controller-finder?redirect=https://example.com"
```

**Expected Output**: HTTP response showing a 3xx redirect status (e.g., 302 Found) to the specified URL, confirming no validation.

**Success Indicators**:
- Redirect occurs to arbitrary domain
- No error or validation blocks the redirect
- User is seamlessly sent to phishing site

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of open redirect for phishing link creation
2. Potential for credential theft or malware delivery via redirected traffic
3. Demonstration of impact on user trust in legitimate Ubiquiti domains

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
