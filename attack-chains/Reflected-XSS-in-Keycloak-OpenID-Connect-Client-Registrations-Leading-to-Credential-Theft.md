---
id: ac-keycloak-xss-2021
tags:
  - xss
  - reflected-xss
  - keycloak
  - openid-connect
  - credential-theft
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-Keycloak-Client-Registrations]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.382Z'
description: >-
  A single-stage attack exploiting a reflected XSS vulnerability in Keycloak's
  OpenID Connect client registrations endpoint to execute arbitrary JavaScript
  and steal authentication credentials.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS in Keycloak OpenID Connect Client Registrations Leading to Credential Theft

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via XSS Exploit] --> B[Execution and Credential Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Keycloak versions 8.0 and prior
- Web platform with OpenID Connect services
- Accessible /auth/realms/master/clients-registrations/openid-connect endpoint
- Network access to the target host on port 80/443

### Initial Access Requirements

- No prior credentials required
- Direct network access to the Keycloak server
- No authentication needed for the vulnerable endpoint

## Detailed Attack Procedures

### Step 1: Exploit Reflected XSS
procedure: [[procedures/Exploit-Reflected-XSS-in-Keycloak-Client-Registrations]]

**Objective**: Send a malicious POST request to the OpenID Connect client registrations endpoint to trigger reflected XSS, executing arbitrary JavaScript in the victim's browser and stealing cookie-based authentication credentials.

**Instructions**: Prepare the target URL and craft the payload. Use [[commands/keycloak-xss-poc-post]] to send the request:

```bash
curl -X POST 'http://target.com/auth/realms/master/clients-registrations/openid-connect' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -d '{"<img onerror=confirm(\'xss_poc_unexpectedbufferc0n\') src/>":1}'
```

Validate the response for payload reflection by checking if the JavaScript executes (e.g., alert dialog appears in a browser context).

**Expected Output**: HTTP response reflecting the payload in the body, triggering JavaScript execution such as a confirm dialog displaying 'xss_poc_unexpectedbufferc0n'. In a real attack, this could exfiltrate cookies via a script sending data to an attacker-controlled server.

**Success Indicators**:
- Payload reflected in response without sanitization
- JavaScript execution confirmed (e.g., alert or network request to attacker server)
- Potential credential theft if executed in authenticated session

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of CVE-2021-20323 in Keycloak
2. Arbitrary JavaScript execution leading to session hijacking
3. Potential for further attacks like account compromise or defacement

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
