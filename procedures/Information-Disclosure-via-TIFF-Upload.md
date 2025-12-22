---
tags:
  - info-disclosure
  - tiff
  - graphicsmagick
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ae9a3822-70e4-47de-abe3-6fc2f3b34a0d
created_at: '2025-12-14T03:46:14.342Z'
updated_at: '2025-12-14T03:46:14.342Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Information Disclosure via TIFF Upload

## Summary

Uploads TIFF content as PNG to leak GraphicsMagick version and temp path during conversion.

## Description

Server converts uploaded TIFF (sent as image/png) using GraphicsMagick, embedding comment with /tmp path and version (1.4 snapshot-20160531).

## Requirements

1. TIFF file

## Defense

- Strip metadata in conversions
- Sanitize temp paths

## Objectives

1. Extract version/path

## Instructions

### Step 1: Create TIFF Payload

**Context**: Save TIFF as .png.

Content-Type: image/png, body: TIFF data.

### Step 2: Upload and Download

**Context**: Process and inspect result.

Upload; download converted file, check TIFF comment.

> Reveals /tmp/gmi7JIsA and version.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[leak]]
