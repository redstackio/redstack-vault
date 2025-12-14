---
tags:
  - open-redirect
  - exploit
  - wordpress
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.091Z'
sub_techniques: []
id: d6a02092-b263-45f4-b477-9845dcf53dc9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Trigger-Open-Redirect

## Summary

This procedure constructs a malicious URL using the Base64-encoded payload and triggers the open redirect in the WordPress Feed Statistics plugin, demonstrating the vulnerability's exploitability for phishing.

## Description

By appending the encoded URL to the site's root or plugin endpoint (e.g., /wp-content/plugins/wordpress-feed-statistics/feed-statistics.php?url=), the plugin decodes and redirects without validation. Tested on WordPress 3.9.1 with Firefox on Debian Linux, this leads to uncontrolled navigation to external sites, enabling attacks on numerous installations.

## Requirements

1. Vulnerable WordPress site with Feed Statistics plugin
2. Base64-encoded malicious URL from prior step
3. Web browser for accessing and verifying the crafted URL

## Defense

Defensive measures and detection strategies:

- Add domain whitelisting in plugin code for redirects
- Use HTTP security headers like Strict-Transport-Security to prevent mixed redirects
- Scan logs for frequent redirects to unknown domains and block suspicious patterns

## Objectives

1. Build exploit URL targeting vulnerable endpoints
2. Execute redirect to confirm arbitrary navigation
3. Validate impact for phishing potential

## Instructions

### Step 1: Construct Malicious URL

**Context**: Combine the target site with the encoded parameter.

For root: http://www.example.com/?feed-stats-url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v.

For plugin: http://www.example.com/wp-content/plugins/wordpress-feed-statistics/feed-statistics.php?url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v.

> Ensure the Base64 string is URL-encoded if needed (e.g., replace / with %2F).

### Step 2: Access and Observe Redirect

**Context**: Use the browser to trigger the exploit and monitor behavior.

In [[tools/Firefox]], enter the crafted URL and press Enter; the page should redirect to the malicious site.

> Expected: Seamless redirect without user prompts or errors, landing on http://www.sooevilsite.com/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- open-redirect
- exploit
