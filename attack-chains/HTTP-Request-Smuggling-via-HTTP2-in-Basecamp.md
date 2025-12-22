---
tags:
  - http-request-smuggling
  - http2
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-http2-request]]'
  - '[[commands/burp-repeater-test]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Identify-HTTP-Request-Smuggling-Vulnerability]]'
  - '[[procedures/Exploit-HTTP-Request-Smuggling-via-HTTP2]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of HTTP Request Smuggling vulnerability in Basecamp using HTTP/2
  to potentially bypass security controls or hijack requests
skill_level: intermediate
impact_level: high
id: 1a491681-66ad-4fb0-a721-7edff6edfc12
created_at: '2025-12-13T09:01:26.207Z'
updated_at: '2025-12-13T09:01:26.207Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling via HTTP/2 in Basecamp

## Overview

This attack chain demonstrates the exploitation of an HTTP Request Smuggling vulnerability in the Basecamp application via HTTP/2 protocol handling. Discovered and reported on May 28, 2021, this critical vulnerability allows attackers to smuggle requests, potentially bypassing security controls, poisoning caches, or hijacking legitimate requests. The chain covers identification and exploitation steps, leading to unauthorized actions within the application.

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Recon] --> B[Vulnerability Identification]
    B --> C[Exploitation]
    C --> D[Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/cURL]]

### Target Environment

- Web-based application supporting HTTP/2
- Target platform: Web
- Required services/ports: HTTP/HTTPS (ports 80/443)
- Network access requirements: Direct access to the Basecamp application endpoint

### Initial Access Requirements

- No credentials required for initial testing
- Network position: External attacker with internet access
- Prior access needed: None, public-facing application

## Detailed Attack Procedures

### Step 1: Identify HTTP Request Smuggling Vulnerability
procedure: [[procedures/Identify-HTTP-Request-Smuggling-Vulnerability]]

**Objective**: Scan and confirm the presence of HTTP Request Smuggling vulnerability in the target's HTTP/2 handling.

**Instructions**: Begin by sending a test HTTP/2 request using [[commands/curl-http2-request]] to check for protocol support:

```bash
curl --http2 -v https://basecamp-target.com/
```

Next, use Burp Suite to craft and send smuggling test requests. Configure Burp to use HTTP/2 and send a request with mismatched Content-Length or chunked encoding to detect desynchronization.

**Expected Output**: Verbose output showing HTTP/2 negotiation success and any desynchronization indicators, such as unexpected responses or errors.

**Success Indicators**:
- HTTP/2 protocol confirmed
- Evidence of request desynchronization detected

### Step 2: Exploit HTTP Request Smuggling via HTTP/2
procedure: [[procedures/Exploit-HTTP-Request-Smuggling-via-HTTP2]]

**Objective**: Smuggle a malicious request to bypass security or hijack sessions.

**Instructions**: Craft a smuggled request using [[commands/burp-repeater-test]] in Burp Suite Repeater: Set up two requests where the first has a smuggling payload (e.g., invalid chunk size) followed by a second malicious request. Send to the Basecamp endpoint.

```bash
# Example smuggling payload in Burp (manual crafting required)
POST / HTTP/2
Host: basecamp-target.com
Content-Length: 0

GET /admin HTTP/1.1
Host: basecamp-target.com
```

Monitor the response for signs of successful smuggling, such as access to restricted resources.

**Expected Output**: Response indicating the smuggled request was processed, potentially returning sensitive data or allowing unauthorized actions.

**Success Indicators**:
- Smuggled request executed
- Security controls bypassed or cache poisoned

## Attack Chain Summary

### Key Achievements

1. Confirmed vulnerability in HTTP/2 handling
2. Successful request smuggling leading to potential hijacking
3. Demonstration of critical impact on Basecamp application

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
