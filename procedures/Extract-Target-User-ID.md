---
tags:
  - discovery
  - user-enum
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
updated_at: '2025-12-14T17:25:28.986Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 613d9368-bd54-4dfe-aeb6-f3e7d615987b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-Target-User-ID

## Summary

This procedure retrieves the internal userID of a target TopCoder user from their public profile page source, enabling direct reference in API requests for IDOR exploitation.

## Description

TopCoder public profiles embed the 'userID' in the HTML source, making it accessible without authentication. This step involves basic browser inspection to extract the numeric ID, which is then used to bypass authorization in the Chameleon API. It's a low-risk reconnaissance action that relies on client-side developer tools.

## Requirements

1. Web browser with dev tools (e.g., Chrome F12)
2. URL of target user's public profile (e.g., https://www.topcoder.com/members/nomadex41)

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove internal IDs from public-facing HTML
- Implement client-side protections like CSP to limit dev tools usage
- Monitor for automated scraping of profile pages

## Objectives

1. Locate and copy the target 'userID'
2. Verify ID validity for API targeting
3. Prepare for request modification

## Instructions

### Step 1: Visit Target Profile

**Context**: Access the public profile page of the desired user.

Navigate to https://www.topcoder.com/members/{username}, e.g., https://www.topcoder.com/members/nomadex41.

**Expected Output**: Profile page loaded with user details.

### Step 2: Open Developer Tools

**Context**: Inspect the page source for hidden identifiers.

Press F12 to open dev tools, then use CTRL-F to search for 'userID'.

**Expected Output**: Search result highlighting the userID value in JSON or script tag.

### Step 3: Copy UserID

**Context**: Extract the numeric value for use in API requests.

Copy the value, e.g., "userID": 40991562.

**Expected Output**: Valid integer ID ready for pasting.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- discovery
- user-enum
