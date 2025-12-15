---
id: proc-uuid-2
tags:
  - referer-leakage
  - oauth-trigger
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:24:38.976Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Trigger-Referer-Leakage-via-Victim-Access

## Summary

This procedure relies on victims accessing the injected forum reply during an active Facebook OAuth flow, causing the browser to leak the authorization code in the referer header to the attacker's domain.

## Description

The attack exploits the default browser behavior of including the full referer URL (with query parameters like the OAuth code) when loading external resources via <img> tags. Victims must initiate Facebook login on the Rockstar site, receive the authorization code in the redirect, and then view the forum reply in the same session. Without a Referrer-Policy header, the sensitive code is exposed. This is passive from the attacker's side, relying on forum traffic.

## Requirements

1. Injected payload already present in a visible forum reply
2. Victims using browsers without strict referer policies (common in standard setups)
3. Active OAuth flow integration on the target site

## Defense

Defensive measures and detection strategies:

- Set Referrer-Policy: no-referrer on all pages handling OAuth redirects
- Sanitize forum content to prevent external resource loads
- Log and alert on referer headers containing OAuth parameters in external requests

## Objectives

1. Induce passive data leakage through normal user navigation
2. Capture transient OAuth codes before they expire
3. Enable collection without direct exploitation

## Instructions

### Step 1: Monitor Forum Traffic

**Context**: Wait for or lure victims to the thread during OAuth.

Use analytics or server logs to track views on the thread; no active action needed beyond payload placement.

### Step 2: Simulate Victim Conditions

**Context**: Test the trigger by replicating the OAuth flow.

Start Facebook OAuth on support.rockstargames.com, note the code in the URL, then open the forum reply in the same tab/session. Check your server for the referer request.

> Expected: Referer includes code=... parameter.

### Step 3: Validate Leakage

**Context**: Confirm the full referer is sent.

Inspect network requests in dev tools; ensure the img load sends Referer: https://support.rockstargames.com/...&code=LEAKED_CODE.

> Success if code is visible in server access logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[referer-leakage]]
- [[oauth-trigger]]
