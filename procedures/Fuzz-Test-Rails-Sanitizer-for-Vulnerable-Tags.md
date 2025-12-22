---
id: proc-fuzz-rails-sanitizer
tags:
  - xss
  - fuzzing
  - rails
type: procedure
tools:
  - '[[tools/rails-html-sanitizer]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:25.786Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fuzz-Test-Rails-Sanitizer-for-Vulnerable-Tags

## Summary

This procedure uses fuzz testing to probe Rails::Html::SafeListSanitizer for bypasses in HTML sanitization, specifically identifying that 'svg' + 'style' and 'math' + 'style' tag combinations fail to strip malicious nested content like script tags or event handlers.

## Description

In a Rails application, user input is often sanitized using SafeListSanitizer to prevent XSS. Fuzzing involves generating random or systematic HTML inputs with various tag permutations to check if dangerous elements persist after sanitization. This targets versions like 1.4.3 where the sanitizer inadequately handles style tags nested in svg or math, allowing JavaScript injection. Prerequisites include a Ruby environment with the gem installed.

## Requirements

1. Ruby environment with rails-html-sanitizer gem installed
2. Fuzzing tool or script to generate HTML payloads (e.g., custom Ruby script)
3. Access to IRB or a test harness for sanitization calls

## Defense

Defensive measures and detection strategies:

- Avoid allowing 'style' tags with 'svg' or 'math'; use stricter allowlists
- Upgrade to patched versions of rails-html-sanitizer (post-1.4.3)
- Implement content security policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript execution in web logs

## Objectives

1. Discover tag combinations that bypass sanitization
2. Confirm persistence of malicious payloads
3. Validate potential for XSS exploitation

## Instructions

### Step 1: Set Up Fuzzing Environment

**Context**: Prepare the Ruby environment to load and test the sanitizer repeatedly.

**Command** ([[commands/load-rails-html-sanitizer-gem]]):
```ruby
require 'rails-html-sanitizer'
```

> Loads the gem, enabling access to SafeListSanitizer. Expected output: false (indicating successful require).

### Step 2: Generate and Test Payloads

**Context**: Create fuzz inputs combining tags like svg, math, style with nested script or img onerror, then sanitize and inspect output.

No specific command; use a loop in IRB or script:
```ruby
sanitizer = Rails::Html::SafeListSanitizer.new
payloads = ["<svg><style><script>alert(1)</script></style></svg>", "<math><style><img src=x onerror=alert(1)></style></math>"]
payloads.each do |p|
  result = sanitizer.sanitize(p, tags: ["svg", "style"]).to_s
  puts result if result.include?("alert")
end
```

> Iterates payloads; success if output retains alert(1) without stripping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/load-rails-html-sanitizer-gem]]

## Tools Used

- [[tools/rails-html-sanitizer]]

## Tags

- [[xss]]
- [[fuzzing]]
