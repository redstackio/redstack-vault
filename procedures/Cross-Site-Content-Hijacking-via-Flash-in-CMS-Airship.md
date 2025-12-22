---
id: proc-uuid-004
name: Cross-Site-Content-Hijacking-via-Flash-in-CMS-Airship
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.827Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Windows Command Shell]]'
tags:
  - flash-hijacking
  - cross-site
platforms:
  - Web
tools:
  - '[[tools/CrossSiteContentHijacking]]'
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---

# Cross-Site-Content-Hijacking-via-Flash-in-CMS-Airship

## Summary

This procedure uploads SWF Flash files to CMS Airship, exploiting missing Content-Disposition headers to allow embedding or loading in other contexts, enabling cross-site requests to steal site content in browsers like Chrome.

## Description

PublicFiles.php serves uploaded SWF files without attachment headers, permitting them to be loaded cross-origin via Flash, hijacking content from the target domain. Mitigated by adding proper headers; useful for data theft in legacy Flash-enabled environments.

## Requirements

1. Authenticated access to upload SWF files
2. Tool to generate or obtain malicious SWF
3. Target site with Flash support

## Defense

Defensive measures and detection strategies:

- Ban SWF uploads or serve with Content-Disposition: attachment
- Disable Flash in browsers
- Monitor cross-origin requests from Flash

## Objectives

1. Upload SWF for cross-site loading
2. Steal content via Flash requests
3. Exfiltrate data to attacker

## Instructions

### Step 1: Prepare SWF File

**Context**: Use [[tools/CrossSiteContentHijacking]] to create a demo SWF that loads cross-site content.

Follow tool docs to generate swf_file.swf targeting the site's resources.

> Expected: Valid SWF binary.

### Step 2: Upload and Test

**Context**: Upload via CMS and attempt embedding in another page.

Use browser to load <embed src="https://target.com/files/swf_file.swf"> and check for content theft.

> Expected output: SWF executes and fetches restricted content cross-site.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/CrossSiteContentHijacking]]

## Tags

- [[flash-hijacking]]
- [[cross-site]]
