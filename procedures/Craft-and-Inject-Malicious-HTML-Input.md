---
id: proc-uuid-2
tags:
  - xss
  - html-injection
type: procedure
tools:
  - '[[tools/Nokogiri]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.843Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Inject Malicious HTML Input

## Summary

This procedure involves creating a specially crafted HTML string that exploits parsing quirks in Nokogiri to nest a script tag inside a style element, injecting it into the sanitizer for processing.

## Description

The malicious input '<select<style/>W<xmp<script>alert(1)</script>' leverages self-closing tags and elements like <xmp> to confuse the parser. In JRuby, nekohtml treats this as nested content within style, preserving the script. In CRuby, similar fragments fail to scrub. This step assumes prior sanitizer configuration and targets Rails apps rendering user-controlled HTML.

## Requirements

1. Configured sanitizer from previous procedure
2. Ruby REPL or script environment
3. Understanding of HTML parsing behaviors

## Defense

Defensive measures and detection strategies:

- Input validation to block suspicious tag combinations
- Use stricter sanitizers like Loofah or custom rules
- WAF rules to detect nested script patterns

## Objectives

1. Generate input that evades tag stripping
2. Simulate user-submitted content
3. Prepare for output verification

## Instructions

### Step 1: Construct Malicious Fragment

**Context**: Build the HTML string exploiting the bypass, using elements that trigger improper CDATA/text handling.

**Command**:
```ruby
input = '<select<style/>W<xmp<script>alert(1)</script>'
```

> Assign the string to a variable. Expected output: The raw string. This sets up injection without execution yet.

### Step 2: Pass to Sanitizer

**Context**: Feed the input into the configured sanitizer instance.

**Command**:
```ruby
sanitizer = Rails::Html::SafeListSanitizer.new
sanitized = sanitizer.sanitize(input, tags: tags)
```

> Calls sanitize method. Defer printing to next procedure for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Nokogiri]]

## Tags

- [[xss]]
- [[injection]]
