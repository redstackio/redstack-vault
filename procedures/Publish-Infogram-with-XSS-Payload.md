---
tags:
  - xss
  - publication
  - public-exposure
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
updated_at: '2025-12-14T03:16:14.228Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 610f2748-dc24-4d83-91ac-271ca0eadc1e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Publish-Infogram-with-XSS-Payload

## Summary

This procedure publishes an Infogram infographic containing a persistent XSS payload, making it publicly accessible via a URL and exposing the vulnerability to any visitor.

## Description

After injecting the XSS payload, publishing the infographic generates a public URL where the Share button renders the malicious custom link. The platform does not sanitize the payload during public rendering, allowing it to persist and execute upon user interaction. This step requires no additional tools and relies on Infogram's sharing features. Expected outcomes include a live public page where victims can trigger the XSS.

## Requirements

1. Infographic with injected XSS payload
2. Permissions to publish infographics publicly
3. Internet access for sharing

## Defense

Defensive measures and detection strategies:

- Scan published content for XSS patterns before going live
- Restrict public sharing to verified content
- Implement server-side rendering checks for user inputs

## Objectives

1. Generate a public URL for the infographic
2. Ensure the Share button with payload is visible publicly
3. Expose the vulnerability without alerting during publication

## Instructions

### Step 1: Initiate Public Sharing

**Context**: From the Infogram dashboard, select the sharing options for the edited infographic.

Click the 'Share' or 'Publish' button in the editor to access public sharing settings.

### Step 2: Generate Public URL

**Context**: Configure the infographic for public access, embedding the vulnerable Share button.

Enable public viewing and generate the shareable URL. Ensure the custom link field is included in the public layout.

> The public URL will be something like https://infogram.com/public-xyz, accessible without login.

**Expected Output**: Public URL provided; infographic loads publicly without errors.

### Step 3: Test Public Accessibility

**Context**: Verify the infographic is live and the payload is present but dormant.

Open the public URL in an incognito browser window and inspect the Share button's HTML.

> Confirm the payload is rendered in the link attribute without execution.

**Expected Output**: Infographic visible; source shows injected payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[public-exposure]]
- [[infogram]]
