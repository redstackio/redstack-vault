---
id: proc-uuid-3
tags:
  - csrf
  - poc
  - url-crafting
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.765Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft POC URL for View Inflation

## Summary

This procedure constructs a proof-of-concept URL exploiting the CSRF vuln in VK.com to encode multiple post IDs, enabling simultaneous view increments when visited by an authenticated user.

## Description

In the VK.com environment, the 'data' parameter accepts semicolon-separated post identifiers. The technical approach URL-encodes this payload into the endpoint. Prerequisites: Known post IDs and endpoint. Expected: A clickable link that inflates views without user awareness.

## Requirements

1. List of target post IDs (e.g., from VK.com URLs)
2. URL encoding tool or JavaScript encoder
3. Valid endpoint from prior steps

## Defense

Defensive measures and detection strategies:

- Validate and limit 'data' parameter length/content
- Rate-limit view registrations per session/IP

## Objectives

1. Encode multiple post IDs in 'data'
2. Create shareable POC URL
3. Test for multi-post impact

## Instructions

### Step 1: Gather Post Identifiers

**Context**: Extract IDs from target posts.

**Instructions**: From VK post URLs, parse IDs like 238237355_r268:767:16:1241520615.

> Collect several, including private group ones.

### Step 2: Encode and Construct URL

**Context**: Build the malicious payload.

**Instructions**: Join IDs with semicolons, URL-encode, and append to https://vk.com/al_page.php?act=seen&al=1&data=.

> Example: data=238237355_r268%3A767%3A16%3A1241520615%3B[other_ids].

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[poc]]
