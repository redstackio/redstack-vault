---
tags:
  - rails
  - sanitize
  - svg
  - config
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: dcf95831-00c1-40eb-8531-1a4464f5e151
created_at: '2025-12-13T23:52:34.189Z'
updated_at: '2025-12-13T23:52:34.189Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Rails-ActionView-Sanitizer-to-Allow-SVG-and-Use-Tags

## Summary

This procedure configures the Rails ActionView sanitize helper, powered by Loofah, to allow 'svg' and 'use' tags, enabling the subsequent injection of malicious SVG payloads for XSS bypass.

## Description

In a Ruby on Rails application using Loofah gem versions >=2.1.0 <2.19.1, the default sanitizer strips dangerous tags like 'svg'. By explicitly allowing 'svg' and 'use', attackers or misconfigured developers create a vector for embedding base64 data URIs that Loofah fails to properly sanitize, leading to XSS. This is typically done in development or via template modifications, assuming access to the codebase.

## Requirements

1. Access to Rails configuration files (e.g., config/application.rb) or ERB templates
2. Ruby on Rails environment with Loofah gem installed
3. Rails server running for testing

## Defense

Defensive measures and detection strategies:

- Upgrade Loofah to >=2.19.1 to fix the sanitization issue
- Avoid allowing 'svg' or 'use' tags in sanitizer config; use safer alternatives like 'img' for images
- Implement Content Security Policy (CSP) to block inline scripts and data URIs
- Monitor for unusual config changes in Rails initializers via version control audits

## Objectives

1. Enable SVG tag processing without stripping
2. Prepare the application for payload injection
3. Create a misconfiguration that mimics legitimate SVG use for images

## Instructions

### Step 1: Global Configuration

**Context**: Set allowed tags application-wide to permit SVG elements.

**Command** (Rails Config):
```ruby
# In config/application.rb or config/initializers/sanitizer.rb
Rails.application.config.action_view.sanitized_allowed_tags = ['svg', 'use']
```

> This updates the default sanitizer. Restart the Rails server and verify by rendering a test SVG; it should not be stripped.

### Step 2: Inline Template Configuration

**Context**: Allow tags specifically in an ERB template for targeted injection points.

**Command** (ERB Inline):
```erb
# In index.html.erb or similar
<%= sanitize @user_input, tags: %w(svg use) %>
```

> This applies to a specific sanitize call. Test by passing a simple <svg> tag; it renders intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rails]]
- [[sanitize]]
- [[svg]]
