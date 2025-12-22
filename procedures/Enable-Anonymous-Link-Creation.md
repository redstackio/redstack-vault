---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - web
  - anonymous-access
  - adobe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:53.012Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable Anonymous Link Creation

## Summary

This procedure configures the Adobe file sharing to generate an anonymous link, allowing the stored XSS payload to execute on unauthenticated victims without requiring Adobe login.

## Description

As part of the stored XSS attack on files.acrobat.com, enabling anonymous link creation bypasses authentication checks, ensuring the malicious description renders for any viewer. This targets the https://cloud.acrobat.com/send endpoint. Prerequisites include having a file selected in the interface. Successful execution results in the sharing options reflecting anonymous access.

## Requirements

1. Access to the file send page with a file selected
2. Web browser session
3. No additional credentials beyond initial login

## Defense

Defensive measures and detection strategies:

- Enforce authentication for all sharing links
- Log and alert on anonymous link creations exceeding thresholds

## Objectives

1. Configure sharing for anonymous access
2. Prepare link for broad victim targeting
3. Avoid authentication barriers for payload delivery

## Instructions

### Step 1: Locate Anonymous Option

**Context**: Identify the setting that allows unauthenticated sharing.

On the send page, scroll to the link options section.

> The page displays various sharing modes, including authenticated and anonymous.

### Step 2: Activate Anonymous Link

**Context**: Enable the feature to generate public links.

Check the box labeled 'Create Anonymous Link'.

> This updates the form to indicate no login required for link access, confirming setup for XSS impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- anonymous-access
