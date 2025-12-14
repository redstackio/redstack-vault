---
id: proc-uuid-12345
tags:
  - csrf
  - web
  - widgets
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:36.152Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-CSRF-Page-for-VK-Widgets

## Summary

This procedure involves creating a malicious HTML page that exploits CSRF vulnerabilities in VK.com's application widgets by forging requests to the preview box endpoint, where insufficient hash checks allow unauthorized submissions without proper token validation.

## Description

In the context of VK.com's widgets, the preview box feature lacks robust hash verification, enabling attackers to craft cross-site requests that appear legitimate. This procedure details building an auto-submitting HTML form targeting the vulnerable endpoint, typically used for previewing widget configurations. Prerequisites include understanding the widget API structure via inspection tools and hosting capabilities. Expected outcomes include successful forgery leading to unauthorized widget actions, such as data modification, when loaded by an authenticated user.

## Requirements

1. Access to a web server or hosting service to serve the malicious HTML
2. Knowledge of VK.com widget endpoint URLs (e.g., via browser inspection)
3. Victim authenticated to VK.com in their browser session

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens with hash-based validation on all state-changing endpoints
- Use Content Security Policy (CSP) to restrict form submissions to same-origin
- Monitor for anomalous widget preview requests from unexpected referers

## Objectives

1. Forge a legitimate-looking request to the widget preview box
2. Bypass hash checks to enable unauthorized action execution
3. Prepare for delivery via social engineering to authenticated victims

## Instructions

### Step 1: Inspect Legitimate Widget Request

**Context**: Use browser developer tools to capture a legitimate POST request to the VK.com widget preview endpoint, noting parameters like action, widget_id, and any hash fields.

No specific command; perform manually in browser console or network tab.

> Identify the endpoint URL (e.g., https://vk.com/widget_preview) and required form data, ensuring the hash parameter is either omitted or forged to match expected format.

### Step 2: Create Malicious HTML Form

**Context**: Build an HTML page with an auto-submitting form that replicates the inspected request, targeting the preview box to exploit insufficient validation.

No command; write and save as .html file:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://vk.com/widget_preview" method="POST">
  <input type="hidden" name="action" value="update_widget">
  <input type="hidden" name="widget_id" value="target_widget">
  <input type="hidden" name="malicious_param" value="attacker_value">
  <!-- Hash omitted or static to bypass check -->
</form>
<script>
  document.getElementById('csrf-form').submit();
</script>
</body>
</html>
```

> This form auto-submits on load, sending forged data. Host on attacker domain and verify submission in a test environment.

### Step 3: Host and Test the Page

**Context**: Deploy the HTML to a public server and test in a browser logged into VK.com to confirm the request executes without errors.

Upload to hosting service (e.g., GitHub Pages) and access via URL.

> Expected: Network tab shows POST to VK endpoint succeeding, with server processing the action due to missing hash enforcement.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[widgets]]
