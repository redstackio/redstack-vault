---
tags:
  - http-request-smuggling
  - web-vulnerability
  - cl-te-smuggling
type: attack_chain
tools:
  - '[[tools/Burp-Suite-Turbo-Intruder]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/send-smuggled-http-request]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-CL-TE-HTTP-Request-Smuggling-Using-Burp-Suite]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack chain exploiting CL.TE HTTP Request Smuggling on Helium's
  /api/sessions endpoint to achieve unauthorized access and potential further
  impacts like session hijacking.
skill_level: intermediate
impact_level: high
id: 34e88d01-5ed8-408c-9363-3ae42c546b7b
created_at: '2025-12-13T09:01:26.089Z'
updated_at: '2025-12-13T09:01:26.089Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling via CL.TE on Helium API for Unauthorized Access

Multi-stage attack chain demonstrating the exploitation of a CL.TE HTTP Request Smuggling vulnerability on the Helium console API. This allows smuggling of unauthorized requests, leading to a 200 OK response instead of 401 Unauthorized, with potential for session hijacking, privilege escalation, and other chained attacks.

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
    A[Prepare Tools] --> B[Send Smuggled Request]
    B --> C[Observe Response]
    C --> D[Confirm Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite-Turbo-Intruder]]

### Target Environment

- Web platform
- Helium console website (console.helium.com)
- Open access to /api/sessions endpoint

### Initial Access Requirements

- Network access to the target URL
- No credentials required for initial probing

## Detailed Attack Procedures

### Step 1: Prepare and Run Burp Suite Turbo Intruder
procedure: [[procedures/Exploit-CL-TE-HTTP-Request-Smuggling-Using-Burp-Suite]]

**Objective**: Set up and execute the tool to send a malformed POST request that exploits the CL.TE smuggling vulnerability.

**Instructions**: Launch Burp Suite Turbo Intruder and load the provided malformed POST request to /api/sessions. Use [[commands/send-smuggled-http-request]] to craft the request:

```http
POST /api/sessions HTTP/1.1
Host: console.helium.com
Content-Length: 109
Transfer-Encoding: chunked

0

GET / HTTP/1.1
Host: console.helium.com

```

**Expected Output**: The tool sends the smuggled request.

**Success Indicators**:
- Request successfully sent without errors
- Tool logs the transmission

### Step 2: Automate with Intruder Script
procedure: [[procedures/Exploit-CL-TE-HTTP-Request-Smuggling-Using-Burp-Suite]]

**Objective**: Use a script to automate the smuggling requests with an arbitrary word list.

**Instructions**: Attach the intruder.txt script to Burp Suite Turbo Intruder and select any word list containing characters. Execute to automate sending the smuggling requests.

**Expected Output**: Automated requests are sent, potentially varying based on the word list.

**Success Indicators**:
- Script runs without errors
- Multiple requests logged

### Step 3: Observe the API Response
procedure: [[procedures/Exploit-CL-TE-HTTP-Request-Smuggling-Using-Burp-Suite]]

**Objective**: Monitor the response from the /api/sessions endpoint to detect smuggling success.

**Instructions**: In Burp Suite, inspect the response to the POST request.

**Expected Output**: Receives 200 OK instead of 401 Unauthorized with error {"errors":{"error":["The email address or password you entered is not valid"]}}.

**Success Indicators**:
- 200 OK status code
- No authentication error

### Step 4: Confirm Vulnerability Exploitation
procedure: [[procedures/Exploit-CL-TE-HTTP-Request-Smuggling-Using-Burp-Suite]]

**Objective**: Validate that the smuggled GET request was processed, confirming the vulnerability.

**Instructions**: Review logs, screenshots, or recordings to ensure the smuggled GET / HTTP/1.1 request was interpreted differently by front-end and back-end servers.

**Expected Output**: Confirmation of inconsistent parsing leading to successful smuggling.

**Success Indicators**:
- Smuggled request confirmed in responses
- Potential for further impacts like cache poisoning observed

## Attack Chain Summary

### Key Achievements

1. Successful smuggling of unauthorized requests
2. Bypassed expected 401 Unauthorized response
3. Potential for chained attacks like session hijacking or XSS escalation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
