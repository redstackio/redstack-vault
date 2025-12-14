---
id: proc-drb-setup-001
tags:
  - setup
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
updated_at: '2025-12-14T17:26:30.178Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-DRb-Server

## Summary

This procedure sets up a basic DRb server using Ruby's official example code, creating a vulnerable instance that can be targeted for denial of service testing in a controlled environment.

## Description

DRb (Distributed Ruby) is a library for remote method invocation in Ruby applications. This procedure follows the documentation to implement a simple server that exposes methods over TCP. The server is vulnerable to malformed inputs due to lack of validation in deserialization, but this step focuses on deployment. It requires Ruby 2.7.1 on Linux and assumes local network access. Expected outcome is a running server ready for client interaction and subsequent exploitation.

## Requirements

1. Ruby 2.7.1 installed on Linux
2. Access to write and execute Ruby scripts
3. Open TCP port for DRb (e.g., 12345)

## Defense

Defensive measures and detection strategies:

- Run DRb servers behind firewalls, restricting access to trusted networks only
- Monitor for unexpected server crashes or core dumps in Ruby processes
- Use input validation wrappers around DRb endpoints

## Objectives

1. Deploy a functional DRb server instance
2. Verify server accessibility for remote calls
3. Prepare environment for DoS testing

## Instructions

### Step 1: Implement Server Script

**Context**: Create the server code based on Ruby documentation to define a simple service class and start the DRb server.

**Command** (Ruby script execution):
```ruby
require 'drb'

class DemoServer
  def add(x, y)
    x + y
  end
end

DRb.start_service('druby://:12345', DemoServer.new)
DRb.thread.join
```

> Save this as `drb_server.rb`. This starts the server on port 12345, exposing the `add` method remotely.

### Step 2: Run the Server

**Context**: Execute the script to launch the server process.

**Command** (Run Ruby script):
```bash
ruby drb_server.rb
```

> The server will output confirmation of starting the DRb service and remain running until interrupted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[drb]]
- [[ruby]]
