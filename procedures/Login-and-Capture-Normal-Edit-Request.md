---
tags:
  - recon
  - xss
  - web
type: procedure
tools:
  - '[[tools/Chromium]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-quora-normal-edit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:44.616Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 76c40409-6ed1-4449-93d7-235c1d4c5d45
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Login-and-Capture-Normal-Edit-Request

## Summary

This procedure authenticates an attacker to Quora and captures a legitimate profile edit request from browser developer tools, providing a template for subsequent modifications in the XSS exploitation chain.

## Description

In Quora's AJAX-based interface, profile edits are sent via POST to /webnode2/server_call_POST?_m=edit. Capturing this request reveals parameters like __e2e_action_id (alphanumeric ID reflected in responses) and window_id (user channel). This step requires an authenticated session and uses Chromium's dev tools to monitor network traffic during a dummy edit, copying the full curl equivalent for replay and alteration. Prerequisites include a valid Quora account; outcomes include a baseline request that can be modified for IDOR and XSS injection.

## Requirements

1. Valid Quora login credentials
2. Chromium browser with developer tools enabled
3. Network access to quora.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on profile edit endpoints
- Monitor for unusual network captures or automated request copying in client-side logs
- Enforce client-side validation on action IDs before submission

## Objectives

1. Establish authenticated access to edit endpoints
2. Obtain a modifiable request template
3. Prepare for payload injection without triggering alerts

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to Quora and reach the profile edit page to initiate a request.

**Command** ([[commands/curl-quora-normal-edit]]):

Use [[tools/Chromium]] to log in manually.

> No command needed; manual browser action. Expected output: Profile page loaded with edit option.

### Step 2: Capture Request via Dev Tools

**Context**: Monitor and copy the POST request during a dummy profile update.

**Command** ([[commands/curl-quora-normal-edit]]):
```bash
# Manual: Update profile description to "a" and copy curl from Network tab
curl 'https://www.quora.com/webnode2/server_call_POST?_v=2rtUq6Z4HO9gWK&_m=edit' -H 'Cookie: m-b="██████████████████"; m-sa=1; m-s="███████████████"; m-screen_size=1920x1080; m-login=1; m-ju=███████████████████████████; m-early_v=4e4c117b82baf40e; m-tz=-120; m-css_v=69026465bc2615b6; m-wf-loaded=q-icons-q_serif; _ga=GA1.2.2058437224.1502195915; _gid=GA1.2.1848940326.1502195915' -H 'Origin: https://www.quora.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://www.quora.com/profile/Aleph-NaN' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'DNT: 1' --data 'json={"args":[],"kwargs":{"id":███████████,"input":{"sections":[{"type":"plain","indent":0,"quoted":false,"spans":[{"modifiers":{},"text":"a"}]}],"caret":{"start":{"spanIdx":0,"sectionIdx":0,"offset":1},"end":{"spanIdx":0,"sectionIdx":0,"offset":1}}}}}&revision=904d048187b642341464067b64246119b8ce9489&formkey=6a34c75ed7fda8439ca2407b4520c974&postkey=736f2eea9e3826808823625bf4ede215&window_id=dep3204-1727465467565139446&referring_controller=user&referring_action=profile&_lm_transaction_id=0.7159021828610441&_lm_window_id=dep3204-1727465467565139446&__vcon_json=["2rtUq6Z4HO9gWK"]&__vcon_method=edit&__e2e_action_id=esl2xq4xyj&js_init={"id":████████████,"input":"user_description_text","typing_area":null,"draft_space":null,"unsaved_content_msg":"Your content has not been saved.","focus_onload":false,"is_qtext":true,"require_comment":false,"require_value":false,"content_type":null,"submit_text":"Update","show_editor":false}&__metadata={}' --compressed
```

> This captures the request; expected output: HTTP 200 with edit applied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/curl-quora-normal-edit]]

## Tools Used

- [[tools/Chromium]]

## Tags

- recon
- web
