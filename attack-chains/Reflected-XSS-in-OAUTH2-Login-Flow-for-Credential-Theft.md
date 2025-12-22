---
tags:
  - xss
  - reflected-xss
  - oauth2
  - credential-theft
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/craft-xss-payload-url]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Craft-Malicious-XSS-URL]]'
  - '[[procedures/Distribute-Malicious-URL]]'
  - '[[procedures/Execute-XSS-Payload]]'
step_count: 3
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
description: >-
  Exploitation of reflected XSS in OAUTH2 login flow to execute arbitrary
  JavaScript and steal credentials
skill_level: intermediate
impact_level: high
id: 1f2a2bc9-0d3f-477e-a450-3103b79cb84c
created_at: '2025-12-14T00:11:25.386Z'
updated_at: '2025-12-14T00:11:25.386Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Reflected XSS in OAUTH2 Login Flow for Credential Theft

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in an OAUTH2 login flow, allowing arbitrary JavaScript execution in the victim's browser for credential theft or account hijacking.

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
    A[Initial Access via Malicious URL] --> B[Payload Distribution] --> C[Execution and Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None specific, standard web browser and URL manipulation tools

### Target Environment

- Web-based application with OAUTH2 login flow
- Vulnerable to reflected XSS in URL parameters
- Victim's browser access

### Initial Access Requirements

- Ability to craft and send URLs to victims
- No prior credentials needed
- Network access to the target application

## Detailed Attack Procedures

### Step 1: Craft Malicious URL
procedure: [[procedures/Craft-Malicious-XSS-URL]]

**Objective**: Create a URL containing an XSS payload that reflects back in the OAUTH2 login flow.

**Instructions**: Construct the malicious URL by appending an XSS payload to a vulnerable parameter in the OAUTH2 login endpoint. Use [[commands/craft-xss-payload-url]] to encode and prepare the payload:

```bash
echo 'https://vulnerable-app.com/oauth2/login?param=<script>alert("XSS"); stealCredentials();</script>' > malicious_url.txt
```

**Expected Output**: A crafted URL ready for distribution.

**Success Indicators**:
- URL contains properly encoded XSS payload
- Payload is not sanitized when reflected

### Step 2: Distribute Malicious URL
procedure: [[procedures/Distribute-Malicious-URL]]

**Objective**: Send the crafted URL to potential victims via messaging or social engineering.

**Instructions**: Share the malicious URL through messages, emails, or links. Ensure the victim is tricked into clicking it while attempting to log in via OAUTH2.

No specific command needed; manual distribution.

**Expected Output**: Victim receives and interacts with the URL.

**Success Indicators**:
- URL delivered to victim
- Victim clicks the link

### Step 3: Execute XSS Payload
procedure: [[procedures/Execute-XSS-Payload]]

**Objective**: Trigger the reflected XSS to execute JavaScript and steal credentials.

**Instructions**: Upon victim interaction, the payload executes in their browser context. The JavaScript can capture credentials or session data and exfiltrate it to an attacker-controlled server.

Monitor for exfiltrated data.

**Expected Output**: Stolen credentials or session hijacking.

**Success Indicators**:
- JavaScript executes successfully
- Data exfiltrated to attacker

## Attack Chain Summary

### Key Achievements

1. Successful crafting of XSS payload in URL
2. Distribution leading to victim interaction
3. Execution of arbitrary JS for credential theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

*Last updated: 2023-10-01*
