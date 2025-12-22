---
tags:
  - xss
  - stored-xss
  - slack
  - javascript-uri
  - clipboard-injection
  - websocket
  - ios-exploit
type: attack_chain
tools:
  - '[[tools/Clipboard-Viewer]]'
  - '[[tools/Python]]'
  - '[[tools/Google-Chrome]]'
  - '[[tools/iOS-Slack-App]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/set-chromium-clipboard-payload]]'
platforms:
  - Web
  - iOS
complexity: medium
procedures:
  - '[[procedures/Discover-javascript-Link-Insertion-in-Editing-Mode]]'
  - '[[procedures/Modify-WebSocket-Request-to-Insert-Malicious-URI]]'
  - '[[procedures/Inject-XSS-Payload-via-Clipboard-Manipulation]]'
  - '[[procedures/Enable-Editing-Permissions-to-Affect-Team-Members]]'
  - '[[procedures/Exploit-XSS-on-iOS-to-Read-Local-Files]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
description: >-
  A multi-stage stored XSS attack exploiting Slack's Markdown editor in editing
  mode to insert javascript: URIs, enabling script execution on team members and
  local file access on iOS.
skill_level: intermediate
impact_level: high
id: 3979fb6d-bdd4-474c-be98-94ba30f89241
created_at: '2025-12-13T23:55:38.204Z'
updated_at: '2025-12-13T23:55:38.204Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Stored XSS in Slack Markdown Editor via javascript: URIs for Arbitrary Script Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in Slack's Markdown editor during editing mode.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Vulnerability] --> B[Payload Insertion via WebSocket or Clipboard]
    B --> C[Enable Editing Permissions]
    C --> D[Script Execution on Click]
    D --> E[Local File Access on iOS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#9b59b6
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Clipboard-Viewer]]
- [[tools/Python]]
- [[tools/Google-Chrome]]
- [[tools/iOS-Slack-App]]

### Target Environment

- Slack team.slack.com (web and iOS app)
- Markdown editor in post editing mode
- WebSocket communication enabled
- Editing permissions on shared posts

### Initial Access Requirements

- Valid Slack team account with post creation/editing access
- Network access to team.slack.com
- No prior elevated privileges needed, but team member interaction required

## Detailed Attack Procedures

### Step 1: Discovery of Vulnerability
procedure: [[procedures/Discover-javascript-Link-Insertion-in-Editing-Mode]]

**Objective**: Identify that javascript: URIs can be inserted in Slack's Markdown editor without validation during editing mode.

**Instructions**: Review old articles or test the Markdown editor by attempting to insert a javascript: link like `javascript:alert('XSS')`. Observe that no sanitization occurs in editing mode, unlike public links.

**Expected Output**: Successful insertion of the link without errors, visible in the editor preview.

**Success Indicators**:
- Link renders as clickable without blocking
- No validation errors in console or UI

### Step 2: Payload Insertion via WebSocket Modification
procedure: [[procedures/Modify-WebSocket-Request-to-Insert-Malicious-URI]]

**Objective**: Bypass direct insertion by modifying WebSocket requests during undo operations to embed the malicious javascript: URI.

**Instructions**: Perform an undo (Ctrl+Z) after deleting a link in the editor, capture the WebSocket request, and modify the 'links' array to include `{'url': 'javascript:alert("XSS")'}`. Replay the modified request.

**Expected Output**: The malicious link appears in the post editor upon reload.

**Success Indicators**:
- Modified request accepted by Slack
- Payload visible and clickable in the edited post

### Step 3: Alternative Payload Injection via Clipboard
procedure: [[procedures/Inject-XSS-Payload-via-Clipboard-Manipulation]]

**Objective**: Use clipboard injection to insert the payload without relying on WebSocket interception.

**Instructions**: Create a file 'chromium' with JSON payload including the malicious link, then execute [[commands/set-chromium-clipboard-payload]] to set the clipboard with org.chromium.web-custom-data UTI. Paste into the Slack post editor.

```python
from AppKit import NSPasteboard, NSData
uti = "org.chromium.web-custom-data"
chromium = open('chromium').read()
pb = NSPasteboard.generalPasteboard()
pb.clearContents()
pb.declareTypes_owner_([uti], None)
data = NSData.dataWithBytes_length_(chromium, len(chromium))
pb.setData_forType_(data, uti)
```

**Expected Output**: Paste inserts a failed unfurl with the javascript: link.

**Success Indicators**:
- Clipboard set successfully
- Malicious link appears on paste

### Step 4: Propagation to Team Members
procedure: [[procedures/Enable-Editing-Permissions-to-Affect-Team-Members]]

**Objective**: Share the post with editing enabled to trick team members into clicking the payload.

**Instructions**: In the post settings, enable 'Let others edit this Post' and share the link. Wait for a team member to edit and interact with the link.

**Expected Output**: Team member sees and clicks the link during editing, triggering script execution.

**Success Indicators**:
- Post shared with edit permissions
- Victim interacts and alert pops up

### Step 5: iOS Exploitation for File Access
procedure: [[procedures/Exploit-XSS-on-iOS-to-Read-Local-Files]]

**Objective**: Leverage the XSS on iOS Slack app to bypass SOP and read local files.

**Instructions**: Insert the same javascript: payload in an iOS-editable post, load external JS via the URI, and use it to read files like `/etc/passwd`.

**Expected Output**: Script executes and displays file contents in an alert or console.

**Success Indicators**:
- No SOP enforcement on iOS
- Local file contents retrieved

## Attack Chain Summary

### Key Achievements

1. Discovered and exploited unvalidated javascript: URIs in Slack's editing mode
2. Inserted payloads via WebSocket and clipboard methods for reliability
3. Propagated to team members via shared editing, achieving domain-context execution
4. Extended impact on iOS to local file disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01*
