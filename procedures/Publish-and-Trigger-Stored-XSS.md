---
tags:
  - xss-trigger
  - publish
  - client-execution
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:30.573Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: d598a277-870e-41b9-8f42-2ec1d98485e6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Publish-and-Trigger-Stored-XSS

## Summary

This procedure publishes the infographic containing the stored XSS payload and demonstrates triggering the JavaScript execution by clicking the malicious link in a viewer's browser.

## Description

After injection, this procedure finalizes the attack by making the infographic public, generating a shareable URL where the malicious media link is rendered. Viewers clicking the link execute the javascript: payload in their browser context, potentially leading to session hijacking or data exfiltration. It requires no additional tools beyond a browser, focusing on the delivery and activation phase.

## Requirements

1. Infographic with stored payload from prior injection
2. Infogram account with publish permissions
3. Victim browser (can be your own for testing)
4. Public internet access

## Defense

Defensive measures and detection strategies:

- Escape or neutralize URI schemes in rendered links (e.g., prefix with 'void:' for javascript:)
- Implement click handlers to validate links before navigation
- Educate users on suspicious infographics and disable JavaScript if possible
- Scan published content for malicious URIs pre-publication

## Objectives

1. Expose the stored payload to arbitrary viewers
2. Trigger JavaScript execution via user interaction
3. Achieve client-side impact like alert or cookie theft

## Instructions

### Step 1: Publish Infographic

**Context**: Generate a public URL to host the payload.

In the editor, click 'Publish' and select 'Make public'.

> This creates a URL like https://infogram.com/step-by-step-chartsgreaterlesssvg-onloadalert1greater-1ggk2694e7dj2n0.

### Step 2: Access Public Page

**Context**: Simulate victim access to the infographic.

Open the public URL in a new browser tab or incognito window.

> The page loads with the media element containing the malicious link.

### Step 3: Interact with Link

**Context**: Click to execute the payload.

Locate and click the injected link in the media element.

> Alert pops up with document.domain, confirming XSS.

### Step 4: Validate Impact

**Context**: Check for potential further exploitation.

In a real attack, replace alert with code to exfiltrate session data (e.g., send cookies to attacker server).

> Success: Arbitrary JS runs in victim's context.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-execution
- drive-by
