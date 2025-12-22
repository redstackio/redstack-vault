---
id: proc-extract-victim-ids
tags:
  - profile-recon
  - id-extraction
  - public-enum
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:47.463Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-ProfileId-and-ImageId-from-Victim-Profile

## Summary

This procedure involves accessing a victim's public LinkedIn profile to copy and parse the featured image viewer link, extracting the required ProfileId and ImageId for IDOR exploitation.

## Description

LinkedIn exposes ProfileId and ImageId in public image viewer URLs, such as https://www.linkedin.com/in/username/details/featured/[ImageId]/single-media-viewer?type=IMAGE&profileId=[ProfileId]. No login is needed for this step, making it low-risk reconnaissance. The extracted IDs are directly usable in the modified API request. This leverages the vulnerability's root cause: lack of ID obfuscation in public links.

## Requirements

1. Target victim's LinkedIn username or profile URL
2. Web browser
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize IDs in public URLs
- Implement access controls on profile media links

## Objectives

1. Identify target featured image publicly
2. Parse URL for exploitable parameters
3. Prepare IDs for request substitution

## Instructions

### Step 1: Access Victim Profile

**Context**: View the public profile to locate featured media.

Enter the victim's username in LinkedIn search or direct URL (e.g., linkedin.com/in/victim-username) and navigate to the Featured section.

### Step 2: Copy and Parse Image Link

**Context**: Extract IDs from the viewer URL.

Click on a featured image to open the viewer, copy the full URL, and parse: ImageId from path (/[ImageId]/), ProfileId from query (?profileId=[ProfileId]).

**Expected Output**: Two values: e.g., ProfileId=123456789, ImageId=urn:li:fsd_profileTreasuryMedia:987654321.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[profile-recon]]
- [[id-extraction]]
- [[public-enum]]
