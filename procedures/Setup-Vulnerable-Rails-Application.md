---
id: proc-rails-setup-001
tags:
  - rails
  - setup
  - vulnerable-app
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:38.008Z'
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
# Setup-Vulnerable-Rails-Application

## Summary

This procedure sets up a vulnerable Ruby on Rails application with a controller action that uses redirect_to on user-supplied input, enabling testing of the control character injection vulnerability leading to XSS.

## Description

In a Rails environment, create a controller with an action that redirects to a user-provided URL using allow_other_host: true. This exposes the redirect_to function to potential manipulation. The setup mimics a common open redirect pattern vulnerable in Rails 7.0.4.3. Prerequisites include Ruby and Rails installed; run in a development environment to avoid production impact. Expected outcome: A running app with /vuln endpoint that redirects normally for benign inputs.

## Requirements

1. Ruby 3.0+ and Rails 7.0.4.3 installed
2. Local development machine with bundler and Puma server
3. No network restrictions for localhost access on port 3000

## Defense

Defensive measures and detection strategies:

- Validate and sanitize redirect URLs to remove control characters before passing to redirect_to
- Use Rails' built-in URL validation or custom filters to block javascript: schemes
- Monitor server logs for suspicious redirect parameters containing %01-%1F characters

## Objectives

1. Establish a testable vulnerable endpoint for redirect exploitation
2. Verify normal redirect behavior before injection
3. Prepare environment for payload delivery

## Instructions

### Step 1: Create Rails Application and Controller

**Context**: Initialize a new Rails app and add the vulnerable controller action.

**Command** (Rails Generator):
```bash
rails new vuln_app --skip-bundle && cd vuln_app
```

> Creates a basic Rails app. Then edit app/controllers/application_controller.rb to add:
> ```ruby
def vuln
  redirect_to params[:redirect_url], allow_other_host: true
end
```
> And config/routes.rb: `get '/vuln' => 'application#vuln'`. Run `bundle install`.

### Step 2: Start the Server

**Context**: Launch the Puma development server to host the vulnerable endpoint.

**Command** (Rails Server):
```bash
rails server -p 3000
```

> Starts the server on localhost:3000. Test with a clean request: `curl -v http://localhost:3000/vuln?redirect_url=https://example.com` to confirm 302 with Location header.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None (uses Rails CLI commands)

## Tools Used

- None

## Tags

- rails
- setup
- vulnerable-app
