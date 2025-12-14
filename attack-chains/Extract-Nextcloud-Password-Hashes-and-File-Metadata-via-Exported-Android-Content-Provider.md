---
tags:
  - android
  - information-disclosure
  - content-provider
  - nextcloud
  - credential-access
type: attack_chain
tools:
  - '[[tools/Android-Debug-Bridge]]'
  - '[[tools/Content-Provider-Helper]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-and-Authenticate-Nextcloud-Android-App]]'
  - '[[procedures/Establish-ADB-Connection-to-Device]]'
  - '[[procedures/Query-Shares-Content-Provider-for-Hashes]]'
  - '[[procedures/Query-File-and-Directory-Providers-for-Metadata]]'
  - '[[procedures/Exploit-Provider-Using-Content-Provider-Helper-App]]'
step_count: 5
techniques:
  - '[[T1420]]'
  - '[[Credentials from Password Stores]]'
updated_at: '2025-12-14T17:24:40.110Z'
description: >-
  Multi-stage attack exploiting an exported Content Provider in the Nextcloud
  Android app to disclose bcrypt password hashes for protected shares and
  sensitive file metadata, enabling offline cracking and unauthorized access.
skill_level: intermediate
impact_level: high
id: 7c6599b5-1f7a-4515-a84f-eb3420c2295d
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[T1420]]'
  - '[[Credentials from Password Stores]]'
---
# Extract Nextcloud Password Hashes and File Metadata via Exported Android Content Provider

Multi-stage attack chain demonstrating exploitation of an exported Content Provider in the Nextcloud Android client (v1.4.3) to extract bcrypt password hashes and share tokens for password-protected files and folders, as well as synced file and directory metadata. This allows a malicious app or attacker with device access to perform offline cracking, bypassing server-side protections and potentially gaining unauthorized access to shares.

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
    A[App Installation and Authentication] --> B[ADB Setup and Shell Access]
    B --> C[Query Shares Provider]
    C --> D[Query File/Dir Providers]
    D --> E[Alternative App-Based Query]
    E --> F[Offline Cracking and Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#1abc9c
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Android-Debug-Bridge]]
- [[tools/Content-Provider-Helper]]

### Target Environment

- Android device (API level supporting Nextcloud app v1.4.3)
- Nextcloud server with password-protected shares
- USB debugging enabled on device

### Initial Access Requirements

- Physical or ADB access to the Android device
- Nextcloud account credentials for app authentication
- No network access to server required post-setup; local exploitation

## Detailed Attack Procedures

### Step 1: App Installation and Authentication
procedure: [[procedures/Install-and-Authenticate-Nextcloud-Android-App]]

**Objective**: Install the vulnerable Nextcloud app and populate local storage with sensitive share data by creating password-protected shares.

**Instructions**: Download and install the Nextcloud Android app (v1.4.3) from the Play Store or APK source. Sign in with valid credentials and ensure password-protected shares exist on the server to sync hashes and tokens locally.

**Expected Output**: App authenticates successfully; shares sync to device, making data available via Content Provider.

**Success Indicators**:
- App login confirmed
- Password-protected shares visible in app

### Step 2: Establish ADB Connection
procedure: [[procedures/Establish-ADB-Connection-to-Device]]

**Objective**: Gain shell access to the Android device via ADB for querying local Content Providers.

**Instructions**: Enable USB debugging in device settings, connect via USB to a computer with ADB installed. List devices using [[commands/list-adb-devices]]:

```bash
adb devices
```

Then open shell with [[commands/open-adb-shell]]:

```bash
adb shell
```

**Expected Output**: Device listed as connected; shell prompt appears.

**Success Indicators**:
- Device serial shown in output
- Shell access granted without errors

### Step 3: Query Shares Provider
procedure: [[procedures/Query-Shares-Content-Provider-for-Hashes]]

**Objective**: Extract bcrypt hashes and share tokens from the exported shares provider.

**Instructions**: In the ADB shell, query the provider using [[commands/query-content-provider-shares]]:

```bash
content query --uri content://org.nextcloud/shares
```

Review output for 'share_with' (hashes) and 'token' fields.

**Expected Output**: Table rows showing share data, including hashed passwords for protected shares.

**Success Indicators**:
- Hashes visible in 'share_with' column
- Tokens listed for shares

### Step 4: Query File and Directory Providers
procedure: [[procedures/Query-File-and-Directory-Providers-for-Metadata]]

**Objective**: Leak synced file names and folder structures via additional exported providers.

**Instructions**: Still in ADB shell, query files with [[commands/query-content-provider-files]]:

```bash
content query --uri content://org.nextcloud/file
```

For directories, use [[commands/query-content-provider-directory]] (replace [dir ID] with actual ID from prior queries):

```bash
content query --uri content://org.nextcloud/dir/[dir ID]
```

**Expected Output**: Lists of file names and directory contents.

**Success Indicators**:
- File metadata exposed
- Folder names revealed

### Step 5: Alternative App-Based Exploitation
procedure: [[procedures/Exploit-Provider-Using-Content-Provider-Helper-App]]

**Objective**: Demonstrate access by a malicious app without ADB, using a third-party query tool.

**Instructions**: Install [[tools/Content-Provider-Helper]] on the device, add URI 'content://org.nextcloud/shares', and query.

**Expected Output**: App displays share data, including hashes.

**Success Indicators**:
- Data visible in third-party app
- No authentication required

## Attack Chain Summary

### Key Achievements

1. Exposed bcrypt hashes for offline cracking
2. Leaked share tokens and file metadata
3. Bypassed server protections via local access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1420]] File and Directory Discovery
- [[Credentials from Password Stores]] Credentials from Password Stores

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

---

*Last updated: 2024-10-01T00:00:00Z*
