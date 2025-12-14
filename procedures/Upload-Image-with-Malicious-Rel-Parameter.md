---
id: proc-malicious-rel-upload-001
tags:
  - file-upload
  - input-injection
  - format-disruption
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-malicious-upload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:13.577Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Image-with-Malicious-Rel-Parameter

## Summary

This procedure exploits improper input validation in the Lichess /upload/image/user/{rel} endpoint by injecting colons into the rel parameter, breaking the ImageId format and potentially causing downstream parsing errors.

## Description

The Lichess backend (Picfit.scala) constructs ImageId as s"$rel:${random12}:${random8}.$extension" without sanitizing colons in rel, allowing a malicious rel like 'test:evil:format:break' to produce a 6-part ImageId. This can disrupt regex-based parsing in markdown or image lookup. The scenario targets the authenticated upload endpoint, requiring a session cookie. Outcomes include successful upload with malformed ID, leading to edge-case bugs.

## Requirements

1. Valid Lichess session cookie
2. Test image file (e.g., test.png)
3. curl installed for HTTP requests
4. Network access to lichess.org

## Defense

Defensive measures and detection strategies:

- Sanitize rel parameter to remove/disallow colons and other format-breaking chars
- Validate ImageId format post-construction before storage/processing
- Log and alert on uploads with unexpected rel patterns (e.g., containing ':')
- Use strict regex for parsing ImageId in downstream components

## Objectives

1. Inject colons to malformed ImageId
2. Confirm upload success with disrupted format
3. Observe potential parsing failures in app logic

## Instructions

### Step 1: Prepare and Send Malicious Upload

**Context**: Craft a POST request to the endpoint with colons in the URL path's rel segment, attaching the image and authentication headers.

**Command** ([[commands/curl-malicious-upload]]):

```bash
curl -X POST "https://lichess.org/upload/image/user/test:evil:format:break" -b "lila2=YOUR_SESSION_COOKIE" -H "Origin: https://lichess.org" -H "Referer: https://lichess.org/" -F "image=@test.png"
```

> Replace YOUR_SESSION_COOKIE with the actual value. The response should be JSON with imageUrl showing the malformed path, e.g., {"imageUrl":"https://image.lichess1.org/display?...&path=test:evil:format:break:ePU9oRLnNvCz:iFZRITKQ.png&..."}. Check for extra colons in the path to confirm injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-malicious-upload]]

## Tools Used

- [[tools/curl]]

## Tags

- exploitation
- web-vulnerability
