---
tags:
  - clickjacking
  - browser-test
  - verification
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
updated_at: '2025-12-14T17:28:04.439Z'
skill_level: novice
impact_level: high
detection_risk: low
sub_techniques: []
id: c6906eef-789d-41af-8ac4-24cb8dc75a25
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate-Clickjacking-by-Loading-HTML-in-Browser

## Summary

This procedure loads the prepared HTML file in a browser to verify the clickjacking attack, confirming that users can be tricked into interacting with nextcloud.com elements disguised by the overlay.

## Description

Once the HTML payload is ready, opening it in a browser simulates the attack vector. The iframe loads nextcloud.com seamlessly due to missing protections, and clicking the overlaid button performs actions on the site (e.g., submitting a form). This demonstrates the vulnerability's impact, such as deceiving users into account actions or data submissions. The environment is a standard web browser, with outcomes including visual confirmation of framing and interaction hijacking.

## Requirements

1. Completed clickjack.html file with iframe and overlay
2. A modern web browser (e.g., Chrome, Firefox)
3. Local file access to open the HTML

## Defense

Defensive measures and detection strategies:

- Browser extensions like NoScript or uBlock Origin to block suspicious iframes
- Server-side logging of referer headers to detect framing attempts
- User training to avoid clicking on untrusted pages

## Objectives

1. Confirm nextcloud.com embeds without blocking
2. Validate overlay deceives clicks into site actions
3. Assess potential for real-world user compromise

## Instructions

### Step 1: Load HTML File in Browser

**Context**: Open the local file to render the clickjacking setup and observe the embedded site.

Navigate to the file location and double-click clickjack.html, or use File > Open in the browser menu to load it.

> The page should display the iframe with nextcloud.com visible (adjust opacity if needed). Ensure no frame-busting script blocks the load.

### Step 2: Test Deceptive Interaction

**Context**: Interact with the overlay to verify it triggers unintended actions on the framed site.

Click the "Click and go!" button on the overlay. Observe if it aligns with and activates an element on nextcloud.com, such as a link or form.

> Successful test: The click performs an action on nextcloud.com (e.g., navigation or submission) while the user believes they are interacting with the malicious button. Use browser dev tools to inspect network requests for confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[browser]]
- [[web]]
