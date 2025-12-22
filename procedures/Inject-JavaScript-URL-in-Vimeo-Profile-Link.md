---
tags:
  - xss
  - javascript-url
  - injection
  - vimeo
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.799Z'
sub_techniques: []
id: d579f420-3a2d-47d4-9b05-14096e518ffc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-JavaScript-URL-in-Vimeo-Profile-Link

## Summary

This procedure injects a malicious javascript: URL into the link field of Vimeo's profile settings, exploiting the lack of URL scheme validation to store an XSS payload.

## Description

The vulnerability stems from insufficient sanitization in the profile link addition feature, allowing javascript: protocols to be saved. In an attack scenario, an authenticated user adds a payload like 'javascript:alert(document.domain+"http://")' to their profile. This can lead to execution when the link is clicked, potentially by the user themselves or viewers of the profile. Prerequisites include access to the settings page. The outcome is a persisted malicious link enabling JavaScript execution in the browser context.

## Requirements

1. Access to Vimeo's profile settings page
2. Web browser for form submission
3. Understanding of JavaScript payloads for testing

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all input URLs to block javascript: schemes
- Implement server-side whitelisting for allowed protocols (e.g., http, https)
- Monitor for anomalous link additions in user profiles

## Objectives

1. Bypass URL validation to inject executable code
2. Persist the payload in the user's profile
3. Set up for payload execution via user interaction

## Instructions

### Step 1: Enter Payload in Link Field

**Context**: Locate the link addition input on the profile settings page and insert the malicious URL.

**Action**:

In the URL field for adding a new link, input: javascript:alert(document.domain+"http://")

> Submit the form to save. Expected output: The link is added to the profile without error, confirming lack of validation.

### Step 2: Save Profile Changes

**Context**: Persist the injection by updating the profile.

**Action**:

Click the save button on the profile settings form.

> Expected output: Profile updates successfully, with the new link visible in the profile view.

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
- [[injection]]

