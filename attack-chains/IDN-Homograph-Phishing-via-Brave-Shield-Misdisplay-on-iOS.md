---
tags:
  - phishing
  - idn-homograph
  - browser-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - iOS
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Visit-Malicious-Homograph-Domain]]'
  - '[[procedures/Open-Brave-Shield-Panel]]'
  - '[[procedures/Observe-Domain-Misdisplay]]'
step_count: 3
techniques:
  - '[[Phishing]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:41.785Z'
description: >-
  Demonstrates a phishing attack exploiting the Brave Shield panel's failure to
  display punycode domains correctly, deceiving users into trusting spoofed
  sites.
skill_level: low
impact_level: medium
id: 416c065c-093b-460e-b999-a3971b66fba1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[T1566.002]]'
---
# IDN Homograph Phishing via Brave Shield Misdisplay on iOS

Multi-stage attack chain demonstrating a phishing workflow that exploits the Brave browser's Shield panel on iOS to spoof legitimate domains using IDN homograph attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Visit Malicious URL] --> B[Open Shield Panel]
    B --> C[Observe Deception]
    C --> D[Phishing Success]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Brave Browser for iOS (vulnerable version)

### Target Environment

- iOS platform
- Brave Browser app
- No specific services or ports required; operates via browser navigation

### Initial Access Requirements

- User access to Brave iOS app
- Ability to enter or click a malicious URL (e.g., via email, message, or direct input)
- No prior credentials or network position needed

## Detailed Attack Procedures

### Step 1: Visit Malicious Homograph Domain
procedure: [[procedures/Visit-Malicious-Homograph-Domain]]

**Objective**: Direct the user to a punycode-encoded domain that visually mimics a legitimate site like apple.com to initiate the spoofing.

**Instructions**: In the Brave iOS app, navigate to the malicious URL https://www.xn--80ak6aa92e.com/. This domain uses Internationalized Domain Names (IDN) to appear as 'apple.com' in Unicode rendering, but it is encoded in punycode (xn-- prefix).

**Expected Output**: The browser loads the spoofed site, displaying it visually as the legitimate domain in the address bar (which correctly shows punycode), but the site's content may attempt to phish credentials.

**Success Indicators**:
- Page loads without errors
- Address bar shows the punycode URL, but visual rendering deceives the eye

### Step 2: Open Brave Shield Panel
procedure: [[procedures/Open-Brave-Shield-Panel]]

**Objective**: Access the Brave Shield interface to trigger the vulnerability in domain display.

**Instructions**: While on the malicious site, tap the Shield icon in the address bar of the Brave iOS app to open the panel. This panel is intended to show site security details.

**Expected Output**: The Shield panel opens, but due to the lack of IDN handling, it prepares to display incorrect information.

**Success Indicators**:
- Shield panel appears in the UI
- No immediate alerts or blocks from Brave

### Step 3: Observe Domain Misdisplay
procedure: [[procedures/Observe-Domain-Misdisplay]]

**Objective**: Confirm the deception by viewing the incorrectly displayed domain in the Shield panel, leading to user trust in the phishing site.

**Instructions**: Examine the domain field in the opened Brave Shield panel. The panel will show 'apple.com' instead of the actual punycode domain.

**Expected Output**: The panel incorrectly renders the domain as the legitimate one (e.g., 'apple.com'), convincing the user the site is safe and encouraging interaction like entering credentials.

**Success Indicators**:
- Domain shown as spoofed legitimate name
- User proceeds with phishing actions (e.g., login)

## Attack Chain Summary

### Key Achievements

1. Successful spoofing of a high-value domain like apple.com using IDN homograph.
2. Exploitation of Brave Shield's display flaw to bypass user suspicion.
3. Facilitation of phishing attacks by building false trust in the malicious site.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Phishing]] Phishing
- [[T1566.002]] Spearphishing Link

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
