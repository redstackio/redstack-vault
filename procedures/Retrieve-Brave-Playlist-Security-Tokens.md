---
tags:
  - token-exposure
  - information-disclosure
  - javascript
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - iOS
  - WebView
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-13T23:52:33.358Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Credentials In Files]]'
id: 4803769a-ddf9-452f-a38c-8a46bfbe979d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[System Information Discovery]]'
---
---

# Retrieve-Brave-Playlist-Security-Tokens

## Summary

This procedure exploits information disclosure vulnerabilities in Brave iOS Playlist JavaScript files to extract hidden security tokens, enabling further exploitation like crafting messages for UXSS.

## Description

In Brave iOS, the Playlist feature embeds exact values of UserScriptManager.securityToken and UserScriptManager.messageHandlerToken directly into JavaScript code loaded in the WebView. An attacker-hosted malicious iframe on a cross-origin page can read these tokens from Playlist.js (line 353) and WindowRenderHelper.js (line 12), as they are exposed in prototypes like HTMLVideoElement.prototype.setAttribute and postMessage handlers. These tokens facilitate sending crafted messages to the app's native code, bypassing normal protections. The procedure targets Brave versions vulnerable to this exposure and requires the victim to load the malicious page in the browser.

## Requirements

1. Control of a remote server to host the malicious iframe (e.g., PHP script at https://csrf.jp/brave/playlist.php)
2. Victim using vulnerable Brave iOS on an iOS device
3. Cross-origin page (e.g., Google Sites) to embed the iframe without same-origin restrictions

## Defense

Defensive measures and detection strategies:

- Obfuscate or dynamically generate tokens in JavaScript instead of embedding plaintext values
- Implement Content Security Policy (CSP) to restrict script execution and iframe sources
- Monitor for anomalous postMessage calls or prototype modifications in WebView logs

## Objectives

1. Extract securityToken and messageHandlerToken from exposed JS
2. Prepare crafted payload using retrieved tokens
3. Enable escalation to arbitrary code execution on the main WebView

## Instructions

### Step 1: Host Malicious Iframe

**Context**: Set up the iframe source to load and execute token-reading JavaScript.

**Technical Details**: Create a PHP or HTML page that injects script to access window.HTMLVideoElement.prototype.setAttribute and window.postMessage, parsing for token values like $<notifyNode> and $<handler>.

### Step 2: Embed in Cross-Origin Page

**Context**: Load the iframe in a neutral domain to avoid sandboxing.

**Technical Details**: On the demo page (e.g., https://sites.google.com/view/nishimunea-brave-uxss1/page), include <iframe src="https://csrf.jp/brave/playlist.php" style="display:none;"></iframe>. The iframe runs on load.

### Step 3: Extract and Craft Message

**Context**: Use extracted tokens to build a postMessage payload.

**Technical Details**: In the iframe JS: var securityToken = /* parse from prototype */; var handlerToken = /* parse from postMessage */; then window.webkit.messageHandlers[handlerToken].postMessage({nodeTag: '');alert(document.location);//', securityToken: securityToken});

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Unsecured Credentials]]
- [[System Information Discovery]]

### Sub-Techniques

- [[Credentials In Files]]

## Commands Used


## Tools Used


## Tags

- token-exposure
- information-disclosure
- javascript

---
