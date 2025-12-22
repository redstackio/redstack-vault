---
tags:
  - path-traversal
  - rce
  - android
  - evernote
  - mobile-exploitation
  - library-hijacking
type: attack_chain
tools:
  - '[[tools/ADB]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-Malicious-Library-to-Evernote-Note]]'
  - '[[procedures/Rename-Attachment-with-Path-Traversal]]'
  - '[[procedures/Share-Note-via-Invitation-and-Link]]'
  - '[[procedures/Trigger-Download-via-Victim-Interaction]]'
  - '[[procedures/Restart-App-to-Execute-Malicious-Library]]'
  - '[[procedures/Connect-to-Reverse-Shell]]'
step_count: 6
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
updated_at: '2025-12-14T17:24:43.000Z'
description: >-
  A multi-stage attack exploiting path traversal in the Evernote Android app to
  overwrite a native library and achieve remote code execution upon app restart.
skill_level: intermediate
impact_level: high
id: d501986a-3bdf-4569-a36e-bb949b349b4f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
---
# Path Traversal in Evernote Android Attachment Download Leading to RCE via Library Overwrite

Multi-stage attack chain demonstrating a complete attack workflow exploiting a path traversal vulnerability in the Evernote Android app's attachment handling to achieve remote code execution on the victim's device.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Malicious Library] --> B[Rename with Traversal]
    B --> C[Share Note Link]
    C --> D[Victim Opens and Clicks]
    D --> E[App Restart Triggers Load]
    E --> F[Connect Reverse Shell]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ADB]]
- [[tools/nc]]

### Target Environment

- Android device with Evernote app installed (vulnerable version)
- ARM64 architecture for the malicious library
- Physical access to attacker's device for ADB setup
- Port 6666 open for netcat listener

### Initial Access Requirements

- Attacker account in Evernote
- Victim's email for note invitation
- No prior credentials on victim side; relies on social engineering via shared link

## Detailed Attack Procedures

### Step 1: Upload Malicious Library
procedure: [[procedures/Upload-Malicious-Library-to-Evernote-Note]]

**Objective**: Prepare and attach a malicious native library to an Evernote note to serve as the payload for later exploitation.

**Instructions**: Compile or obtain a malicious `libjnigraphics.so` library for ARM64 that includes reverse shell code connecting to localhost:6666. Upload it as an attachment to a new note in the Evernote Android app.

**Expected Output**: The file is successfully attached to the note with a default filename.

**Success Indicators**:
- Attachment visible in the note
- File size and type match the uploaded library

### Step 2: Rename Attachment with Path Traversal
procedure: [[procedures/Rename-Attachment-with-Path-Traversal]]

**Objective**: Modify the attachment filename to include path traversal sequences, enabling the file to be written to a sensitive directory during download.

**Instructions**: In the note editor, rename the attachment to `../../../lib-1/libjnigraphics` (the `.so` extension is preserved internally). The app does not restrict special characters like `../`.

**Expected Output**: Filename updated in the note; no errors from the app.

**Success Indicators**:
- Renamed filename displays correctly in the note
- Traversal path is accepted without sanitization

### Step 3: Share Note via Invitation and Link
procedure: [[procedures/Share-Note-via-Invitation-and-Link]]

**Objective**: Invite the victim to the note and generate a shareable link to facilitate initial access.

**Instructions**: Invite the victim's email to the note. Then, access the share options: tap the three dots, select "Copy internal link" or "Copy web link" to generate an Android deeplink.

**Expected Output**: Invitation sent; shareable link copied to clipboard.

**Success Indicators**:
- Victim receives invitation email
- Deeplink is valid and testable

### Step 4: Trigger Download via Victim Interaction
procedure: [[procedures/Trigger-Download-via-Victim-Interaction]]

**Objective**: Lure the victim to open the shared note and click the attachment, triggering the unsanitized download to the sensitive path.

**Instructions**: Send the deeplink to the victim (e.g., via email or messaging). Victim opens the link (first click), accesses the note, and clicks the attachment (second click). This extracts the filename from the Content-Disposition header and writes to `/data/data/com.evernote/lib-1/libjnigraphics.so`.

**Expected Output**: File downloaded and overwritten in the app's lib directory instead of cache.

**Success Indicators**:
- Victim confirms note access
- No download errors; file appears processed

### Step 5: Restart App to Execute Malicious Library
procedure: [[procedures/Restart-App-to-Execute-Malicious-Library]]

**Objective**: Force the app to reload and execute the overwritten malicious library, initiating the reverse shell.

**Instructions**: Instruct the victim to close and reopen the Evernote app. Upon restart, the app loads the tampered `libjnigraphics.so`, executing the payload.

**Expected Output**: Malicious code runs silently, attempting connection to the listener.

**Success Indicators**:
- App restarts without crash
- No immediate alerts from the device

### Step 6: Connect to Reverse Shell
procedure: [[procedures/Connect-to-Reverse-Shell]]

**Objective**: Capture the incoming reverse shell connection from the exploited device.

**Instructions**: Use ADB to access the device shell and run the netcat listener with [[commands/nc-reverse-shell-listener]]:

```bash
adb shell
nc 127.0.0.1 6666
```

**Expected Output**: Incoming connection establishes a shell session.

**Success Indicators**:
- Reverse shell prompt appears
- Commands executable on victim device

## Attack Chain Summary

### Key Achievements

1. Successful path traversal to overwrite sensitive app library
2. Two-click social engineering to trigger exploitation without authentication
3. Remote code execution on Android device via native library hijacking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Dynamic Linker Hijacking]] Dynamic-link Library Injection

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
