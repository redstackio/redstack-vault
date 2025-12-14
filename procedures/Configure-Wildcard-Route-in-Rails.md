---
tags:
  - rails
  - route-configuration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/rails-generate-controller]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:12.386Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 5e801981-d8c6-494a-8597-d05c2a1c735c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Wildcard-Route-in-Rails

## Summary

This procedure sets up a wildcard route in a Ruby on Rails application, which is a prerequisite for exploiting the directory traversal vulnerability in ActionView::FileSystemResolver by allowing unmatched actions to resolve arbitrary paths.

## Description

In vulnerable Rails setups, defining a wildcard route like 'get "/help/(*action)", controller: 'help'' enables the view resolver to use Dir.glob on user-supplied paths, potentially traversing directories. This is typically done in a development or misconfigured production environment. The procedure involves generating a controller and editing routes.rb. Expected outcome is a functional route that doesn't restrict view paths, leading to potential information disclosure when exploited.

## Requirements

1. Ruby on Rails environment installed and running (e.g., Rails 4.x or vulnerable version)
2. Access to edit config/routes.rb and app/controllers
3. Rails server (e.g., via 'rails server')

## Defense

Defensive measures and detection strategies:

- Avoid wildcard routes; use explicit path matching
- Enable Rack::Protection::PathTraversal middleware (though bypassable)
- Monitor logs for suspicious route patterns and 200 responses to traversal paths

## Objectives

1. Establish a vulnerable route configuration for traversal exploitation
2. Create an empty controller to handle unmatched actions
3. Verify route activation without errors

## Instructions

### Step 1: Generate the Controller

**Context**: Create a basic HelpController to associate with the wildcard route.

**Command** ([[commands/rails-generate-controller]]):
```bash
rails generate controller Help
```

> This generates the controller files in app/controllers and app/views. Expected output: Files created, no errors.

### Step 2: Define the Wildcard Route

**Context**: Add the wildcard segment to routes.rb to capture arbitrary actions.

**Command** (Manual edit):
```ruby
# In config/routes.rb
get '/help/(*action)', to: 'help#index'
```

> Edit the file directly. Expected output: Route added; restart server to apply.

### Step 3: Empty the Controller Action

**Context**: Ensure the index action is empty to allow view resolution via Dir.glob.

**Command** (Manual edit):
```ruby
# In app/controllers/help_controller.rb
class HelpController < ApplicationController
  def index
    # Empty
  end
end
```

> Expected output: Controller ready; test with a normal request to /help/something returning 200.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/rails-generate-controller]]

## Tools Used


## Tags

- rails
- route-configuration
