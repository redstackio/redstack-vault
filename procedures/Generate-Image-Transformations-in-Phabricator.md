---
tags:
  - phabricator
  - image-transformation
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
detection_risk: medium
sub_techniques: []
id: b9065891-11b2-4207-9f4b-d91f82b24c64
created_at: '2025-12-14T05:32:13.525Z'
updated_at: '2025-12-14T05:32:13.525Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-Image-Transformations-in-Phabricator

## Summary

This procedure involves applying image transformations in Phabricator to a private file, which creates a new version that becomes publicly accessible, bypassing original privacy controls.

## Description

The 'regenerate' function in Phabricator's transformations interface processes the private image to create derivatives (e.g., cropped versions), but assigns public visibility and transfers ownership automatically. This exploits improper access control, exposing sensitive content like PII without consent. Requires access to the transformations page for a private file. Outcomes: A new public file is generated, uneditable by the owner.

## Requirements

1. Loaded transformations interface for a private image
2. Authenticated Phabricator session
3. Web browser capable of previewing images

## Defense

Defensive measures and detection strategies:

- Inherit visibility policies to transformed files
- Require explicit consent for public derivatives
- Block regeneration for private files without approval

## Objectives

1. Trigger transformation generation
2. Preview the new image version
3. Observe unintended visibility shift

## Instructions

### Step 1: Select Transformation Type

**Context**: Choose an image modification option in the interface.

In the transformations view, select a type such as 'profile crop'.

> This highlights the regeneration option for the selected transformation.

### Step 2: Click Regenerate

**Context**: Initiate the creation of a new transformed file.

Click 'regenerate' next to the selected option.

> Phabricator processes the image, creating a new version without updating the original.

### Step 3: Preview Transformed Image

**Context**: View the output to confirm generation.

Examine the preview of the new transformed image.

> Expected: Image displays, but check for new link generation indicating exposure.

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
- [[image-transformation]]
- [[privacy-leak]]
