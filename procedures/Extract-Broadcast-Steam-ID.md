---
id: proc-steam-id-extract-001
tags:
  - steam
  - id-extraction
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:35.514Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Extract-Broadcast-Steam-ID

## Summary

This procedure involves parsing the Steam broadcast URL to isolate the Steam ID parameter, which is essential for constructing the CSRF form targeting the vulnerable chat moderation endpoint.

## Description

The Steam broadcast URL follows a predictable format, making ID extraction straightforward via manual inspection or simple scripting. This step is reconnaissance-focused in the attack chain, enabling precise targeting of the `broadcaststeamid` parameter in the CSRF payload. Prerequisites include an active broadcast URL; outcomes provide the numeric ID for form inputs.

## Requirements

1. Access to the broadcast URL from Step 1
2. Web browser or text editor for parsing
3. Basic knowledge of URL structure

## Defense

Defensive measures and detection strategies:

- Obfuscate IDs in URLs or use token-based identifiers
- Log and monitor URL access patterns for anomalies
- Implement ID validation on all endpoints

## Objectives

1. Isolate the Steam ID from the broadcast URL
2. Prepare ID for use in CSRF form parameters
3. Ensure accuracy to avoid payload failures

## Instructions

### Step 1: Inspect the Broadcast URL

**Context**: Locate the URL generated from the broadcast start.

Copy the full URL, e.g., `https://steamcommunity.com/broadcast/watch/123456789/`, from the Steam interface.

### Step 2: Parse and Extract the ID

**Context**: Manually or programmatically extract the numeric segment.

In a browser, use developer tools (F12) to view the URL, or in a text editor, copy the value between `/watch/` and the trailing `/`. The extracted ID is `123456789` in this example.

> Verify the ID by testing it in a non-malicious context, like viewing the broadcast page.

**Expected Output**: A clean numeric Steam ID ready for form input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[steam]]
- [[id-extraction]]
- [[recon]]
