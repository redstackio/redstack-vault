---
tags:
  - data-leakage
  - cache-access
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
id: fcbfab43-4a00-40b8-86b0-bf9cbc957f4a
created_at: '2025-12-13T09:00:34.509Z'
updated_at: '2025-12-13T09:00:34.509Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve Leaked Data from Cache

## Summary

This procedure involves accessing the previously crafted and populated cached URL to extract the victim's sensitive information served by the proxy.

## Description

After the victim has accessed the URL, the attacker simply visits the same URL. The caching proxy returns the stored response containing personal data, achieving the leakage without authentication. This works on sites like algolia.com with improper cache validation.

## Requirements

1. Crafted URL with cached content
2. Public access to the target site's cache
3. No authentication needed for retrieval

## Defense

Defensive measures and detection strategies:

- Use cache keys that include authentication tokens
- Regularly purge or validate cached content
- Detect repeated accesses to suspicious URLs

## Objectives

1. Obtain leaked personal information
2. Validate successful exploitation
3. Achieve impact of data breach

## Instructions

### Step 1: Access Cached URL

**Context**: Visit the URL to retrieve the cached response.

> Example: Navigate to https://algolia.com/user/profile/random.css in a browser or via curl.

### Step 2: Extract Data

**Context**: Parse the response for sensitive information.

> Save and review the output for personal details.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[data-leakage]]
- [[cache-access]]
