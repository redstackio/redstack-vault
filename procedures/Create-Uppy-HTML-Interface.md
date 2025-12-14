---
tags:
  - uppy
  - client-setup
  - web
type: procedure
tools:
  - '[[tools/Uppy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.568Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b5bd82da-01e8-4f9d-a2a5-54138358d72d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Uppy-HTML-Interface

## Summary

This procedure sets up a basic HTML page with the Uppy JavaScript library, configuring the Dashboard, URL, and Tus plugins to connect to the local Companion server for file uploads via URLs.

## Description

Uppy is a modular file uploader that relies on the Companion server for remote URL handling. This setup creates a client-side interface targeting http://localhost:3020, allowing submission of arbitrary URLs that trigger SSRF on the server. The page loads Uppy v1.8.0 from CDN and initializes plugins for dashboard UI, URL input, and Tus upload endpoint. No server-side changes are needed; this prepares the attack vector for internal URL exploitation.

## Requirements

1. Web browser (Chrome, Firefox) for loading the HTML
2. Local Companion server running on port 3020
3. Internet access for CDN resources
4. Basic HTML/JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Disable or restrict URL plugins in Uppy configurations to trusted domains only
- Implement client-side URL validation before submission
- Monitor browser network requests for connections to localhost or internal IPs
- Use Content Security Policy (CSP) to block unauthorized script loading

## Objectives

1. Load functional Uppy interface in browser
2. Enable URL-based file addition targeting Companion
3. Facilitate SSRF trigger via user interaction

## Instructions

### Step 1: Create HTML File

**Context**: Write an HTML file incorporating Uppy CSS/JS and initializing the core with plugins.

**Command** (No CLI; manual file creation):
```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://releases.transloadit.com/uppy/v1.8.0/uppy.min.css">
</head>
<body>
  <script src="https://releases.transloadit.com/uppy/v1.8.0/uppy.min.js"></script>
  <script>
    const uppy = new Uppy.Core({
      plugins: [
        'Dashboard',
        'Url',
        'Tus'
      ]
    }).use(Uppy.Dashboard, { target: '#uppy' })
      .use(Uppy.Url, { companionUrl: 'http://localhost:3020' })
      .use(Uppy.Tus, { endpoint: 'https://master.tus.io/files/' });
  </script>
  <div id="uppy"></div>
</body>
</html>
```

> Save as index.html. Expected output: File created; no runtime errors on load.

### Step 2: Load in Browser

**Context**: Open the file to verify the dashboard renders correctly.

**Instructions**: Double-click index.html or serve via local HTTP (e.g., python -m http.server 8000) and navigate to it.

> Expected: Uppy dashboard with 'Add Files' button appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Uppy]]

## Tags

- uppy
- client-setup
- web
