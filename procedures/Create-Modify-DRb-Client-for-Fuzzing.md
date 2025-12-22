---
id: proc-drb-client-fuzz-001
tags:
  - fuzzing
  - client
  - drb
  - ruby
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:30.175Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Modify-DRb-Client-for-Fuzzing

## Summary

This procedure creates a standard DRb client from the official example and modifies it to perform basic fuzzing by sending malformed TCP payloads, preparing for a DoS attack on the server.

## Description

The client connects to the DRb server URI and invokes methods, but modifications introduce invalid data like string references ('eval') instead of integer object IDs during message crafting. This targets the deserialization in DRb's recv_request. Run on Linux with Ruby 2.7.1; requires server running. Outcome: A client ready to trigger crashes without immediate impact.

## Requirements

1. Ruby 2.7.1 on Linux
2. Network access to DRb server port
3. Basic knowledge of Ruby and DRb protocol

## Defense

Defensive measures and detection strategies:

- Implement client-side validation before sending requests
- Log anomalous client connections or payload sizes
- Use network intrusion detection for unusual TCP patterns to DRb ports

## Objectives

1. Establish client connection to DRb server
2. Modify client to inject malformed inputs
3. Test client without crashing server yet

## Instructions

### Step 1: Implement Basic Client Script

**Context**: Start with the official DRb client example to connect and call a method.

**Command** (Ruby script):
```ruby
require 'drb'

server = DRbObject.new_with_uri('druby://localhost:12345')
puts server.add(1, 2)  # Should output 3
```

> Save as `drb_client.rb`. Run with `ruby drb_client.rb` to verify basic functionality.

### Step 2: Modify for Fuzzing

**Context**: Alter the script to craft and send malformed payloads, simulating invalid object references in DRb messages.

**Command** (Modified Ruby script):
```ruby
require 'drb'

# Simulate fuzzing by overriding or injecting invalid ref in request
# For example, use DRb::ExtMaglevProtocol or manual TCP fuzz, but simply:
DRb.start_service
server = DRbObject.new_with_uri('druby://localhost:12345')
# Inject string 'eval' as ref in internal call simulation
# This will be triggered in deserialization
server.add(1, 'eval')  # Malformed to cause invalid ref
```

> Update `drb_client.rb` with fuzzing logic. This prepares payloads that lead to ObjectSpace._id2ref errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[fuzzing]]
- [[client]]
- [[drb]]
- [[ruby]]
