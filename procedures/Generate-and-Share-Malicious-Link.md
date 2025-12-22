---
id: proc-linkpop-generate-link-001
tags:
  - link-generation
  - payload-delivery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.404Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Generate-and-Share-Malicious-Link

## Summary

This procedure covers generating a unique shareable URL from a malicious Linkpop template, enabling delivery of the stored XSS payload to victims for subsequent execution.

## Description

After injecting the XSS payload into a template, Linkpop provides a shareable link (e.g., https://linkpop.com/testnaglinagli) that renders the tainted content. This link can be distributed via email, social media, or phishing to trick victims into visiting and interacting, triggering the JavaScript. The procedure assumes the template has been successfully created with the payload.

## Requirements

1. Successfully created template with injected payload
2. Access to the dashboard's link generation feature
3. Means to distribute the link (e.g., email or messaging)

## Defense

Defensive measures and detection strategies:

- Scan generated links for suspicious patterns before sharing
- Educate users on verifying link origins and avoiding unsolicited shares
- Implement rate limiting on link generation to prevent abuse

## Objectives

1. Obtain a persistent, victim-facing URL embedding the XSS
2. Ensure the link renders the payload without immediate detection
3. Facilitate easy distribution for maximum reach

## Instructions

### Step 1: Save Template

**Context**: Finalize the creation to trigger link generation.

Complete any remaining fields and submit the template.

> The system processes and saves the page.

### Step 2: Copy Shareable Link

**Context**: Extract the unique URL for sharing.

Locate the 'Copy Link' button in the dashboard and click it to get the URL like https://linkpop.com/testnaglinagli.

> The link is copied to the clipboard; paste it into a text editor to verify.

### Step 3: Distribute Link

**Context**: Deliver to potential victims.

Share the link via preferred channels, disguising it as a legitimate resource.

> Victims visiting the link will load the malicious template.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- link-generation
- payload-delivery
