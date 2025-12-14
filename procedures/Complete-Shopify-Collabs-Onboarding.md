---
tags:
  - onboarding
  - social-media
  - shopify
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:43.844Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b367b45a-ab66-4287-9c9a-1c5680929900
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Complete-Shopify-Collabs-Onboarding

## Summary

This procedure finalizes the onboarding process by connecting a social media account and editing the creator profile, granting early access to the platform.

## Description

Onboarding in Shopify Collabs requires linking a social media account (e.g., Instagram) and updating profile details to validate the creator. This legitimate step establishes full authenticated access, which is prerequisite for exploiting the XSS in the creator_redirect parameter. Completion logs the user in with early bird privileges.

## Requirements

1. Access to a social media account (e.g., Instagram credentials)
2. Loaded onboarding page
3. Valid profile information

## Defense

Defensive measures and detection strategies:

- Validate social media OAuth tokens
- Require profile verification (e.g., photo upload)
- Monitor for rapid onboarding completions

## Objectives

1. Connect social media for creator validation
2. Edit and save profile details
3. Achieve full platform access

## Instructions

### Step 1: Connect Social Media

**Context**: Link an external account to enable Collabs features.

Select and connect a social media account like Instagram via OAuth.

> Authorize the connection. Expected output: Social media linked successfully.

### Step 2: Edit Profile

**Context**: Customize creator information as required.

Fill in profile fields such as bio, interests, or content.

> Save changes. Expected output: Profile updated and onboarding advanced.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[onboarding]]
- [[social-media]]
- [[shopify]]

