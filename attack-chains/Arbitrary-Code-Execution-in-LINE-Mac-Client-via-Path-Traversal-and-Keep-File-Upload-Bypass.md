---
id: ac-line-mac-rce-001
tags:
  - path-traversal
  - rce
  - file-upload-bypass
  - macos
  - line-app
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - macOS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-Malicious-Terminal-File-to-LINE-Keep]]'
  - '[[procedures/Share-Terminal-File-via-LINE]]'
  - '[[procedures/Craft-Zip-with-Path-Traversal-Payload]]'
  - '[[procedures/Trigger-Execution-via-Zip-Handling]]'
step_count: 6
techniques:
  - '[[Malicious File]]'
  - '[[Remote File Copy]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:29.942Z'
description: >-
  A multi-stage attack exploiting file upload restrictions in LINE's Keep
  service and path traversal in the Mac client's zip filename parsing to deliver
  and execute malicious .terminal files, achieving arbitrary code execution on
  macOS if Gatekeeper is disabled.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Malicious File]]'
  - '[[Remote File Copy]]'
  - '[[File and Directory Discovery]]'
---
# Arbitrary Code Execution in LINE Mac Client via Path Traversal and Keep File Upload Bypass

Multi-stage attack chain demonstrating a complete attack workflow exploiting vulnerabilities in the LINE Mac client and Keep service to achieve remote code execution on victim machines.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Malicious File to Keep] --> B[Share File with Victim]
    B --> C[Victim Downloads File]
    C --> D[Craft and Send Malicious Zip]
    D --> E[Victim Clicks Zip]
    E --> F[Arbitrary Code Execution]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- No specialized tools required; uses built-in LINE app features and standard macOS zip creation.

### Target Environment

- macOS (LINE Mac client version vulnerable to the issue, e.g., pre-patch versions)
- LINE app with Keep service enabled
- Victim with Gatekeeper disabled or bypassed

### Initial Access Requirements

- Attacker account in LINE
- Victim using LINE Mac client
- Social engineering to get victim to download and interact with files

## Detailed Attack Procedures

### Step 1: Upload Malicious .terminal File to Keep

procedure: [[procedures/Upload-Malicious-Terminal-File-to-LINE-Keep]]

**Objective**: Bypass file upload restrictions in LINE's Keep service to store a malicious executable .terminal file.

**Instructions**: Create a .terminal file with desired executable commands (e.g., using TextEdit or terminal to save as .terminal with base64-encoded commands for execution). Upload it directly via the Keep feature in the LINE app, exploiting the incomplete extension blacklist that allows .terminal files.

**Expected Output**: File successfully uploaded to Keep storage without rejection.

**Success Indicators**:
- Upload confirmation in LINE Keep
- File visible in attacker's Keep library

### Step 2: Share .terminal File with Victim from Keep

procedure: [[procedures/Share-Terminal-File-via-LINE]]

**Objective**: Deliver the malicious file to the victim via LINE's sharing mechanism, bypassing executable restrictions.

**Instructions**: From the Keep interface in LINE, select the uploaded .terminal file and use the share feature to send it to the target victim's LINE chat.

**Expected Output**: File shared successfully in the chat, appearing as a downloadable attachment.

**Success Indicators**:
- Victim receives the file notification
- File downloadable from the chat

### Step 3: Victim Downloads Shared File

**Objective**: Ensure the malicious .terminal file lands in the victim's Downloads directory.

**Instructions**: The victim must interact with the LINE message by clicking to download the shared .terminal file, which saves to ~/Downloads by default in the LINE Mac client.

**Expected Output**: .terminal file present in victim's ~/Downloads folder.

**Success Indicators**:
- File appears in Downloads
- No immediate execution (requires next steps)

### Step 4: Send Malicious .zip File with Path Traversal Vulnerability

procedure: [[procedures/Craft-Zip-with-Path-Traversal-Payload]]

**Objective**: Craft and send a zip file with a filename that exploits path traversal to target the downloaded .terminal file.

**Instructions**: Create a zip file using macOS Terminal or Finder, naming it with a traversal payload like '..%2f..%2f..%2f..%2f..%2f..%2f..%2fDownloads%2fmalicious.terminal#.zip' (using %2f for / and # to block extension parsing). Send this zip via LINE chat to the victim.

**Expected Output**: Zip file received and visible in victim's LINE chat.

**Success Indicators**:
- Zip file downloadable
- Filename payload intact upon receipt

### Step 5: Victim Clicks .zip File

procedure: [[procedures/Trigger-Execution-via-Zip-Handling]]

**Objective**: Trigger the LINE Mac client's faulty filename parsing to resolve the traversal path.

**Instructions**: The victim clicks on the received zip file in the LINE Mac client, causing the app to parse the filename and attempt to handle it, navigating outside the intended directory via the traversal sequence.

**Expected Output**: LINE app processes the zip, resolving to the target .terminal file path.

**Success Indicators**:
- No zip extraction error
- App attempts to launch the resolved path

### Step 6: Code is Executed

procedure: [[procedures/Trigger-Execution-via-Zip-Handling]]

**Objective**: Achieve arbitrary code execution by launching the .terminal file.

**Instructions**: Upon path resolution, the LINE client executes the .terminal file from ~/Downloads, running the embedded commands (e.g., launching Calculator.app or custom payload) if Gatekeeper is disabled.

**Expected Output**: Target application or payload executes on victim's machine.

**Success Indicators**:
- Evidence of execution (e.g., app launch, system changes)
- No Gatekeeper block

## Attack Chain Summary

### Key Achievements

1. Bypassed LINE's executable upload filters using .terminal extension
2. Delivered malicious file via Keep sharing without detection
3. Exploited path traversal in zip handling for out-of-directory execution
4. Achieved RCE on macOS without additional privileges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Malicious File]] User Execution: Malicious File
- [[Remote File Copy]] Ingress Tool Transfer
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
