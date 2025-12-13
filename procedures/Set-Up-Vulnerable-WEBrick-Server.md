---
tags:
  - webrick
  - ruby
  - server-setup
type: procedure
tools:
  - '[[tools/WEBrick]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/webrick-server-setup]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ddff133e-6ffa-4f35-8d51-e0c5eab43955
created_at: '2025-12-13T09:01:22.216Z'
updated_at: '2025-12-13T09:01:22.216Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set Up Vulnerable WEBrick Server

## Summary

This procedure deploys a vulnerable WEBrick HTTP server in Ruby with sample endpoints to demonstrate HTTP Request Smuggling exploitation.

## Description

WEBrick is set up on port 8080 with '/' returning 'hello world' and '/flag' returning 'flag is 123456'. The vulnerability lies in loose parsing of Transfer-Encoding headers, allowing smuggling attacks.

## Requirements

1. Ruby installed with WEBrick library
2. Localhost access on port 8080
3. No prior services on port 8080

## Defense

Defensive measures and detection strategies:

- Update WEBrick to patch loose regex
- Implement strict header validation

## Objectives

1. Create backend server for proxy testing
2. Expose vulnerable endpoints
3. Verify server responsiveness

## Instructions

### Step 1: Create Ruby Script

**Context**: Write the script to mount endpoints.

Execute [[commands/webrick-server-setup]]:

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

### Step 2: Run the Server

**Context**: Start the WEBrick server.

Run the script to listen on port 8080.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/webrick-server-setup]]

## Tools Used

- [[tools/WEBrick]]

## Tags

- [[tools/WEBrick]]
- [[ruby]]
