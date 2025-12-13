---
tags:
  - ssti
  - injection
  - web-vuln
  - rce
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-submit-registration-form]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Register-Account-with-SSTI-Payload]]'
  - '[[procedures/Verify-SSTI-Exploitation-via-Email]]'
  - '[[procedures/Escalate-SSTI-to-Malicious-Payloads]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  Exploits SSTI in the First Name field during Glovo user registration to
  achieve template evaluation and potential remote code execution via malicious
  payloads.
skill_level: intermediate
impact_level: high
id: d3994d39-f492-4ebb-82b5-e21748b6f20b
created_at: '2025-12-13T09:01:16.974Z'
updated_at: '2025-12-13T09:01:16.974Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Server-Side Template Injection in Glovo Sign-Up for Potential RCE

Multi-stage attack chain demonstrating exploitation of a Server Side Template Injection (SSTI) vulnerability in the Glovo registration process, leading to template evaluation in welcome emails and potential escalation to remote code execution or information disclosure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Registration] --> B[Verify Injection] --> C[Escalation to RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (web browser sufficient)

### Target Environment

- Web platform (Glovo website)
- Email service for receiving welcome emails

### Initial Access Requirements

- Access to Glovo website (https://www.glovoapp.com)
- Valid email address for registration

## Detailed Attack Procedures

### Step 1: Register Account with SSTI Payload
procedure: [[procedures/Register-Account-with-SSTI-Payload]]

**Objective**: Initiate registration and inject a basic SSTI payload into the First Name field to test for template evaluation.

**Instructions**: Navigate to the Glovo registration page and submit the form with the SSTI payload '{{7*7}}' in the First Name field. Use [[commands/curl-submit-registration-form]] to automate if desired:

```bash
curl -X POST https://www.glovoapp.com/kg/en/bishkek/register -d 'first_name={{7*7}}' -d 'email=your@email.com' -d 'password=yourpassword'
```

Provide valid values for other fields like email and password.

**Expected Output**: Successful account creation.

**Success Indicators**:
- Form submission succeeds without errors
- Account is registered

### Step 2: Verify SSTI Exploitation via Email
procedure: [[procedures/Verify-SSTI-Exploitation-via-Email]]

**Objective**: Check the welcome email to confirm that the SSTI payload was evaluated server-side.

**Instructions**: Monitor the registered email inbox for the welcome email from Glovo. Look for the subject line containing the evaluated result (e.g., '49, welcome to Glovo!').

**Expected Output**: Email subject reflects the computed value '49' instead of the raw payload.

**Success Indicators**:
- Email received with evaluated payload in subject
- Confirmation of SSTI vulnerability

### Step 3: Escalate SSTI to Malicious Payloads
procedure: [[procedures/Escalate-SSTI-to-Malicious-Payloads]]

**Objective**: Inject advanced payloads to achieve remote code execution, information disclosure, or further server attacks.

**Instructions**: Repeat the registration process with escalated payloads (e.g., for system command execution or variable dumping). Use [[commands/curl-submit-registration-form]] with modified payloads:

```bash
curl -X POST https://www.glovoapp.com/kg/en/bishkek/register -d 'first_name={{malicious_payload_here}}' -d 'email=your@email.com' -d 'password=yourpassword'
```

Monitor emails or server responses for evidence of execution.

**Expected Output**: Evidence of payload execution, such as disclosed sensitive data in emails.

**Success Indicators**:
- Payload executes successfully
- Sensitive information disclosed or RCE achieved

## Attack Chain Summary

### Key Achievements

1. Confirmed SSTI via template evaluation in emails
2. Potential for RCE and information disclosure
3. Demonstration of insecure template handling in web forms

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
