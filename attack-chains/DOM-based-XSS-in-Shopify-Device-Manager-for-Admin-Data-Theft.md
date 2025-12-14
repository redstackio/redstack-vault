---
tags:
  - xss
  - dom-based-xss
  - shopify
  - admin-dashboard
  - data-theft
  - javascript-execution
type: attack_chain
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Inject-XSS-Payloads-into-User-Profiles]]'
  - '[[procedures/Trigger-XSS-via-Admin-Dashboard-Search]]'
  - '[[procedures/Capture-XSS-Executions-with-XSS-Hunter]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
description: >-
  Multi-stage attack exploiting DOM-based XSS in Shopify's admin dashboard to
  inject payloads into user profiles and trigger them during searches, enabling
  theft of sensitive admin-viewable user data.
skill_level: intermediate
impact_level: high
id: 8ef92a3d-12fe-4cca-8327-7c92cdcf611a
created_at: '2025-12-13T23:52:55.566Z'
updated_at: '2025-12-13T23:52:55.566Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-based XSS in Shopify Device Manager for Admin Data Theft

Multi-stage attack chain demonstrating exploitation of a DOM-based Cross-site Scripting (XSS) vulnerability in Shopify's Device Manager admin dashboard to steal sensitive user data visible to administrators.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Payload Injection] --> B[Trigger Execution]
    B --> C[Data Capture]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/XSS-Hunter]]

### Target Environment

- Web platform with Shopify integration
- Access to create user accounts and stores
- Admin dashboard at https://devicemanager.shopifycloud.com/admin

### Initial Access Requirements

- Ability to register test accounts (e.g., via email aliases like 'samudra+lp@wearehackerone.com')
- No prior admin credentials needed; relies on admin interaction with search functionality

## Detailed Attack Procedures

### Step 1: Payload Injection
procedure: [[procedures/Inject-XSS-Payloads-into-User-Profiles]]

**Objective**: Embed malicious JavaScript payloads into user account names or profiles to prepare for DOM-based XSS execution.

**Instructions**: Create test accounts and stores with XSS payloads in profile fields. Use an advanced payload like the XSS Hunter script for tracking, or a simple test payload like `<img src=x onerror=prompt(document.domain)>`.

**Expected Output**: Successful account/store creation with payloads stored in unsanitized fields.

**Success Indicators**:
- Account registered without payload sanitization errors
- Profile data saved including the injected script

### Step 2: Trigger Execution
procedure: [[procedures/Trigger-XSS-via-Admin-Dashboard-Search]]

**Objective**: Cause the payload to execute by simulating or inducing admin searches that load the vulnerable user data into the DOM.

**Instructions**: Access the admin dashboard at https://devicemanager.shopifycloud.com/admin and perform searches for the injected profiles. The search functionality renders user data without proper encoding, triggering the DOM-based XSS.

**Expected Output**: JavaScript execution in the admin's browser context, potentially alerting or exfiltrating data.

**Success Indicators**:
- Payload triggers during search (e.g., prompt box appears for simple payload)
- No server-side errors; execution occurs client-side

### Step 3: Data Capture
procedure: [[procedures/Capture-XSS-Executions-with-XSS-Hunter]]

**Objective**: Monitor and collect data from multiple XSS triggers across admin sessions.

**Instructions**: Use XSS Hunter to receive notifications of executions, capturing details like IP addresses, stolen user data (emails, locations, store names, IDs, usernames), and observing ongoing triggers from various sources.

**Expected Output**: Email alerts with exfiltrated data from up to 25 accounts per dashboard page across multiple pages.

**Success Indicators**:
- Notifications received showing data theft
- Triggers continue from different IP addresses over hours

## Attack Chain Summary

### Key Achievements

1. Injected persistent XSS payloads into user profiles without detection
2. Triggered arbitrary JavaScript execution in authenticated admin context via search functionality
3. Stole sensitive data from numerous user accounts, demonstrating high confidentiality impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01*
