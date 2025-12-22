---
tags:
  - phabricator
  - image-transformation
  - access-control
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
id: 77d4b274-4959-44fa-9d4c-4668653c22d7
created_at: '2025-12-14T05:32:13.529Z'
updated_at: '2025-12-14T05:32:13.529Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-View-Transformations-in-Phabricator

## Summary

This procedure covers accessing the 'View Transformations' interface for an uploaded private image in Phabricator, enabling the setup for generating new versions that expose the content publicly.

## Description

Phabricator's image handling includes a transformations feature for resizing or cropping, accessible via the file details page. For a private image, this interface should respect original permissions, but it does not, allowing regeneration that creates public derivatives. This step requires an authenticated session and the uploaded private file. Outcomes include loading the interface without altering the original file's privacy, but priming the vulnerability.

## Requirements

1. Previously uploaded private image in Phabricator
2. Authenticated access to the file details page
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Restrict transformation access to private files
- Log all transformation views for private assets
- Audit file visibility inheritance in transformations

## Objectives

1. Locate and open the transformations interface
2. Review available options without triggering changes
3. Identify potential exposure points

## Instructions

### Step 1: Navigate to File Details

**Context**: Go to the details page of the private uploaded image.

From the Phabricator dashboard, search for or navigate to the uploaded file's page.

> This displays file metadata, including visibility confirmation.

### Step 2: Click View Transformations

**Context**: Access the specific interface for image modifications.

On the right side of the file details page, click 'View Transformations'.

> The interface loads, showing options like profile crop for the private image.

### Step 3: Verify Interface Load

**Context**: Ensure the private file context is maintained.

Confirm the original file remains private in the interface.

> Expected: No immediate visibility changes; options ready for regeneration.

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
- [[access-control]]
