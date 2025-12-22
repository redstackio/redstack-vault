---
tags:
  - xss
  - stored-xss
  - imgur
  - self-xss
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
updated_at: '2025-12-13T23:56:03.936Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fc5ab69f-a32b-4a87-a986-3ee2d6eb137e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Adding-Image-to-Folder

## Summary

This procedure triggers the stored self-XSS payload in the malicious Imgur folder by having the victim add an image to it, executing arbitrary JavaScript in the authenticated context.

## Description

Once the folder with the XSS payload in its name exists, Imgur's image addition UI renders the folder name unsafely when selecting it from the dropdown. Clicking the plus icon on an image and choosing the malicious folder causes the payload to execute, such as an onerror handler on an img tag. This requires user interaction but can be prompted via malicious links to images. Outcomes include JS execution for potential session hijacking, like stealing cookies or redirecting to phishing sites.

## Requirements

1. Malicious folder already created in victim's account
2. Victim directed to an Imgur image page
3. Victim performs the add-to-favorites action

## Defense

Defensive measures and detection strategies:

- Sanitize all user-generated content in UI rendering, including folder names
- Use Content Security Policy (CSP) to restrict inline JS execution
- Log and alert on XSS payload executions or unusual JS prompts

## Objectives

1. Execute the injected JS payload in the victim's browser
2. Achieve code execution for data exfiltration or account takeover
3. Exploit user interaction in a trusted application context

## Instructions

### Step 1: Lure Victim to Image Page

**Context**: Direct the victim to a specific Imgur image to initiate the addition process.

Share a link to an Imgur image, e.g., https://imgur.com/gallery/example-image, via email or social media.

> This positions the victim to interact with the favorites feature.

### Step 2: Perform Image Addition to Malicious Folder

**Context**: Trick or observe the victim adding the image, triggering the render of the payload.

On the image page, click the plus icon next to the heart icon in the bottom left, select 'Add to favorites', and choose the malicious folder from the list.

> Expected: The folder name renders, executing <img src=x onerror=prompt(1)>, popping an alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[imgur]]
