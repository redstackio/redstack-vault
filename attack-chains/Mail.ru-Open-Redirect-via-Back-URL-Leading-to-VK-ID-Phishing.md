---
tags:
  - open-redirect
  - phishing
  - mail.ru
  - vk-id
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Mail-ru-Open-Redirect-via-Back-URL]]'
  - '[[procedures/Phishing-via-VK-ID-Integrated-Login]]'
step_count: 2
techniques:
  - '[[Phishing]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:55:06.054Z'
description: >-
  A multi-stage attack exploiting an open redirect vulnerability in Mail.ru's
  login flow with VK ID integration to facilitate phishing and potential
  credential theft.
skill_level: intermediate
impact_level: high
id: e235991e-c039-408b-89ee-94935b26a19a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Drive-by Compromise]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: Mail.ru Open Redirect via Back URL Leading to VK ID Phishing
type: attack_chain
description: "A multi-stage attack exploiting an open redirect vulnerability in Mail.ru's login flow with VK ID integration to facilitate phishing and potential credential theft."
verified: false
submitted: false
step_count: 2
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Exploit-Mail-ru-Open-Redirect-via-Back-URL]], [[procedures/Phishing-via-VK-ID-Integrated-Login]]
techniques: [[Phishing]], [[Drive-by Compromise]]
tactics: [[Initial Access]]
tags: open-redirect, phishing, mail.ru, vk-id
platforms: Web
tools: []
---

# Mail.ru Open Redirect via Back URL Leading to VK ID Phishing

Multi-stage attack chain demonstrating a complete attack workflow exploiting Mail.ru's login redirection and VK ID integration for phishing.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Craft Phishing Link] --> B[Execution: Trigger Redirect and Login Mimic]
    B --> C[Objective: Credential Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for URL manipulation
- Phishing site hosting (e.g., attacker-controlled domain)

### Target Environment

- Web platform
- Mail.ru services with VK ID authentication
- No specific ports required; standard HTTPS (443)

### Initial Access Requirements

- Public access to Mail.ru login page
- No prior credentials needed; targets unsuspecting users
- Attacker must control a malicious redirect target

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Exploit-Mail-ru-Open-Redirect-via-Back-URL]]

**Objective**: Craft a malicious URL that exploits the open redirect in Mail.ru's 'back_url' parameter to redirect users post-login to an attacker-controlled site.

**Instructions**: Construct the phishing link by appending a malicious 'back_url' to the Mail.ru garage endpoint. For example, replace the legitimate back_url with an attacker site:

```url
https://account.mail.ru/user/garage?back_url=https://attacker.com/phishing
```
Distribute this link via email or social engineering to lure the victim into clicking and logging in.

**Expected Output**: Victim is prompted to log in to Mail.ru, and upon successful authentication, redirected to the attacker's phishing page.

**Success Indicators**:
- Victim accesses the crafted URL and initiates login
- Post-login redirect occurs to the malicious domain

### Step 2: Execution
procedure: [[procedures/Phishing-via-VK-ID-Integrated-Login]]

**Objective**: Mimic the legitimate Mail.ru login interface with VK ID elements to capture user credentials during the authentication flow.

**Instructions**: On the attacker-controlled site (reached via redirect), replicate the Mail.ru login page, embedding VK ID social authentication elements such as user photos sourced from VK's external domains. Use similar styling and VK API calls to make it indistinguishable. Capture entered credentials (email, password, VK token if applicable) and submit to attacker's backend.

**Expected Output**: Victim enters credentials on the fake page, which are exfiltrated to the attacker, potentially enabling account takeover.

**Success Indicators**:
- Victim submits credentials on the phishing page
- Attacker receives stolen credentials or session data

## Attack Chain Summary

### Key Achievements

1. Successful open redirect post-authentication to bypass trust in Mail.ru domain
2. Effective phishing mimicry using VK ID integration for credential theft
3. Potential for full account compromise on Mail.ru or linked VK accounts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Phishing]] Phishing
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
