---
id: proc-884159-attacker-session
tags:
  - session-hijacking
  - authentication
  - shopify
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/authenticate-mailbox-session]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.577Z'
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
# Initiate-Attacker-Session-Authentication

## Summary

This procedure establishes a valid session for the attacker's shop owner account with Shopify's mailbox service, obtaining a session ID that can be used to craft requests impersonating legitimate access while targeting another store.

## Description

To exploit the IDOR, a fresh session from the attacker's store is needed to pair with the target's shipping label ID. This involves sending an authentication request to the session endpoint, following a redirect in a browser to complete the flow, and extracting the session ID from the JSON response. The Origin header must match the attacker's shop domain (e.g., https://{shop}.myshopify.com). This step ensures the session is scoped but exploitable due to insufficient ID checks.

## Requirements

1. Valid shop owner credentials for the attacker's store
2. Attacker's shop domain (e.g., attacker.myshopify.com)
3. Browser for handling redirects and JSON parsing

## Defense

Defensive measures and detection strategies:

- Bind sessions strictly to shop IDs and validate all object references against session ownership
- Monitor cross-origin authentication attempts to mailbox.shopifycloud.com
- Implement CSRF tokens in session flows

## Objectives

1. Authenticate the attacker's session with the mailbox service
2. Obtain a valid session ID for GraphQL requests
3. Complete the OAuth-like install flow without errors

## Instructions

### Step 1: Send Session Authentication Request

**Context**: Initiate authentication using the attacker's shop details via [[commands/authenticate-mailbox-session]].

Execute [[commands/authenticate-mailbox-session]]:

```bash
curl 'https://mailbox.shopifycloud.com/session/authentication' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: */*' -H 'Origin: https://{shop}.myshopify.com' -H 'Sec-Fetch-Site: cross-site' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Accept-Language: en-US,en;q=0.9' --compressed
```

> Replace {shop} with the attacker's domain. Expected output: JSON with redirectUrl.

### Step 2: Complete Authentication in Browser

**Context**: Follow the redirect to finalize the session and extract the ID.

Copy the redirectUrl from the response, open it in [[tools/Web-Browser]], click the install button, and parse the resulting JSON (e.g., {"id": "abc", "status":"success"}) to get the session ID.

> Verify status is 'success' and note the 'id' value.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/authenticate-mailbox-session]]

## Tools Used

- [[tools/curl]]
- [[tools/Web-Browser]]

## Tags

- session-hijacking
- authentication
- shopify
