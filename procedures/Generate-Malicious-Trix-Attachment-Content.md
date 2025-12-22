---
tags:
  - xss
  - payload-generation
  - trix-editor
type: procedure
tools:
  - '[[tools/Browser]]'
  - '[[tools/Trix-Editor]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d566a8cf-5f05-481b-bdf9-d6f3fde9aa5d
created_at: '2025-12-13T23:55:06.251Z'
updated_at: '2025-12-13T23:55:06.251Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Generate-Malicious-Trix-Attachment-Content

## Summary

This procedure creates a copyable HTML div element containing a data-trix-attachment with malicious content, specifically an img tag that uses an onerror event to execute JavaScript, targeting the sanitization flaw in Trix editor 2.1.1.

## Description

In the context of exploiting stored XSS in Trix editor, this step involves crafting an HTML demo page that loads the vulnerable Trix library and dynamically generates a div with embedded malicious data. The attachment mimics a file upload but includes an HTML snippet with <img src="1" onerror="alert(document.domain)">, which fails to load and triggers the script. This is pasted later to store the payload in the editor. Prerequisites include a modern browser and access to the Trix CDN. Expected outcome is a clipboard-ready payload that evades initial checks.

## Requirements

1. Modern web browser (e.g., Chrome, Firefox) for running HTML
2. Internet access to load Trix editor from CDN
3. Basic HTML/JavaScript knowledge to modify the demo if needed

## Defense

Defensive measures and detection strategies:

- Update Trix editor to version 2.1.2 or later with fixed sanitization
- Implement client-side content security policy (CSP) to block inline scripts
- Monitor for anomalous paste events or attachment uploads in application logs

## Objectives

1. Produce a valid data-trix-attachment that embeds executable HTML
2. Ensure the payload is copyable without altering its structure
3. Prepare for seamless integration into target editor instances

## Instructions

### Step 1: Create and Load HTML Demo

**Context**: Build a simple HTML file that initializes Trix and generates the malicious div using document.write for dynamic insertion.

The HTML structure includes:
- Script tag loading Trix from https://cdn.jsdelivr.net/npm/trix@2.1.1/dist/trix.umd.min.js
- A div with id for the editor
- JavaScript to write the malicious div: <div data-trix-attachment="{&quot;contentType&quot;:&quot;text/html5&quot;,&quot;details&quot;:{&quot;file&quot;:{&quot;href&quot;:&quot;data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=&quot;}},&quot;file&quot;:{&quot;url&quot;:&quot;data:&quot;}}" contenteditable="false"><img src="1" onerror="alert(document.domain)"></div>

Save as demo.html and open in browser.

**Expected Output**: Trix editor loads, and a copyable div appears with the malicious img.

### Step 2: Copy the Malicious Div

**Context**: Select and copy the generated div to the clipboard for pasting.

Click any 'copy me' element or manually select the div and copy (Ctrl+C).

**Expected Output**: Content is in clipboard, verifiable by pasting into a text editor to see the data-trix-attachment attribute.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Trix-Editor]]
- [[tools/Browser]]

## Tags

- [[xss]]
- [[payload-generation]]
