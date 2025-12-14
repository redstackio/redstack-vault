---
tags:
  - configuration
  - vulnerable
  - xss
  - rails
type: procedure
tools:
  - '[[tools/rails]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.931Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 05b6e7bd-86fc-4ebe-93e4-7266779af54e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Configure-Vulnerable-Rails-Application

## Summary

This procedure configures routes, controller, and view in a Rails app to expose XSS via the translate method, using untrusted params for missing keys and unescaped defaults.

## Description

Edit routes.rb to define endpoints, implement ArticlesController with t calls that inject params or defaults marked html_safe, and create a view that renders the output. This setup allows testing the vulnerability where missing keys ending in '_html' or defaults lead to unescaped HTML/JS execution when viewed in browser.

## Requirements

1. Existing Rails app directory
2. Text editor (e.g., vim, VS Code)
3. Knowledge of Rails routing and ERB templating

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to t method with html_escape
- Use Rails 7.1+ patches or upgrade to fixed versions
- Static analysis with tools like brakeman to detect unsafe t usage

## Objectives

1. Define vulnerable routes
2. Implement controller with unsafe translate
3. Render output in view for execution

## Instructions

### Step 1: Configure Routes

**Context**: Add GET routes for missing_key and default actions in ArticlesController.

**Instructions**: Open config/routes.rb and append:

```ruby
get "/articles/missing_key", to: "articles#missing_key"
get "/articles/default", to: "articles#default"
```

> Saves routes. Expected: No syntax errors on rails routes.

### Step 2: Implement Vulnerable Controller

**Context**: Add methods using t with params and default to trigger html_safe without escaping.

**Instructions**: Edit app/controllers/articles_controller.rb:

```ruby
class ArticlesController < ApplicationController
  def missing_key
    @message = t(params[:text])
    render :show
  end

  def default
    @message = t("message_html", default: "<script>alert(location)</script>")
    render :show
  end
end
```

> Controller updated. Expected: Methods defined without errors.

### Step 3: Create View Template

**Context**: Display @message to execute injected content.

**Instructions**: Create/edit app/views/articles/show.html.erb:

```erb
<h1><%= @message %></h1>
<p>Comparison: <%= t('safe.message_html', default: 'Safe in view') %></p>
```

> View renders @message as html_safe. Expected: ERB syntax valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/rails]]

## Tags

- configuration
- vulnerable
- xss
- rails
