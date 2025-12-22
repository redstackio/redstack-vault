---
tags:
  - host-header-injection
  - web-vulnerability
  - http
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-host-header-injection-test]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Test-for-Host-Header-Injection]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Testing for host header injection vulnerability by modifying the Host header
  in HTTP requests to external domains, potentially leading to password reset
  poisoning or cache poisoning.
skill_level: beginner
impact_level: medium
id: dcc0e717-0e1e-4b21-b048-471eb468e858
created_at: '2025-12-13T09:01:17.479Z'
updated_at: '2025-12-13T09:01:17.479Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host Header Injection Testing via Spoofed Host in HTTP Requests

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Execution]
    B --> C[Objective]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Target OS/Platform: Web
- Required services/ports: HTTP/HTTPS
- Network access requirements: Direct access to the target web server

### Initial Access Requirements

- Credential requirements: None
- Network position: External
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Test Host Header Injection
procedure: [[procedures/Test-for-Host-Header-Injection]]

**Objective**: Send a crafted HTTP request with a modified Host header to check for injection vulnerabilities.

**Instructions**: Use [[commands/curl-host-header-injection-test]] to send the request with a spoofed Host header:

```bash
curl -H "Host: www.google.com" -H "User-Agent: Mozilla/5.0" -H "Accept: */*" https://target.com/contact/
```

**Expected Output**: Server responds with HTTP/1.1 421 Misdirected Request or similar indication of mishandling.

**Success Indicators**:
- Response code 421 or unexpected behavior
- Potential for further exploitation like password reset poisoning

## Attack Chain Summary

### Key Achievements

1. Identification of host header injection vulnerability
2. Potential access to internal hosts or cache poisoning
3. Demonstration of server misdirection handling

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: [TIMESTAMP]*
