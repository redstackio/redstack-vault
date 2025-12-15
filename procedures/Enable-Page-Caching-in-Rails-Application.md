---
tags:
  - page-caching
  - rails-config
type: procedure
tools:
  - '[[tools/rails]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/rails-dev-cache]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.469Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9712f5ba-7197-4f15-a0c1-f51f8d5f57d1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable-Page-Caching-in-Rails-Application

## Summary

This procedure activates the page caching feature in a Rails development environment and configures the BooksController to cache the show action, setting the stage for traversal exploitation.

## Description

Page caching in Rails stores rendered pages as static HTML files in the public directory. The actionpack-page_caching gem handles this but fails to sanitize paths, allowing traversal. This step modifies config/environments/development.rb and the controller. Prerequisites include the setup from the previous procedure. Expected outcome: Caching ready for verification.

## Requirements

1. Rails app with actionpack-page_caching gem installed
2. Access to edit app/controllers/books_controller.rb
3. Development environment

## Defense

Defensive measures and detection strategies:

- Disable page caching in production or use secure alternatives like Russian Doll caching
- Implement URL path whitelisting
- Log caching operations for anomaly detection

## Objectives

1. Enable caching in dev config
2. Cache specific actions to expose vulnerability

## Instructions

### Step 1: Enable Caching in Development

**Context**: Activate the feature globally for dev.

**Command** ([[commands/rails-dev-cache]]):
```bash
rails dev:cache
```

> Updates config/environments/development.rb to include config.action_controller.page_cache_directory = Rails.root.join('public'). Expected: Caching enabled message.

### Step 2: Configure Controller for Caching

**Context**: Add caches_page to BooksController show action.

Edit app/controllers/books_controller.rb:
```ruby
class BooksController < ApplicationController
  before_action :set_book, only: [:show, :edit, :update, :destroy]

  caches_page :show
end
```

> Adds caching directive. Expected: No errors on save.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/rails-dev-cache]]

## Tools Used

- [[tools/rails]]

## Tags

- page-caching
- rails-config
