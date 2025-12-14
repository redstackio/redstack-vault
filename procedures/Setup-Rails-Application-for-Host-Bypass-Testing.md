---
id: uuid-setup-rails
tags:
  - rails-setup
  - host-authorization
  - testing
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Ruby
  - Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.632Z'
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
# Setup-Rails-Application-for-Host-Bypass-Testing

## Summary

This procedure sets up a local Ruby on Rails application with a redirect endpoint protected by Host Authorization middleware, simulating a vulnerable environment to test open redirect bypasses via X-Forwarded-Host manipulation.

## Description

The setup involves creating a TestsController with an index action that performs a redirect to the root path ('/'), while configuring Rails to allow only specific hosts. This middleware, part of Action Pack, is vulnerable because it does not downcase the X-Forwarded-Host header, leading to nil values for mixed-case inputs and skipping validation. Prerequisites include Ruby and Rails installed; the target is a development server on port 3000.

## Requirements

1. Ruby (version compatible with Rails, e.g., 2.7+) and Rails (version with vulnerable Action Pack, e.g., pre-patch 6.1.4.6)
2. Local development environment with bundler for gem management
3. Access to run Rails server on localhost:3000

## Defense

Defensive measures and detection strategies:

- Patch Rails to version 6.1.4.6 or later where downcase is applied to X-Forwarded-Host
- Monitor proxy logs for anomalous X-Forwarded-Host headers with mixed case
- Implement additional redirect validation beyond host authorization

## Objectives

1. Establish a testable Rails app with host restrictions
2. Enable reproduction of the open redirect vulnerability
3. Prepare for header manipulation exploits

## Instructions

### Step 1: Create Rails Application and Controller

**Context**: Initialize a new Rails app and add a controller that triggers a redirect, extending ActiveSupport::Concern if needed for custom behavior.

**Command** (Manual setup - no direct command):

Create `app/controllers/tests_controller.rb`:
```ruby
class TestsController < ApplicationController
  def index
    redirect_to '/'
  end
end
```

Add route in `config/routes.rb`:
```ruby
get '/tests', to: 'tests#index'
```

> This sets up the /tests endpoint to redirect to '/', which will use the host from the request.

### Step 2: Configure Host Authorization

**Context**: Enable middleware and set allowed hosts to restrict redirects.

**Command** (Manual config):

In `config/application.rb` or initializer:
```ruby
config.host_authorization = { exclude: ->(request) { request.path == '/tests' } } # Optional exclude for testing
Rails.application.config.hosts = %w(.localhost .example.com)
```

> Configures middleware to match against allowed hosts; vulnerable versions fail on case mismatches.

### Step 3: Start Rails Server

**Context**: Launch the development server to host the vulnerable app.

**Command** (rails server):
```bash
rails server -p 3000
```

> Server runs on http://localhost:3000; verify by accessing /tests normally (should redirect to allowed host).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- rails-setup
- host-authorization
- testing
