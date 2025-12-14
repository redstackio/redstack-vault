---
tags:
  - recon
  - mime-type
  - mimemagic
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:16:02.466Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 8633dea4-b485-4f31-98fa-9af7c32ca388
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Review-mimemagic-MIME-Type-Mappings-for-mml

## Summary

This procedure involves inspecting the mimemagic library to confirm that .mml file extensions are mapped to application/mathml+xml, enabling potential XSS via MathML rendering in browsers.

## Description

In Ruby on Rails Active Storage, MIME types are determined using the Marcel gem, which relies on mimemagic. When magic bytes fail to identify a file, it falls back to extension-based detection. The mimemagic library explicitly maps .mml to application/mathml+xml at line 3872 in tables.rb. This MIME type causes Firefox to render MathML content, which supports JavaScript execution through href attributes, leading to stored XSS if malicious files are uploaded and viewed.

## Requirements

1. Access to the mimemagic GitHub repository or local installation
2. Basic knowledge of Ruby gems and MIME type handling
3. Text editor or browser for code review

## Defense

Defensive measures and detection strategies:

- Update mimemagic to latest version and validate MIME mappings
- Implement strict MIME type whitelisting in Active Storage
- Scan uploads for executable content beyond MIME detection

## Objectives

1. Confirm .mml MIME type vulnerability
2. Understand fallback detection mechanism
3. Identify browser-specific rendering risks

## Instructions

### Step 1: Access mimemagic Source Code

**Context**: Locate the relevant mapping in the library to verify the extension-based MIME assignment.

Navigate to https://github.com/minad/mimemagic/blob/master/lib/mimemagic/tables.rb and search for line 3872 or the 'mml' extension.

> The code shows: 'mml' => 'application/mathml+xml'. This confirms the mapping without magic byte checks for plain text MathML files.

### Step 2: Analyze Implications

**Context**: Evaluate how this affects Rails Active Storage.

Review Marcel::MimeType.for documentation to understand fallback to extension when magic detection fails on non-binary files.

> Expected: Files saved as .mml will be served with application/mathml+xml, triggering MathML parser in supporting browsers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- mime-type
- mimemagic
