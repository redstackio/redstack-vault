---
id: proc-overlay-deceptive-elements
tags:
  - clickjacking
  - ui-overlay
  - deception
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
updated_at: '2025-12-14T17:28:05.053Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Overlay-Deceptive-Elements-for-Click-Tricking

## Summary

This procedure adds overlaid HTML elements to a clickjacking PoC to guide victim clicks onto hidden iframe content, enabling actions like account deletion or rating submissions without user awareness.

## Description

Overlays use absolute-positioned divs with pointer-events: none to highlight click zones on the embedded Zomato page. For example, account deletion requires 3 clicks at precise coordinates, while ratings need 1-2. This deceives users into interacting with invisible sensitive forms, impacting integrity and availability.

## Requirements

1. Existing clickjacking PoC with embedded iframe
2. Knowledge of target page layout and click coordinates
3. Browser for coordinate testing

## Defense

Defensive measures and detection strategies:

- Disable pointer-events on untrusted overlays via CSP
- Use frame-busting JavaScript to detect embedding
- Log unusual click patterns or form submissions

## Objectives

1. Position overlays to align with sensitive elements
2. Guide multi-click sequences for complex actions
3. Ensure invisibility to avoid detection

## Instructions

### Step 1: Identify Click Coordinates

**Context**: Inspect the iframe content to find exact positions for actions.

Load PoC, use browser inspector to note coordinates (e.g., delete button at left:70px top:860px).

**Expected Output**: List of x,y positions for each required click.

### Step 2: Add Overlay Divs

**Context**: Insert divs over the iframe for guidance.

Update HTML:

```html
<div style="position: absolute; left: 70px; top: 860px; width: 50px; height: 50px; background: red; opacity: 0.5; pointer-events: none;">Click 1</div>
<iframe ... style="opacity: 0;"></iframe>
```

**Expected Output**: Visual markers on sensitive areas.

### Step 3: Sequence Multi-Click Actions

**Context**: For actions like deletion (3 clicks), add multiple divs.

Add divs for each step, e.g., Clicks 2&3 at left:330px top:600px.

**Expected Output**: Clicks trigger Zomato form submissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ui-redressing]]
- [[click-tricking]]
