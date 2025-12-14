---
tags:
  - token-leak
  - ajax-request
  - csrf-bypass
type: procedure
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:29.125Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 680f7b26-60b6-43d3-9122-d14af0cc4b62
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Trigger AJAX Request to Leak Authenticity Token

## Summary

This procedure triggers a victim's browser to execute GitLab JavaScript that sends an AJAX request to an attacker-controlled domain, leaking the Rails authenticity_token due to manipulated URL construction.

## Description

When the victim, authenticated in GitLab, interacts with the forged link, the JS in `environments_folder_view.js` or similar uses the tainted `location.pathname` to build the request URL. The authenticity_token, embedded in the page, is included in the request body or headers, exfiltrating it to the attacker without violating same-origin policy visibly.

## Requirements

1. Victim authenticated session in GitLab
2. Hosted malicious link on attacker domain
3. Monitoring setup on attacker server to capture requests

## Defense

Defensive measures and detection strategies:

- Enforce CORS policies strictly on all endpoints
- Tokenize requests with short-lived, single-use CSRF tokens
- Detect anomalous request patterns from JS files

## Objectives

1. Induce cross-domain AJAX call from victim's browser
2. Capture the leaked authenticity_token
3. Confirm token validity for further exploitation

## Instructions

### Step 1: Lure Victim to Malicious Link

**Context**: Ensure the victim is on a GitLab page with vulnerable JS loaded.

Send the forged link via email or embed in a site, prompting interaction like clicking to 'view environments'.

### Step 2: Execute JS on Interaction

**Context**: Let GitLab's JS handle the request automatically.

Upon click or page load, the JS triggers `Vue.http.get` or `$.ajax` to the forged URL, including the token from `meta[name="csrf-token"]`.

### Step 3: Capture and Log the Request

**Context**: Receive and store the token on the attacker server.

Set up a simple HTTP endpoint to log incoming requests, extracting the authenticity_token from headers (e.g., X-CSRF-Token) or POST body.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-leak]]
- [[ajax-request]]
- [[csrf-bypass]]
