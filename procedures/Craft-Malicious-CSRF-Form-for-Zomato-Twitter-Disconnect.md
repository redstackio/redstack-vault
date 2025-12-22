---
tags:
  - csrf
  - web-exploit
  - html-form
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
updated_at: '2025-12-14T17:27:30.103Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5a96e87b-53e9-4d62-87f3-d5b43f4252c6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-CSRF-Form-for-Zomato-Twitter-Disconnect

## Summary

This procedure involves creating and hosting an HTML form that exploits the CSRF vulnerability in Zomato's Twitter disconnect endpoint, allowing automatic submission to force unlinkage without user consent.

## Description

The Zomato platform's /php/disconnect_twitter_profile.php endpoint uses a GET request without CSRF token validation, origin checks, or referer validation. By crafting an HTML page with a form that auto-submits this request, an attacker can leverage the victim's active session to perform the action. This targets authenticated users with Twitter integrated, disrupting their account linkages. Prerequisites include identifying the endpoint via network inspection during normal disconnection flows.

## Requirements

1. Access to a web hosting service to serve the HTML file
2. Knowledge of the target endpoint URL and required headers
3. Victim must have an active Zomato session with Twitter connected

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Enforce same-origin policy and validate referer/origin headers
- Monitor for anomalous disconnect requests from unexpected sources

## Objectives

1. Forge a request to the vulnerable endpoint
2. Automate submission to bypass user interaction
3. Achieve unauthorized account modification

## Instructions

### Step 1: Analyze Endpoint

**Context**: Inspect the legitimate disconnection process to capture the exact request details.

Use browser developer tools to monitor network traffic while disconnecting Twitter on Zomato. Note the GET URL and any headers like X-Requested-With: XMLHttpRequest.

### Step 2: Create HTML Form

**Context**: Build the malicious page that mimics the request.

Write an HTML file with a form action set to https://www.zomato.com/php/disconnect_twitter_profile.php. Use method="GET" and add a script to submit on load:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://www.zomato.com/php/disconnect_twitter_profile.php" method="GET">
<input type="hidden" name="some_param" value="if_needed">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

To mimic AJAX, include headers via JavaScript if needed, but GET forms suffice for basic exploitation.

### Step 3: Host the Page

**Context**: Make the page accessible via a URL.

Upload the HTML to a free hosting service like GitHub Pages or a personal server. Obtain the public URL for delivery.

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
- [[web-exploit]]
