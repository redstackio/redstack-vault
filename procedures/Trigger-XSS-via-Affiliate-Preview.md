---
tags:
  - xss
  - open-redirect
  - trigger
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:26.153Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fe2ab9e9-2f58-4dd5-a8f0-399185357362
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-XSS-via-Affiliate-Preview

## Summary

This procedure outlines how to trigger the stored XSS payload in Revive Adserver by previewing affiliate invocation tags as an administrator, leading to JavaScript execution and an open redirect to an arbitrary site.

## Description

After injecting the payload into the Website URL, an administrator can generate invocation tags via the affiliate-preview.php endpoint. The preview renders the stored website properties without proper escaping, executing the injected img tag's JavaScript. Clicking the banner triggers the onclick event, redirecting the user to a malicious site like google.com. This exploits the lack of output encoding in the preview rendering, affecting authenticated admins and potentially leading to phishing or session hijacking.

## Requirements

1. Administrator credentials for preview access
2. Injected payload from prior procedure
3. Direct URL access to affiliate-preview.php

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered outputs in preview endpoints (e.g., htmlspecialchars on URLs)
- Restrict preview access to trusted contexts or add CSRF tokens
- Log and alert on unexpected redirects or script executions
- Use browser security features like X-Frame-Options and strict CSP

## Objectives

1. Render the stored payload in the admin preview
2. Execute JavaScript to perform open redirect
3. Demonstrate impact on authenticated users

## Instructions

### Step 1: Login as Administrator

**Context**: Elevate to admin privileges to access preview tools.

Instructions: Log in to the Revive Adserver admin panel using administrator credentials.

### Step 2: Access Affiliate Preview Endpoint

**Context**: Generate tags that include the vulnerable website, rendering the payload.

Instructions: Construct and navigate to `http://[target]/admin/affiliate-preview.php?codetype=invocationTags%3AoxInvocationTags%3Aspc&block=0&blockcampaign=0&target=&source=&withtext=0&charset=&noscript=1&ssl=0&comments=0&affiliateid=1&submitbutton=Generate`, replacing [target] with the instance URL and affiliateid with a relevant ID linked to the injected website.

> This URL simulates tag generation for SPC invocation, embedding the website URL in the output.

**Expected Output**: Page displays invocation code with a rendered banner image.

### Step 3: Interact to Trigger Payload

**Context**: Execute the JavaScript by simulating user interaction.

Instructions: Click on the Header Script Banner image in the preview output.

> The onclick (or onerror) event fires, executing window.location to redirect.

**Expected Output**: Browser navigates to the specified external URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[xss]]
- [[revive-adserver]]
