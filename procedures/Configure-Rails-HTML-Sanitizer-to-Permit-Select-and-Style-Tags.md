---
id: proc-uuid-1
tags:
  - xss
  - rails
  - sanitizer-config
type: procedure
tools:
  - '[[tools/rails-html-sanitizer]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/rails-sanitizer-configure-tags]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:25.854Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure Rails HTML Sanitizer to Permit Select and Style Tags

## Summary

This procedure sets up the Rails::Html::SafeListSanitizer to allow 'select' and 'style' tags, which is a prerequisite for exploiting the XSS bypass vulnerability due to inadequate nested element scrubbing in Nokogiri.

## Description

In Rails applications, HTML sanitization prevents XSS by restricting tags and attributes. However, permitting 'select' and 'style' tags exposes a flaw where parsing differences between JRuby (nekohtml backend) and CRuby in Nokogiri fail to properly handle nested scripts within style elements. This procedure configures the sanitizer with these tags, enabling the attack in test or vulnerable environments. Prerequisites include a Ruby/Rails setup with the rails-html-sanitizer gem installed.

## Requirements

1. Ruby environment (JRuby 9.3.3.0 or CRuby) with Rails and Nokogiri gems
2. Access to IRB or a Ruby script for execution
3. rails-html-sanitizer gem version prior to 1.4.3

## Defense

Defensive measures and detection strategies:

- Restrict allowed tags to exclude 'select' and 'style' in sanitizers
- Upgrade to rails-html-sanitizer >= 1.4.3 which patches the issue
- Monitor for anomalous HTML inputs containing nested tags in logs

## Objectives

1. Establish permissive sanitization rules to enable bypass
2. Prepare for injection of crafted HTML
3. Set stage for XSS execution

## Instructions

### Step 1: Define Allowed Tags

**Context**: Create an array of permitted tags to pass to the sanitizer, focusing on 'select' and 'style' to trigger the vulnerability.

**Command** ([[commands/rails-sanitizer-configure-tags]]):
```ruby
tags = %w(select style)
```

> This Ruby array defines the tags. Expected output: tags = ["select", "style"]. Success confirms configuration readiness.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/rails-sanitizer-configure-tags]]

## Tools Used

- [[tools/rails-html-sanitizer]]

## Tags

- [[xss]]
- [[rails]]
