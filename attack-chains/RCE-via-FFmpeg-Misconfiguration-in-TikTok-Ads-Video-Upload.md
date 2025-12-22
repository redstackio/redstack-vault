---
id: ac-uuid-1
name: RCE via FFmpeg Misconfiguration in TikTok Ads Video Upload
tags:
  - rce
  - ffmpeg
  - video-upload
  - tiktok
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-FFmpeg-RCE-in-Video-Upload]]'
  - '[[procedures/Exploit-FFmpeg-for-RCE]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:24:14.656Z'
description: >-
  Multi-stage attack exploiting a misconfiguration in FFmpeg for video
  processing in the TikTok Ads portal, leading to remote code execution and root
  access on the server.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# RCE via FFmpeg Misconfiguration in TikTok Ads Video Upload

Multi-stage attack chain demonstrating a complete attack workflow exploiting FFmpeg misconfiguration in the TikTok Ads portal's video upload endpoint, resulting in remote code execution and root access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Vulnerability] --> B[Exploitation and Execution]
    B --> C[System Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on standard web browser and command injection via upload)

### Target Environment

- Web platform with video upload functionality
- FFmpeg installed for video processing
- Access to TikTok Ads portal

### Initial Access Requirements

- Valid user account in TikTok Ads portal
- Network access to the video upload endpoint
- No prior privileged access needed

## Detailed Attack Procedures

### Step 1: Discovery of RCE Vulnerability
procedure: [[procedures/Discover-FFmpeg-RCE-in-Video-Upload]]

**Objective**: Identify the misconfiguration in FFmpeg during the video creation/upload process that allows command injection.

**Instructions**: Analyze the video upload endpoint in the TikTok Ads portal. Test uploads with specially crafted filenames or parameters that FFmpeg processes, such as including shell metacharacters (e.g., `; id`) in the filename to inject commands. Monitor server responses for signs of execution, like error messages or unexpected behaviors.

**Expected Output**: Confirmation of command injection, such as partial output from injected commands in error logs or responses.

**Success Indicators**:
- Server processes the injected command without proper sanitization
- Evidence of command execution in upload feedback

### Step 2: Exploitation for Remote Code Execution
procedure: [[procedures/Exploit-FFmpeg-for-RCE]]

**Objective**: Leverage the FFmpeg misconfiguration to execute arbitrary system commands, achieving root access and system compromise.

**Instructions**: Upload a video file with a malicious filename or metadata that triggers FFmpeg to execute injected commands, such as `$(id)` or `; ls`. Once RCE is confirmed, chain commands to explore the system. For verification, inject and execute [[commands/id]] to check privileges:

```bash
; id
```

Then use [[commands/ls]] to list directory contents:

```bash
; ls
```

**Expected Output**: Output from commands, e.g., `uid=0(root) gid=0(root)` for id, confirming root access; directory listing for ls.

**Success Indicators**:
- Root privileges confirmed via id output
- Filesystem exploration successful via ls
- Full system compromise achieved

## Attack Chain Summary

### Key Achievements

1. Identified FFmpeg misconfiguration enabling RCE in video processing
2. Executed arbitrary commands as root on the server
3. Demonstrated full system compromise through basic reconnaissance commands

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
