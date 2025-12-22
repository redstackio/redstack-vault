---
id: proc-003
tags:
  - harvesting
  - information-disclosure
  - privacy
type: procedure
tools:
  - '[[tools/Burp-Suite-Repeater]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:12.687Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-Emails-from-Responses

## Summary

This procedure focuses on parsing and collecting email addresses disclosed in HTTP responses from valid user_id queries, completing the enumeration attack by compiling a dataset of user information.

## Description

Following successful ID bruteforcing, responses from the Manage Users endpoint on staging.seatme.us include email fields in JSON or HTML. This step manually extracts them, highlighting the privacy impact of the disclosure. The scenario assumes web access; outcomes include a harvested list for potential misuse like targeting.

## Requirements

1. Valid responses from prior bruteforcing steps
2. Text editor or spreadsheet for logging
3. Burp Repeater for response viewing

## Defense

Defensive measures and detection strategies:

- Sanitize responses to exclude sensitive fields like emails
- Enable CORS and content security policies
- Monitor for bulk data extraction attempts

## Objectives

1. Identify email data in responses
2. Compile and store extracted information
3. Assess the scale of disclosure

## Instructions

### Step 1: Inspect Response Content

**Context**: Review raw responses for email exposure.

In Burp Repeater, examine the response body for each valid user_id (e.g., search for 'email' key in JSON).

> Expected output: Emails visible, e.g., {"user_id":514755, "email":"user@example.com"}.

### Step 2: Log and Harvest Emails

**Context**: Systematically collect data from multiple responses.

Copy emails from valid responses into a log file, associating with user_ids for completeness.

> Expected output: A growing list of emails, demonstrating easy harvesting without controls.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Repeater]]

## Tags

- [[harvesting]]
- [[information-disclosure]]
- [[privacy]]
