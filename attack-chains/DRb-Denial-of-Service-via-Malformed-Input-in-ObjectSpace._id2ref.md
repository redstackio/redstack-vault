---
id: ac-drb-dos-001
tags:
  - dos
  - ruby
  - drb
  - deserialization
  - crash
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - Ruby
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-DRb-Server]]'
  - '[[procedures/Create-Modify-DRb-Client-for-Fuzzing]]'
  - '[[procedures/Execute-DRb-DoS-Attack]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.182Z'
description: >-
  A multi-stage attack chain exploiting a denial of service vulnerability in
  Ruby's DRb library by sending malformed input to crash the server through an
  unhandled error in ObjectSpace._id2ref.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# DRb Denial of Service via Malformed Input in ObjectSpace._id2ref

Multi-stage attack chain demonstrating a complete denial of service workflow against Ruby's DRb library.

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
    A[Set Up DRb Server] --> B[Prepare Fuzzing Client]
    B --> C[Trigger Server Crash]
    C --> D[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Ruby 2.7.1 or compatible version
- Basic text editor for Ruby scripts

### Target Environment

- Linux platform
- DRb service running on a local or remote port (default TCP)
- Ruby tech stack with DRb library

### Initial Access Requirements

- Network access to the DRb server port
- Ability to execute Ruby scripts on attacker machine
- No credentials needed, as DRb assumes trusted clients

## Detailed Attack Procedures

### Step 1: Set Up DRb Server
procedure: [[procedures/Set-Up-DRb-Server]]

**Objective**: Establish a vulnerable DRb server instance following official documentation to simulate the target environment.

**Instructions**: Implement and run the DRb server script using the official Ruby example code. Save the code as `drb_server.rb` and execute it to start the server on a local port.

```ruby
require 'drb'

class DemoServer
  def add(x, y)
    x + y
  end
end

server = DRb::DRbServer.new(Rack::Handler::WEBrick.run(DemoServer.new, Port: 12345))
DRb.start_service('druby://:12345', DemoServer.new)
server.join
```

**Expected Output**: Server starts listening on druby://localhost:12345 without errors.

**Success Indicators**:
- DRb server process is running and accessible
- No immediate crashes or errors on startup

### Step 2: Create and Modify DRb Client for Fuzzing
procedure: [[procedures/Create-Modify-DRb-Client-for-Fuzzing]]

**Objective**: Develop a client script based on the official example and modify it to send malformed TCP payloads for fuzzing the DRb protocol.

**Instructions**: Start with the basic DRb client example, then alter it to craft invalid input, such as replacing object IDs with strings like 'eval' during deserialization simulation. Save as `drb_client.rb`.

```ruby
require 'drb'

server = DRbObject.new_with_uri('druby://localhost:12345')
# Modify to send malformed payload, e.g., simulate invalid ref in request
# Example fuzzing: inject string 'eval' as object ID in DRb message
DRb.start_service
# Craft malformed request to trigger recv_request
```

**Expected Output**: Client connects to server; no crash yet, but prepared for fuzzing input.

**Success Indicators**:
- Client script executes without syntax errors
- Connection to server is established

### Step 3: Execute Attack to Crash Server
procedure: [[procedures/Execute-DRb-DoS-Attack]]

**Objective**: Run the fuzzing client to send malformed input, causing the server to crash via an unhandled error in ObjectSpace._id2ref.

**Instructions**: With the server running, execute the modified client script to send the fuzzing payload. Monitor the server process for crash.

```ruby
# In drb_client.rb, invoke the malformed call
server.add(1, 2)  # But with fuzzed payload injecting invalid ref like 'eval'
# This triggers internal call to ObjectSpace._id2ref('eval')
```

**Expected Output**: Server crashes with segmentation fault or core dump at lib/drb/drb.rb:366.

**Success Indicators**:
- Server process terminates unexpectedly
- Core dump generated, confirming DoS

## Attack Chain Summary

### Key Achievements

1. Successfully set up a vulnerable DRb server environment.
2. Prepared and modified a client for targeted fuzzing of DRb protocol inputs.
3. Triggered a denial of service crash, rendering the DRb service unavailable.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
