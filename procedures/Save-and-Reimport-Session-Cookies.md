---
tags:
  - cookie-manipulation
  - session-reuse
type: procedure
tools:
  - '[[tools/EditThisCookie]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:31:19.359Z'
sub_techniques: []
id: ed6f44ea-5024-403a-9c6f-f2b4d840ad2c
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Save-and-Reimport-Session-Cookies

## Summary

This procedure clears, saves, and reimports Coursera session cookies to simulate hijacking after logout, restoring access without re-authentication.

## Description

After logout, clear browser cookies to mimic a clean state, then export the original cookies to a file. Reimport them using extensions, exploiting the lack of invalidation. This targets web browsers interacting with coursera.org. Expected results include seamless session restoration, enabling access to protected areas.

## Requirements

1. Extracted cookies from prior steps.
2. Browser extension for cookie management.
3. Text editor for saving cookie data.

## Defense

Defensive measures and detection strategies:

- Bind sessions to IP/user-agent and invalidate on mismatch.
- Implement cookie signing to prevent tampering/reuse.
- Detect rapid cookie clear/import patterns via client-side logging.

## Objectives

1. Simulate post-logout clean state.
2. Preserve and restore session via cookies.
3. Prepare for unauthorized access validation.

## Instructions

### Step 1: Clear Cookies

**Context**: Remove all Coursera cookies to test reuse.

Use [[tools/EditThisCookie]] to select and delete cookies for coursera.org.

> Browser shows no active Coursera session.

### Step 2: Save Extracted Cookies

**Context**: Store cookies externally for persistence.

Export cookies via extension to a .txt or .json file, including name, value, domain, and expiry.

> File contains raw cookie data ready for import.

### Step 3: Reimport Cookies

**Context**: Inject saved cookies to hijack the session.

Use [[tools/EditThisCookie]] import function to load the file for coursera.org.

> Cookies appear in browser storage, potentially reactivating the session.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/EditThisCookie]]
