---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - reflected-xss
  - web
  - browser-exploitation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-VK-Mobile-Confirmation]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:53.347Z'
description: >-
  A reflected XSS attack exploiting a vulnerability in the VK.com mobile
  confirmation page on the 0.vk.com subdomain, affecting old Internet Explorer
  versions via MTS and Beeline mobile operators, allowing arbitrary JavaScript
  execution in the victim's browser.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reflected XSS on VK.com Mobile Confirmation Page for Script Execution

Multi-stage attack chain demonstrating a complete attack workflow targeting a reflected XSS vulnerability in the VK.com mobile confirmation page.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Malicious Link] --> B[Victim Accesses Page]
    B --> C[Script Execution]
    C --> D[Session Hijack or Phishing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for payload testing

### Target Environment

- Web platform
- Specific to 0.vk.com subdomain
- Mobile version accessible via MTS or Beeline operators
- Old versions of Internet Explorer

### Initial Access Requirements

- Ability to send links to victims (e.g., via email or messaging)
- No prior credentials needed
- Victim must use affected browser and operator

## Detailed Attack Procedures

### Step 1: Craft and Deliver Malicious Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-VK-Mobile-Confirmation]]

**Objective**: Inject and reflect a malicious JavaScript payload via a crafted URL to the confirmation page, executing arbitrary code in the victim's browser upon access.

**Instructions**: Construct a URL with a reflected parameter payload, such as appending a script tag to a query parameter that lacks sanitization. For example, target the confirmation page URL like `https://0.vk.com/confirm?param=<script>alert('XSS')</script>`. Send this link to the victim via social engineering. When the victim clicks it on an affected old IE browser via MTS/Beeline, the payload reflects and executes.

To test locally, use browser dev tools to simulate:

```javascript
// In console, simulate payload injection
document.write('<script>alert("XSS Triggered")</script>');
```

Validate by checking if the alert pops or network requests are made.

**Expected Output**: JavaScript execution, such as an alert box or data exfiltration to attacker-controlled server.

**Success Indicators**:
- Payload reflects without encoding
- Script executes in victim's browser
- Potential session cookies captured or phishing form displayed

## Attack Chain Summary

### Key Achievements

1. Successful payload reflection on vulnerable confirmation page
2. Arbitrary JavaScript execution in old IE browsers
3. Potential for session hijacking or phishing attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
