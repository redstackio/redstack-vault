---
id: proc-generate-file-001
tags:
  - payload
  - gibberish
  - file-generation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ls-list-files]]'
  - '[[commands/head-display-file-content]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:32:01.425Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Generate-Large-Gibberish-File

## Summary

This procedure generates a ~1MB file filled with lorem ipsum text to serve as a large payload for secret resources, simulating oversized data that will trigger resource exhaustion when processed by the webhook.

## Description

For the DoS attack, large resources (~1MB secrets) are needed to overwhelm the API Server during concurrent webhook calls. A lorem ipsum generator creates dummy text, saved as lorem-1MB. Commands verify the file size and content. This can be done on the bastion VM or any Linux host with access to the cluster.

## Requirements

1. Linux environment with basic text tools
2. Lorem ipsum generator (e.g., online tool or script)
3. ~1MB disk space

## Defense

Defensive measures and detection strategies:

- Enforce resource quotas on secrets (e.g., size limits via admission controllers)
- Monitor for large object creations in API audit logs
- Use validating webhooks to reject oversized payloads

## Objectives

1. Produce a 1MB dummy file for payload
2. Verify file integrity and size
3. Prepare for secret creation

## Instructions

### Step 1: Generate the File

**Context**: Use a generator to create the large text file.

**Command** ([[commands/lorem-generate]]):
```bash
# Assuming a lorem tool or dd for simulation
for i in {1..10000}; do echo "Lorem ipsum dolor sit amet, consectetur adipiscing elit." >> lorem-1MB; done
# Or use online generator and download
```

> Builds file; expected output: File grows to ~1MB.

### Step 2: List and Verify Size

**Context**: Check file details with long listing.

**Command** ([[commands/ls-list-files]]):
```bash
ls -alh
```

> Lists files; expected output: lorem-1MB 990K.

### Step 3: Inspect Content

**Context**: View first lines to confirm gibberish.

**Command** ([[commands/head-display-file-content]]):
```bash
head lorem-1MB
```

> Shows head; expected output: Lorem ipsum dolor sit amet...

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer (Payload Preparation)

### Sub-Techniques


## Commands Used

- [[commands/ls-list-files]]
- [[commands/head-display-file-content]]
- [[commands/lorem-generate]]

## Tools Used


## Tags

- payload
- gibberish
- file-generation
