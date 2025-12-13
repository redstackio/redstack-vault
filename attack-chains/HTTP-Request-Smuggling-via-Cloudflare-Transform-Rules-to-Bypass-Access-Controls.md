---
tags:
  - http-smuggling
  - cloudflare
  - request-injection
  - bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-smuggling-request]]'
platforms:
  - Cloud
  - Web
complexity: medium
procedures:
  - >-
    [[procedures/Inject-Newlines-in-Cloudflare-Transform-Rules-Using-Concat-Function]]
  - '[[procedures/Perform-HTTP-Request-Smuggling-with-Crafted-POST-Request]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits HTTP request smuggling in Cloudflare Transform Rules by injecting
  newlines via hexadecimal escapes to bypass security and access internal
  servers.
skill_level: intermediate
impact_level: high
id: c8a71969-2fc7-4cb7-820f-71106d75df9d
created_at: '2025-12-13T09:01:26.068Z'
updated_at: '2025-12-13T09:01:26.068Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling via Cloudflare Transform Rules to Bypass Access Controls

## Overview

This attack chain demonstrates HTTP request smuggling in Cloudflare's Transform Rules, exploiting the concat() function's lack of output sanitation for hexadecimal escape sequences. By injecting newlines into request headers, attackers can modify headers like Transfer-Encoding and smuggle secondary requests to bypass Cloudflare Access and reach internal origin servers.

## Attack Flow Visualization

```mermaid
graph LR
    A[Inject Newlines in Headers] --> B[Send Smuggled Request]
    B --> C[Bypass Access and Reach Internal Servers]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (Cloudflare dashboard access required for rule creation)

### Target Environment

- Platform: Cloud (Cloudflare)
- Services: Cloudflare Access, internal origin servers
- Tech Stack: Ruleset Engine, Transform Rules

### Initial Access Requirements

- Access to Cloudflare dashboard for rule creation
- Ability to send HTTP requests to the affected domain

## Detailed Attack Procedures

### Step 1: Create Dynamic Header Rewrite Rule
procedure: [[procedures/Inject-Newlines-in-Cloudflare-Transform-Rules-Using-Concat-Function]]

**Objective**: Set up a Transform Rule in Cloudflare to inject newlines and modify headers using the concat() function.

**Instructions**: Log into the Cloudflare dashboard and navigate to the Transform Rules section. Create a new dynamic header rewrite rule using the concat() function to inject a newline and set Transfer-Encoding to chunked:

```plaintext
concat("-", "\x0d\x0aTransfer-Encoding: chunked")
```

Apply this rule to the target domain's requests.

**Expected Output**: The rule is successfully created and active, allowing newline injection in headers.

**Success Indicators**:
- Rule creation confirmed in dashboard
- Headers can be modified with injected newlines

### Step 2: Send Crafted Smuggling Request
procedure: [[procedures/Perform-HTTP-Request-Smuggling-with-Crafted-POST-Request]]

**Objective**: Send a POST request with a crafted body to smuggle a secondary GET request to an internal host.

**Instructions**: Use [[commands/curl-http-smuggling-request]] to send the request to the affected endpoint. The POST body should be:

```plaintext
0\r\n\r\nGET / HTTP/1.1\r\nHost: internal.example.com\r\n\r\n
```

Execute the command:

```bash
curl -X POST https://target.example.com/ -H "Content-Type: text/plain" --data "0\r\n\r\nGET / HTTP/1.1\r\nHost: internal.example.com\r\n\r\n"
```

**Expected Output**: The smuggled request reaches the internal server, returning content from internal.example.com.

**Success Indicators**:
- Response includes data from internal server
- Bypasses Cloudflare Access controls

## Attack Chain Summary

### Key Achievements

1. Injected newlines into HTTP headers via Cloudflare rules
2. Smuggled secondary request to access internal content
3. Bypassed security products like Cloudflare Access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
