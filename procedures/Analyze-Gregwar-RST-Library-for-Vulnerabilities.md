---
tags:
  - library-analysis
  - lfi
  - path-traversal
type: procedure
tools:
  - '[[tools/Gregwar-RST]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:17.110Z'
sub_techniques: []
id: cd2e9738-2f47-4372-9a80-81c11265e66d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Analyze-Gregwar-RST-Library-for-Vulnerabilities

## Summary

This procedure examines the Gregwar/RST library's implementation to identify flaws in the include directive, confirming its susceptibility to path traversal attacks that enable LFI.

## Description

The Gregwar/RST parser, used by Airship CMS for reStructuredText processing, implements an 'include' directive at Parser.php line 762 without path validation. This allows attackers to specify arbitrary files using traversal sequences. In a vulnerability assessment scenario, this analysis targets PHP libraries in web applications, leading to the discovery of information disclosure risks when parsing untrusted content.

## Requirements

1. Access to Gregwar/RST GitHub repository
2. PHP development environment for testing
3. Understanding of RST directives and PHP file inclusion mechanics

## Defense

Defensive measures and detection strategies:

- Fork and patch the library to add path whitelisting or disable include
- Scan dependencies with tools like OWASP Dependency-Check for known vulns
- Log all include attempts and alert on traversal patterns (e.g., '../')

## Objectives

1. Verify lack of path sanitization in include directive
2. Test traversal payloads for arbitrary file access
3. Assess impact on dependent applications like Airship CMS

## Instructions

### Step 1: Review Parser Source

**Context**: Examine the core parsing logic to locate the include handler.

Clone the repo and inspect Parser.php:

```bash
git clone https://github.com/Gregwar/RST.git
cd RST
cat lib/Gregwar/RST/Parser.php | grep -A5 -B5 "include"
```

> Focus on line 762; expected output shows file inclusion via include($path) without checks. Confirms vulnerability.

### Step 2: Test Directive Behavior

**Context**: Manually verify if traversal works by creating a test RST and parsing it locally.

Use a simple PHP test script to parse sample RST with traversal.

> Expected: Successful inclusion of non-standard paths, proving LFI potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Gregwar-RST]]

## Tags

- library-analysis
- lfi
- path-traversal
