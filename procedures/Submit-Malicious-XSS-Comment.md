---
id: proc-submit-xss-comment
tags:
  - xss
  - injection
  - wordpress
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.335Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Submit-Malicious-XSS-Comment

## Summary

This procedure submits a comment containing a crafted XSS payload wrapped in SyntaxHighlighter code tags, exploiting the plugin's loose regex to create an auto-linked javascript: URL that persists as stored XSS.

## Description

The SyntaxHighlighter plugin on WordPress.com processes [code] blocks in comments, applying a regex like /\w+:\/\/[\w-./?%&=:@;#\]* /g to auto-link URLs. The permissive \w+ allows 'javascript:', enabling attackers to inject payloads like javascript://%0dalert(document.cookie), which renders as a clickable link. Once posted, it tricks victims into executing JS in the site's context.

## Requirements

1. Access to the comments form on a vulnerable post
2. Web browser for submission
3. No special privileges if comments are open

## Defense

Defensive measures and detection strategies:

- Sanitize comment inputs to block javascript: protocols
- Use strict regex in plugins to whitelist safe URLs (e.g., http/https only)
- Implement Content Security Policy (CSP) to restrict inline JS execution

## Objectives

1. Inject and store the XSS payload in a comment
2. Have it processed and rendered as a malicious link
3. Enable persistence for victim interaction

## Instructions

### Step 1: Craft and Post Payload

**Context**: Enter the payload in the comment form to exploit the auto-linking feature.

No command required; use the browser's comment interface:

In the comments section, type: [code]javascript://%0dalert%28document.cookie%29[/code] and submit.

> The %0d is a newline to bypass potential filters. Expected output: Comment publishes, code block highlights, and 'javascript://' becomes a blue, clickable link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[injection]]
- [[wordpress]]
