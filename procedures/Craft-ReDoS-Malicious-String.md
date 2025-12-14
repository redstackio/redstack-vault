---
id: proc-redos-craft-string-001
tags:
  - redos
  - dos
  - payload-craft
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/ruby-test-underscore]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:36.405Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Craft-ReDoS-Malicious-String

## Summary

This procedure generates a malicious string tailored to exploit the ReDoS vulnerability in Active Support's underscore method by inducing catastrophic backtracking in the regex engine used for camelCase to snake_case conversion.

## Description

The underscore method in Active Support relies on a regular expression to split words in camelCase strings, such as /([A-Z]+)([A-Z][a-z])/ which can lead to exponential backtracking on inputs with ambiguous boundaries, like long sequences of lowercase letters followed by mixed case patterns. By crafting a string that maximizes matching attempts (e.g., thousands of 'a's ending in a backtracking trigger), the procedure causes the Ruby regex engine to consume excessive CPU and memory. This is particularly effective in web applications where user-supplied names or identifiers are processed. Prerequisites include basic Ruby knowledge and access to a test environment. Expected outcome is a payload that hangs processing for seconds to minutes.

## Requirements

1. Ruby environment with Active Support gem installed (vulnerable version < 6.1.7.1)
2. Text editor or scripting tool to build the string
3. Local Rails app or IRB for testing the payload

## Defense

Defensive measures and detection strategies:

- Upgrade to patched versions (6.1.7.1 or 7.0.4.1)
- Input validation: Limit string length and sanitize for regex-safe patterns
- Rate limiting on endpoints using inflector methods
- Monitor for high CPU spikes correlated with specific inputs

## Objectives

1. Create a string that triggers maximum backtracking paths in the underscore regex
2. Validate the payload locally to ensure DoS effect
3. Prepare payload for delivery in a web context

## Instructions

### Step 1: Generate Base Malicious Pattern

**Context**: Build a long repetitive string to force the regex to retry combinations exhaustively.

**Command** ([[commands/ruby-test-underscore]]):
```ruby
require 'active_support/inflector'
malicious = 'a' * 5000 + 'X' * 10 + 'aBc'
puts Time.now; result = malicious.underscore; puts Time.now - start_time
```

> This Ruby snippet crafts the string and times the underscore call. Expected output: Processing time exceeds 10 seconds, indicating backtracking.

### Step 2: Iterate and Optimize Payload

**Context**: Test variations to find the most effective string, adjusting length and patterns based on local timing.

**Command** ([[commands/ruby-test-underscore]]):
```ruby
require 'active_support/inflector'
start_time = Time.now
malicious = 'a' * 10000 + 'AbcDef'
result = malicious.underscore
elapsed = Time.now - start_time
puts "Elapsed: #{elapsed} seconds"
```

> Run in IRB or a script. Success if elapsed > 30 seconds; refine by increasing 'a' count or adding more case transitions.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[OS Exhaustion Flood]] Application or Service Exhaustion

### Sub-Techniques

- None

## Commands Used

- [[commands/ruby-test-underscore]]

## Tools Used

- None

## Tags

- redos
- payload-craft
- ruby
