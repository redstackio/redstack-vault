---
tags:
  - setup
  - payload-prep
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.930Z'
sub_techniques: []
id: cd438ab5-4b37-490a-bf1a-33e1c4b2abaf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enter-Random-Birth-Date

## Summary

This procedure populates the birth date fields with arbitrary values to increase the chances of matching existing user records during SQL injection, enabling unauthorized data access.

## Description

The application likely queries the database using SSN and birth date for authentication. Entering a common or random birth date (e.g., January 1, 1990) can align with other users' data when combined with an SQL payload, leading to login as that user. This step is non-technical and prepares for injection.

## Requirements

1. Form loaded with birth date fields (day, month, year)
2. No tools beyond browser

## Defense

Defensive measures and detection strategies:

- Rate limiting on form submissions
- Validate birth dates against realistic ranges

## Objectives

1. Set up matching criteria for injection success
2. Avoid triggering immediate errors
3. Enable cross-user data access

## Instructions

### Step 1: Select Birth Date Values

**Context**: Choose arbitrary but plausible birth date components in the form fields.

Browser form input:

```plaintext
Month: January
Day: 1
Year: 1990
```

> Fields are typically dropdowns or text inputs; select values that might exist in the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[payload-prep]]
