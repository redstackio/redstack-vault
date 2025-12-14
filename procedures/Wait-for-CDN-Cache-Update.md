---
id: proc-cdn-wait-001
name: Wait-for-CDN-Cache-Update
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.273Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - xss
  - cdn
  - propagation
platforms:
  - Web
tools:
  - '[[tools/Browser-DevTools]]'
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Wait-for-CDN-Cache-Update

## Summary

This procedure monitors and waits for the malicious Graphie to propagate to Khan Academy's CDN (cdn.kastatic.org), ensuring it's available for rendering on target pages.

## Description

After upload, CDN caching may delay availability. Attackers poll the asset URL until the malicious version appears, potentially disabling client-side cache. Expected outcome: Confirmed propagation, ready for XSS trigger.

## Requirements

1. Uploaded file hash and CDN URL
2. Browser for monitoring

## Defense

Defensive measures and detection strategies:

- Implement short TTLs on CDN assets
- Sign and validate CDN files with hashes
- Log and alert on rapid asset changes

## Objectives

1. Verify malicious content in CDN response
2. Minimize wait time for execution
3. Handle cache invalidation if needed

## Instructions

### Step 1: Poll CDN URL

**Context**: Repeatedly fetch to check for update.

Use browser console or curl (adapt to JS):

```javascript
fetch('https://cdn.kastatic.org/ka-perseus-graphie/2122427aa8dc4ef2a59058bc1a7a934ba6ca6747.svg').then(r => r.text()).then(console.log);
```

> Run every 30 seconds. Expected output: Response containing onload or script.

### Step 2: Disable Cache if Stuck

**Context**: Force refresh using devtools.

In [[tools/Browser-DevTools]], disable cache under Network tab.

> Clears local cache. Expected output: Fresh fetch shows malicious content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-DevTools]]

## Tags

- [[xss]]
- [[cdn]]
