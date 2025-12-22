---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - information-disclosure
  - error-handling
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T05:32:10.060Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Capture-Error-Response-for-Path-Disclosure

## Summary

This procedure involves inspecting the JSON error response from the failed SVG upload to extract leaked internal server file paths.

## Description

Upon rmagick failure, the Ruby on Rails application returns a JSON error including the full temporary path (e.g., /var/app/current/tmp/uploads/...) due to poor error sanitization. This discloses deployment details like AWS Elastic Beanstalk structure, aiding attackers in mapping the filesystem for further reconnaissance or exploits.

## Requirements

1. Failed upload from previous step
2. Browser with network inspection capabilities (e.g., DevTools)
3. Knowledge of JSON parsing for error details

## Defense

Defensive measures and detection strategies:

- Sanitize error messages to remove paths and sensitive details
- Use custom error handlers in rmagick integration
- Monitor logs for path exposures and implement web application firewall rules

## Objectives

1. Identify leaked filesystem information
2. Document paths for reconnaissance
3. Assess potential for chained attacks

## Instructions

### Step 1: Open Developer Tools

**Context**: Prepare to capture the response.

In the browser, open DevTools (F12) and go to the Network tab before submitting the upload.

### Step 2: Re-trigger the Upload if Needed

**Context**: Ensure the error is generated.

Repeat the SVG URL submission if the response wasn't captured.

### Step 3: Inspect JSON Response

**Context**: Analyze for path details.

Locate the failed request (e.g., POST to /upload endpoint), view the response, and search for rmagick error strings containing absolute paths like /var/app/current/tmp/....

**Expected Output**: Error JSON with details such as {"error": "rmagick failed at /var/app/current/tmp/uploads/abc123/def.svg"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- error-handling
- reconnaissance
