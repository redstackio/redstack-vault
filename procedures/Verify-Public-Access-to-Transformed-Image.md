---
tags:
  - phabricator
  - access-control
  - privacy-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: eec61a6b-82ad-458b-9c13-ea69fdd6e610
created_at: '2025-12-14T05:32:13.521Z'
updated_at: '2025-12-14T05:32:13.521Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Public-Access-to-Transformed-Image

## Summary

This procedure verifies that the transformed image from Phabricator is now publicly accessible, confirming the access control vulnerability and the inability of the owner to remediate.

## Description

After transformation, Phabricator generates a public link for the new file, stripping privacy and ownership from the original uploader. This step tests accessibility in an unauthenticated context and checks for control loss, highlighting the privacy breach impact (e.g., exposed PII). Requires the transformations page and a new incognito session. Outcomes: Proof of public exposure with no delete/edit options.

## Requirements

1. Recently generated transformed image in Phabricator
2. Access to the transforms page
3. Incognito browser or separate unauthenticated session

## Defense

Defensive measures and detection strategies:

- Audit public file creation from private sources
- Provide ownership retention for derivatives
- Enable user alerts for visibility changes

## Objectives

1. Locate the public link for the transformed file
2. Test unauthenticated access
3. Confirm loss of control by owner

## Instructions

### Step 1: Return to Transforms Page

**Context**: Revisit the interface to find the new file link.

Go back to the 'View Transformations' page for the original file.

> A new entry with a link to the transformed image appears.

### Step 2: Access the Link

**Context**: Test if the link allows public viewing.

Copy the link to the transformed file and open it in an incognito window or share with another user.

> The image loads publicly, accessible without login.

### Step 3: Check Permissions

**Context**: Verify the original owner's inability to manage the file.

Attempt to edit or delete the transformed file from the owner's account.

> Expected: No permissions; file is uncontrollable, confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phabricator]]
- [[access-control]]
- [[privacy-leak]]
