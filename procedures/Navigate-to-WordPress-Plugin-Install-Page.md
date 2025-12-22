---
id: proc-navigate-admin
tags:
  - wordpress
  - admin
  - navigation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:53.903Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-WordPress-Plugin-Install-Page

## Summary

Redirect the original window to the WordPress plugin installation page to create the same-origin context needed for the SWF to access the DOM.

## Description

Using setTimeout, navigate to the plugin info page for a target plugin (e.g., wp-super-cache, modified maliciously), loading it in a thickbox iframe view to position the install button for DOM traversal.

## Requirements

1. Victim still authenticated
2. WordPress admin access
3. Malicious plugin hosted

## Defense

Defensive measures and detection strategies:

- Two-factor authentication for admin actions
- Log unexpected navigations
- Plugin install whitelisting

## Objectives

1. Load admin page with install UI
2. Establish opener reference
3. Position DOM elements for traversal

## Instructions

### Step 1: Execute Navigation Script

**Context**: From the original window, use setTimeout to load the URL.

**Command** (JavaScript):
```javascript
setTimeout(function() { window.location = 'http://target.com/wp-admin/plugin-install.php?tab=plugin-information&plugin=wp-super-cache&TB_iframe=true&width=600&height=550'; }, 200);
```

> Page loads. Expected output: Plugin details page with install button.

### Step 2: Confirm Same-Origin

**Context**: Ensure SWF can reference opener.

**Command** (Dev tools check):
```javascript
// opener.document ready
```

> DOM accessible. Expected output: No cross-origin errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[admin]]
