---
id: proc-enter-arbitrary-url
tags:
  - url
  - input
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:13.435Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enter-Arbitrary-Image-URL

## Summary

This procedure involves inputting an arbitrary URL pointing to a remote image into the modified upload field, preparing the form for submission that will trigger server-side fetching.

## Description

Following input type modification, this step supplies a URL to an attacker-controlled or arbitrary image, exploiting the lack of server-side URL validation. In SSRF contexts, this can lead to internal resource access if the URL targets sensitive endpoints.

## Requirements

1. Modified input field accepting URLs
2. Valid image URL (e.g., public or controlled)
3. No additional tools beyond browser

## Defense

Defensive measures and detection strategies:

- Whitelist allowed URL domains for image fetches
- Sanitize and validate all incoming URLs server-side
- Rate-limit profile update requests

## Objectives

1. Provide a fetchable URL
2. Avoid client-side errors
3. Align with SSRF payload

## Instructions

### Step 1: Select Target URL

**Context**: Choose a URL for testing or exploitation.

No command; manually select e.g., https://example.com/test.jpg.

> Ensure URL returns a valid image. Expected output: URL ready to paste.

### Step 2: Input the URL

**Context**: Enter into the form field.

Click the input and paste the URL.

> Field accepts text. Expected output: URL displayed in input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[url]]
- [[input]]
