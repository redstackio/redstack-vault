---
tags:
  - xss
  - url-hash
  - jquery-injection
  - wordpress-plugin
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3ec1717f-b8e3-490f-894b-5427173db860
created_at: '2025-12-14T03:15:26.769Z'
updated_at: '2025-12-14T03:15:26.769Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-Gallery-Options-with-Malicious-URL-Hash

## Summary

This procedure involves constructing a URL with a malicious hash fragment to exploit the unsanitized use of `location.hash` in the Huge IT Image Gallery plugin's jQuery code, injecting arbitrary JavaScript into the DOM on the admin options page.

## Description

The vulnerability stems from the plugin's admin JavaScript in `gallery_Options_view.php`, where `jQuery(location).attr('hash')` is directly inserted into selectors like `jQuery('#gallery-view-tabs li a[href="'+strliID+'"]')` without escaping. A crafted hash like `#"><img src=M onerror=alert('0wn3d');>` breaks out of the attribute, injecting HTML/JS. This targets the admin page `/wp-admin/admin.php?page=Options_gallery_styles` and requires an active admin session. Outcomes include DOM manipulation leading to script execution, potentially enabling session theft or admin actions.

## Requirements

1. Active admin session from prior login
2. Knowledge of the target site's WordPress admin URL
3. Web browser developer tools for inspection (optional but recommended)

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all URL hash inputs in JavaScript selectors
- Use Content Security Policy (CSP) to restrict inline script execution
- Audit plugin code for unsanitized DOM manipulations and keep plugins updated

## Objectives

1. Deliver the malicious payload via URL hash
2. Trigger DOM parsing that reflects the injection
3. Position for JavaScript execution without direct server interaction

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the full URL incorporating the vulnerable page path and injected hash payload.

Manually craft the URL: `https://target.com/wp-admin/admin.php?page=Options_gallery_styles#"><img src=M onerror=alert('0wn3d');>`.

> Replace `target.com` with the actual domain. The hash payload escapes the href attribute and injects an img tag with onerror handler.

### Step 2: Load URL in Browser

**Context**: Access the page while authenticated to process the hash in the client-side jQuery.

Paste the crafted URL into the browser address bar and press Enter.

> The page should load the gallery options interface. Use browser dev tools (F12) to inspect the Network tab for no errors and Elements tab to see DOM reflection.

### Step 3: Confirm Hash Processing

**Context**: Verify the jQuery code has parsed the hash without sanitization.

Search the page source or console for the reflected hash content.

> Look for the injected `<img>` tag in the DOM tree under gallery tabs, indicating successful injection setup.

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
- [[url-hash]]
- [[jquery-injection]]
- [[wordpress-plugin]]
