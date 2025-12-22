---
tags:
  - xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/touch-malicious-filename]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.432Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 873bbc6e-b25d-465b-b494-8f14ab4e6ded
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-File-for-XSS-Injection

## Summary

This procedure creates a file with a specially crafted name containing an XSS payload, exploiting RDoc's lack of filename escaping to inject malicious JavaScript into generated HTML documentation.

## Description

In the context of Ruby projects using RDoc for documentation, attackers with file system access can name files to include HTML tags and JavaScript attributes. When RDoc processes these into HTML (e.g., via darkfish generator), the payload embeds unescaped, leading to stored XSS. This affects viewers of the docs, enabling session hijacking or data exfiltration. Prerequisites include a Ruby environment and write access to the project directory.

## Requirements

1. Linux shell access with Ruby/RDoc installed
2. Write permissions in the target project directory
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all filenames before HTML insertion in documentation tools
- Use content security policies (CSP) in generated HTML to block inline JS
- Monitor for unusual file names with script tags during code reviews or CI/CD

## Objectives

1. Create a file embedding an XSS payload in its name
2. Set up for RDoc processing to inject into output
3. Enable arbitrary JS execution on doc viewing

## Instructions

### Step 1: Craft and Create the File

**Context**: Use the touch command to create an empty file with a name that breaks out of HTML context and injects JS.

**Command** ([[commands/touch-malicious-filename]]):
```bash
touch ""><object src=1 onerror=\"javascript:alert(1);\">Controlling what is documented here"
```

> This creates a file named '"><object src=1 onerror="javascript:alert(1);">Controlling what is documented here', where the payload closes an HTML attribute and adds an onerror handler. Expected output: None; verify with ls.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- [[commands/touch-malicious-filename]]

## Tools Used

- None

## Tags

- [[xss]]
- [[injection]]
