---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Open Redirect in VK.com Mobile Photos Feature for Phishing Attacks
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
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploiting-Open-Redirect-in-VK-Mobile-Photos]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.741Z'
description: >-
  An attack chain exploiting an open redirect vulnerability in the mobile photos
  feature of VK.com's m.vk.com site to redirect users to malicious phishing
  pages.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect in VK.com Mobile Photos Feature for Phishing Attacks

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect in VK.com's mobile site.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Malicious Link] --> B[Redirection to Phishing Site]
    B --> C[Phishing Attack Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[curl]] for testing

### Target Environment

- Web platform
- Access to m.vk.com (VK.com mobile site)
- No specific ports or services required beyond standard HTTP/HTTPS

### Initial Access Requirements

- Ability to craft and distribute URLs (e.g., via email or social engineering)
- No prior credentials needed; targets any VK.com user

## Detailed Attack Procedures

### Step 1: Craft and Distribute Malicious Redirect Link
procedure: [[procedures/Exploiting-Open-Redirect-in-VK-Mobile-Photos]]

**Objective**: Exploit the open redirect in the mobile photos feature to send victims to a phishing site, bypassing VK.com's domain trust.

**Instructions**: Identify the vulnerable endpoint in the mobile photos feature, typically involving a redirect parameter that lacks proper validation. Craft a URL like `https://m.vk.com/photos?redirect=https://malicious-phish-site.com`. Distribute this link to targets via phishing emails or messages, tricking them into clicking while appearing to link to legitimate VK content.

Use [[commands/curl-test-open-redirect]] to verify the redirect works:

```bash
curl -L -I "https://m.vk.com/photos?redirect=https://example-malicious.com" -A "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15"
```

Test in a mobile browser to confirm the redirect bypasses validation and lands on the external site.

**Expected Output**: HTTP response showing a 3xx redirect to the external domain, or browser navigation to the malicious site.

**Success Indicators**:
- Redirect occurs without error
- Victim is forwarded to the phishing page
- No VK.com validation blocks the external URL

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of open redirect without authentication
2. Potential for phishing attacks by mimicking trusted VK.com navigation
3. Medium impact due to user deception risks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
