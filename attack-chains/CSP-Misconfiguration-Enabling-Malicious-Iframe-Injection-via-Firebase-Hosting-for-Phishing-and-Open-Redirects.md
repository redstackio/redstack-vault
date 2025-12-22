---
tags:
  - csp-misconfig
  - iframe-injection
  - open-redirect
  - phishing
  - firebase
type: attack_chain
tools:
  - '[[tools/NodeJS]]'
  - '[[tools/Firebase-CLI]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Email-Template-in-Stripo-Editor]]'
  - '[[procedures/Deploy-Malicious-Page-to-Firebase-Hosting]]'
  - '[[procedures/Inject-Iframe-Payload-into-Template]]'
  - '[[procedures/Trigger-Exploit-via-Template-Preview]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:24:31.382Z'
description: >-
  Exploits a permissive CSP in Stripo's email template editor to inject iframes
  from attacker-controlled Firebase subdomains, enabling JavaScript execution
  for redirects, popups, and phishing during template preview or viewing.
skill_level: intermediate
impact_level: high
id: 3e6fb133-7528-4487-98c8-024e74d0ec92
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[T1566.001]]'
---
# CSP Misconfiguration Enabling Malicious Iframe Injection via Firebase Hosting for Phishing and Open Redirects

Multi-stage attack chain exploiting a Content-Security-Policy (CSP) misconfiguration in Stripo's email template editor. The CSP's frame-src directive allows iframes from any *.firebaseapp.com subdomain, enabling attackers to host malicious JavaScript on Firebase and inject it via iframes into user templates. This leads to phishing, open redirects, popups, and disruption when templates are previewed or viewed on viewstripo.email.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Template] --> B[Deploy Malicious Firebase Page]
    B --> C[Inject Iframe]
    C --> D[Preview and Trigger]
    D --> E[Phishing/Redirect/Popup]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/NodeJS]]
- [[tools/Firebase-CLI]]

### Target Environment

- Web platform
- Access to Stripo email template editor at https://my.stripo.email/cabinet/#/template-editor/...
- Firebase account for hosting
- No special ports or services beyond web access

### Initial Access Requirements

- Valid Stripo account (user-level access sufficient)
- Internet access for Firebase deployment
- No prior credentials needed beyond free Firebase signup

## Detailed Attack Procedures

### Step 1: Create New Template
procedure: [[procedures/Create-Malicious-Email-Template-in-Stripo-Editor]]

**Objective**: Gain access to the HTML editor to prepare for payload insertion.

**Instructions**: Log in to Stripo and navigate to the template editor to start a new HTML-based template.

**Expected Output**: An open HTML editor interface ready for content addition.

**Success Indicators**:
- Template editor loads successfully
- HTML input field is editable

### Step 2: Deploy Malicious Page
procedure: [[procedures/Deploy-Malicious-Page-to-Firebase-Hosting]]

**Objective**: Host attacker-controlled JavaScript on a Firebase subdomain to execute redirects and popups.

**Instructions**: Set up a Firebase project, create an index.html with malicious script, and deploy using [[commands/firebase-init]] and [[commands/firebase-deploy]]:

```bash
firebase init hosting
firebase deploy
```

**Expected Output**: Deployed site at a subdomain like hackerone-jm.firebaseapp.com.

**Success Indicators**:
- Site accessible via browser
- JavaScript executes (e.g., alert shows)

### Step 3: Inject Iframe
procedure: [[procedures/Inject-Iframe-Payload-into-Template]]

**Objective**: Embed the malicious Firebase page via iframe, leveraging the permissive CSP.

**Instructions**: Insert the iframe tag directly into the HTML content.

**Expected Output**: Iframe tag added without sanitization errors.

**Success Indicators**:
- HTML saves without validation blocks
- No CSP errors on save

### Step 4: Trigger Exploit
procedure: [[procedures/Trigger-Exploit-via-Template-Preview]]

**Objective**: Execute the malicious script through preview or viewing, causing redirects and popups.

**Instructions**: Preview the template in the editor or access via viewstripo.email URL.

**Expected Output**: Alert popup, top-level redirect, and new window opens.

**Success Indicators**:
- JavaScript executes in iframe
- Redirect to attacker site occurs
- Popup spawns

## Attack Chain Summary

### Key Achievements

1. Bypassed CSP to load external malicious content
2. Achieved JavaScript execution for phishing vectors
3. Enabled broad impact on template viewers including intra-org phishing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]
- [[T1566.001]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
