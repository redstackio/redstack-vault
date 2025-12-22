---
tags:
  - csrf
  - exploitation
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 723991fd-889b-4e9a-871f-d57ea1ea8b41
created_at: '2025-12-14T17:27:22.606Z'
updated_at: '2025-12-14T17:27:22.606Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute CSRF Attack on Admin User

## Summary

This procedure simulates delivering and triggering a CSRF exploit against an authenticated WordPress admin, resulting in unauthorized modification of plugin settings to demonstrate potential site disruption.

## Description

Targeting the Basic Google Maps Placemarks plugin, the attack relies on luring the admin to a malicious HTML page while their session is active. Upon loading, the page submits forged data to `/wp-admin/options.php`, overwriting settings like map width, height, address, zoom, type, and clustering. This can break frontend map displays, highlighting the risk of configuration tampering in multi-user environments. The procedure assumes the PoC from prior steps and focuses on execution and validation.

## Requirements

1. Functional CSRF PoC HTML file
2. Method to deliver the page (e.g., email link, external hosting)
3. Active admin session on the target site

## Defense

Defensive measures and detection strategies:

- Train admins to avoid untrusted links and use anti-phishing tools
- Implement same-site request modes (Lax/Strict) in cookies
- Audit plugin logs for unexpected setting changes and revert via backups

## Objectives

1. Induce the admin to execute the forged request
2. Confirm settings modification on the target
3. Evaluate functional impact on the site

## Instructions

### Step 1: Deliver Malicious Page

**Context**: Host or share the PoC to reach the victim admin.

Upload `csrf-poc.html` to a web server (e.g., GitHub Pages or local ngrok tunnel) and send the URL via email or chat, disguised as a legitimate link (e.g., "Check this map update").

> Ensure the link is clicked while the admin is logged into the WordPress site.

### Step 2: Trigger Submission

**Context**: Have the admin load the page, activating the form submission.

When the admin visits the URL in their browser (with active WP session), the auto-submit script or button triggers the POST to `/wp-admin/options.php` with malicious parameters.

> The request succeeds due to the valid, reusable nonce, bypassing CSRF checks.

### Step 3: Validate Impact

**Context**: Check the target site for changes and disruption.

Log into the WP admin as the same user, navigate to the plugin settings, and observe overwritten values (e.g., width/height as 'testing', zoom as 0). Test frontend pages with maps to confirm broken rendering.

> If settings are altered, the attack succeeded; report as vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploitation]]
- [[social-engineering]]
