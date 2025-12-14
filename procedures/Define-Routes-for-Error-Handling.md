---
id: proc-uuid-2
name: Define Routes for Error Handling
tags:
  - dos
  - rails
  - routing
type: procedure
tools:
  - '[[tools/rails]]'
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
updated_at: '2025-12-14T17:26:36.520Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Define Routes for Error Handling

## Summary

This procedure configures Rails routes to handle errors, directing 404s and other exceptions to a custom controller, which invokes the vulnerable ShowExceptions middleware.

## Description

Routes in Rails determine how requests are processed. By setting up a root route and a catch-all for 404s, malformed requests will trigger exception handling, mutating the shared FAILSAFE_RESPONSE across requests. This is key to building the recursive proxy chain.

## Requirements

1. Existing Rails app directory
2. Access to config/routes.rb
3. Basic Rails knowledge

## Defense

Defensive measures and detection strategies:

- Implement custom exception apps that avoid shared constants
- Log route mismatches for anomaly detection
- Use WAF to block malformed paths

## Objectives

1. Route normal traffic to index
2. Direct errors to errors controller
3. Enable exception flow for exploitation

## Instructions

### Step 1: Edit Routes File

**Context**: Define the root route and error handling routes in config/routes.rb.

**Command** ([[edit routes.rb]]):
```ruby
root to: 'site#index'
get 'errors/not_found'
match '/404', to: 'errors#not_found', via: :all
```

> Add these lines to config/routes.rb. Expected output: Routes syntax valid; `rails routes` shows new entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/rails]]

## Tags

- dos
- rails
- routing
