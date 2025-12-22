---
tags:
  - http-request-smuggling
  - web-vulnerability
  - socket-poisoning
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/HTTP-Request-Smuggler-Plugin]]'
  - '[[tools/Burp-Suite-Turbo-Intruder]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/craft-http-smuggling-request]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Prepare-Burp-Suite-for-HTTP-Smuggling-Exploitation]]'
  - '[[procedures/Execute-Turbo-Intruder-for-Request-Smuggling]]'
  - '[[procedures/Load-and-Run-Turbo-Intruder-Script]]'
  - '[[procedures/Verify-Smuggling-Exploitation-Response]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of HTTP Request Smuggling vulnerability on a web endpoint to
  desynchronize request parsing and poison backend sockets, enabling arbitrary
  data prepending to subsequent requests.
skill_level: intermediate
impact_level: high
id: 98cd83e8-bb47-44fd-8499-9320f966bf25
created_at: '2025-12-13T09:01:17.639Z'
updated_at: '2025-12-13T09:01:17.639Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling to Poison TCP Sockets on Web Endpoint

Multi-stage attack chain demonstrating the exploitation of an HTTP Request Smuggling vulnerability on my.stripo.email, caused by inconsistent HTTP parsing between front-end and back-end servers. This allows desynchronization of request lengths, poisoning TCP/TLS sockets to prepend arbitrary data to subsequent requests, potentially bypassing security rules, accessing internal systems, poisoning web caches, and attacking active users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Tools] --> B[Send Crafted Request]
    B --> C[Load and Execute Script]
    C --> D[Verify Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/HTTP-Request-Smuggler-Plugin]]
- [[tools/Burp-Suite-Turbo-Intruder]]

### Target Environment

- Web platform
- Target endpoint: my.stripo.email /?aeRg=2056729135
- Network access to the target web server

### Initial Access Requirements

- No credentials required
- Direct network access to the public-facing web endpoint
- Prior knowledge of the vulnerable endpoint

## Detailed Attack Procedures

### Step 1: Prepare Burp Suite for Exploitation
procedure: [[procedures/Prepare-Burp-Suite-for-HTTP-Smuggling-Exploitation]]

**Objective**: Set up Burp Suite with the necessary plugin to identify and craft HTTP smuggling requests.

**Instructions**: Install and utilize the HTTP Request Smuggler plugin in Burp Suite to prepare for proof-of-concept exploitation.

**Expected Output**: Burp Suite configured with the plugin ready for crafting requests.

**Success Indicators**:
- Plugin installed successfully
- Burp Suite interface shows smuggling detection capabilities

### Step 2: Execute Turbo Intruder for Request Smuggling
procedure: [[procedures/Execute-Turbo-Intruder-for-Request-Smuggling]]

**Objective**: Send a crafted POST request to exploit the smuggling vulnerability by desynchronizing request lengths.

**Instructions**: Use Burp Suite Turbo Intruder to send the crafted request. Execute [[commands/craft-http-smuggling-request]] with the following details:

```http
POST /?aeRg=2056729135 HTTP/1.1
Host: my.stripo.email
Transfer-Encoding: chunked
Content-Length: keep-alive

f
ubvhq=x&e3t5b=x
0
```

**Expected Output**: Desynchronization in request length interpretation between servers.

**Success Indicators**:
- Request sent without immediate errors
- Backend socket poisoning initiated

### Step 3: Load and Run Turbo Intruder Script
procedure: [[procedures/Load-and-Run-Turbo-Intruder-Script]]

**Objective**: Automate the smuggling attack using a predefined script in Turbo Intruder.

**Instructions**: Load the script from poc.txt (or script.txt) into Burp Suite Turbo Intruder and execute it to automate the sending of smuggling requests.

**Expected Output**: Automated execution of multiple smuggling attempts.

**Success Indicators**:
- Script loads and runs without errors
- Multiple requests processed

### Step 4: Verify Smuggling Exploitation Response
procedure: [[procedures/Verify-Smuggling-Exploitation-Response]]

**Objective**: Observe the server response to confirm successful exploitation of the vulnerability.

**Instructions**: Monitor the responses in Burp Suite, looking for 301 redirect responses with Location header set to https://codeslayer137.000webhostapp.com/indeks.php, indicating successful smuggling.

**Expected Output**: 301 redirect response confirming socket poisoning.

**Success Indicators**:
- Receipt of unexpected redirect
- Evidence of arbitrary data prepending in responses

## Attack Chain Summary

### Key Achievements

1. Successful desynchronization of HTTP request parsing
2. Poisoning of backend TCP/TLS sockets
3. Potential for bypassing security and accessing internal systems

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
