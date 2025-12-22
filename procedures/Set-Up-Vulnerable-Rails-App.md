---
id: proc-rails-setup-vuln
tags:
  - rails
  - setup
  - vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:27.897Z'
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
# Set-Up-Vulnerable-Rails-App

## Summary

This procedure sets up a Ruby on Rails application with a vulnerable endpoint that uses redirect_to on a user-supplied URL with allow_other_host: true, enabling testing of the header stripping vulnerability leading to XSS.

## Description

The vulnerability arises in Rails 7.0.4.3 when redirect_to processes URLs with control characters like %08, causing Rack to strip the Location header for RFC7230 compliance. This results in a fallback HTML redirect where the href is user-controlled. Setup involves creating a simple controller and route to expose this behavior. Prerequisites include Ruby and Rails installed; run in a development environment.

## Requirements

1. Ruby 3.x and Rails 7.0.4.3 installed
2. Puma or Rack-compatible server
3. Local network access to port 3000

## Defense

Defensive measures and detection strategies:

- Validate and sanitize redirect URLs to remove control characters (%01-%1F excluding %09, %0A)
- Disable allow_other_host: true or use a whitelist for redirects
- Monitor for anomalous 302 responses without Location headers

## Objectives

1. Deploy a testable vulnerable Rails endpoint
2. Verify the application responds to redirect requests
3. Prepare for payload injection

## Instructions

### Step 1: Create Vulnerable Controller

**Context**: Define a controller action that redirects using the user-supplied parameter.

In `app/controllers/application_controller.rb` or a new controller:

```ruby
def vuln
  redirect_to params[:redirect_url], allow_other_host: true
end
```

> This action pulls the redirect_url from params and allows external hosts, making it vulnerable.

### Step 2: Define Route

**Context**: Map the endpoint to the vulnerable action.

In `config/routes.rb`:

```ruby
get '/vuln', to: 'application#vuln'
```

> Routes the GET /vuln request to the vuln action.

### Step 3: Start the Server

**Context**: Launch the Rails server to host the application.

```bash
rails server -p 3000
```

> Starts Puma on port 3000; access http://localhost:3000/vuln to test.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rails
- setup
- vulnerability
