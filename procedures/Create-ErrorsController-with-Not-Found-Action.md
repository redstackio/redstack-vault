---
id: proc-uuid-3
name: Create ErrorsController with Not Found Action
tags:
  - dos
  - rails
  - controller
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
updated_at: '2025-12-14T17:26:36.516Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create ErrorsController with Not Found Action

## Summary

This procedure implements an ErrorsController in Rails to handle 404 errors, rendering a response that engages the ShowExceptions middleware and potential mutation.

## Description

The controller's not_found action renders a 404 status, which under exceptions_app configuration, routes through ShowExceptions. This exposes the non-frozen FAILSAFE_RESPONSE to middleware mutation when requests fail routing.

## Requirements

1. Rails app with routes configured
2. app/controllers directory access
3. Ruby syntax knowledge

## Defense

Defensive measures and detection strategies:

- Override default exception rendering to use frozen bodies
- Monitor controller invocation rates
- Patch Rails to fix constant freezing

## Objectives

1. Handle 404 exceptions explicitly
2. Trigger middleware chain for mutation
3. Simulate production error pages

## Instructions

### Step 1: Create Controller File

**Context**: Generate the ErrorsController with a simple not_found action.

**Command** ([[rails generate controller]]):
```ruby
class ErrorsController < ApplicationController
  def not_found
    render status: 404
  end
end
```

> Create app/controllers/errors_controller.rb with this content. Expected output: File saved; no syntax errors on load.

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
- controller
