---
id: proc-webrick-server-setup
tags:
  - webrick
  - server-setup
  - digest-auth
type: procedure
tools:
  - '[[tools/Ruby]]'
  - '[[tools/WEBrick]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Ruby
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:31:19.601Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Configure Vulnerable WEBrick Server with Digest Auth

## Summary

This procedure sets up a local WEBrick HTTP server using Ruby with Digest authentication enabled, reproducing the ReDoS vulnerability for testing purposes.

## Description

The procedure configures WEBrick on port 8000 with a simple endpoint protected by DigestAuth, using a hardcoded user database. The target environment is a local Ruby installation (e.g., 2.5.5). Expected outcome is a running server vulnerable to ReDoS in auth parsing.

## Requirements

1. Ruby 2.5.5 or compatible version installed
2. WEBrick library (standard in Ruby)
3. Local port 8000 available

## Defense

Defensive measures and detection strategies:

- Upgrade to patched Ruby/WEBrick versions (post-2019 fixes)
- Use alternative auth mechanisms like Basic with TLS
- Rate-limit authentication attempts

## Objectives

1. Start server with DigestAuth
2. Verify basic functionality
3. Ensure vulnerability is present

## Instructions

### Step 1: Write Server Script

**Context**: Create a Ruby script to initialize WEBrick with auth.

Use the following code:

```ruby
require 'webrick'
require 'webrick/httpauth/digestauth'

server = WEBrick::HTTPServer.new(:Port => 8000)
server.realm = 'DigestAuth example realm'
server.users = {'user' => WEBrick::HTTPAuth::DigestAuth.make_passwd(server.realm, 'user', 'password')}

proc = Proc.new do |req, res|
  res.body = 'Protected content.'
end

WEBrick::HTTPAuth::DigestAuth.define_auth_proc(server, 'Secure Area', proc) do |user, pass|
  user == 'user' && pass == 'password'
end

server.start
```

### Step 2: Run the Server

**Context**: Execute the script to start listening.

Save as server.rb and run `ruby server.rb`.

> Server outputs 'WEBrick 1.4.2' and listens on localhost:8000.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Ruby]]
- [[tools/WEBrick]]

## Tags

- webrick
- server-setup
