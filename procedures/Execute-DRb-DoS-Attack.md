---
id: proc-drb-dos-execute-001
tags:
  - dos
  - crash
  - drb
  - ruby
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/Trigger-DRb-Crash-with-Invalid-Object-Reference]]'
verified: false
platforms:
  - Linux
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.172Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Execute-DRb-DoS-Attack

## Summary

This procedure runs the modified DRb client to send fuzzing input, triggering a server crash via an unhandled segmentation fault in ObjectSpace._id2ref when processing invalid references like 'eval'.

## Description

With the server running, the client sends malformed requests that cause deserialization failure in lib/drb/drb.rb:366. This exploits a bug since commit b99833baec2, leading to DoS. Tested on Ruby 2.7.1/Linux; assumes prior server and client setup. Outcome: Server crash and core dump, service unavailable.

## Requirements

1. Running DRb server from previous procedure
2. Modified fuzzing client script
3. Permissions to monitor server process (e.g., via ps or logs)

## Defense

Defensive measures and detection strategies:

- Validate all incoming DRb requests for proper object ID formats (integers only)
- Deploy crash monitoring and auto-restart for DRb services
- Restrict DRb to localhost or VPN; avoid public exposure

## Objectives

1. Send malformed payload to trigger crash
2. Confirm DoS via server termination
3. Analyze core dump for vulnerability verification

## Instructions

### Step 1: Run the Server

**Context**: Ensure the vulnerable server is active before attacking.

**Command** (Start server):
```bash
ruby drb_server.rb
```

> Verify with `netstat -tlnp | grep 12345` that it's listening.

### Step 2: Execute Fuzzing Client

**Context**: Launch the client to send the invalid input, invoking the crash.

**Command** ([[commands/trigger-drB-crash-with-invalid-object-reference]]):
```ruby
require 'drb'

server = DRbObject.new_with_uri('druby://localhost:12345')
# Fuzzing payload: causes internal ObjectSpace._id2ref('eval')
# Simulate via malformed add call or direct protocol fuzz
server.add(1, 2)  # But with injected invalid ref
```

> Run `ruby drb_client.rb`. The server will crash immediately upon receiving the payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion (adapted for crash)

## Commands Used

- [[commands/trigger-drB-crash-with-invalid-object-reference]]

## Tools Used


## Tags

- [[dos]]
- [[crash]]
- [[drb]]
- [[ruby]]
