---
id: proc-uuid-1
name: Setup Vulnerable Rails App with Lograge
tags:
  - dos
  - rails
  - setup
type: procedure
tools:
  - '[[tools/rails]]'
  - '[[tools/lograge]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:36.522Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Vulnerable Rails App with Lograge

## Summary

This procedure creates a new Ruby on Rails application and integrates the lograge gem, which contributes to the vulnerability by not wrapping responses in Rack::BodyProxy, enabling mutation of the FAILSAFE_RESPONSE constant.

## Description

In a Rails environment, the ActionDispatch::ShowExceptions middleware uses a non-frozen FAILSAFE_RESPONSE constant. Middleware like lograge can mutate this without proper proxy wrapping, leading to recursive objects when exceptions are handled repeatedly. This setup simulates a production app vulnerable to DoS via stack overflow. Prerequisites include Ruby and Rails installed.

## Requirements

1. Ruby (version compatible with Rails, e.g., 2.7+)
2. Rails gem installed
3. Bundler for gem management
4. Local development environment

## Defense

Defensive measures and detection strategies:

- Freeze constants in middleware or patch Rails to use frozen responses
- Monitor for recursive object growth in heap dumps
- Use request rate limiting to prevent request floods

## Objectives

1. Establish a baseline vulnerable Rails app
2. Enable lograge to facilitate response mutation
3. Prepare for exception triggering

## Instructions

### Step 1: Create New Rails App

**Context**: Generate a fresh Rails application to serve as the target.

**Command** ([[rails generate]]):
```bash
rails new vulnerable_app
cd vulnerable_app
```

> This creates the app structure and navigates into the directory. Expected output: Basic Rails files generated.

### Step 2: Add Lograge Gem

**Context**: Integrate lograge into the Gemfile to customize logging and expose the mutation flaw.

**Command** ([[bundle add]]):
```bash
gem 'lograge'
```

> Edit Gemfile to include `gem 'lograge'`, then run `bundle install`. Expected output: Gem installed without errors.

### Step 3: Configure Lograge

**Context**: Enable lograge in the application configuration to activate its middleware behavior.

**Command** ([[edit config/application.rb]]):
```ruby
config.lograge.enabled = true
config.exceptions_app = self.routes
```

> Add these lines to config/application.rb. Expected output: Configuration applied; run `bundle exec rails console` to verify no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/rails]]
- [[tools/lograge]]

## Tags

- dos
- rails
- setup
