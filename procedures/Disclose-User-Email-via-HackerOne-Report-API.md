---
id: proc-001
tags:
  - information-disclosure
  - api-abuse
  - email-leak
  - hackerone
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-hackerone-report-fetch]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:48.502Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Disclose-User-Email-via-HackerOne-Report-API

## Summary

This procedure exploits an information disclosure vulnerability in the HackerOne API, allowing an authenticated attacker to retrieve any user's private email address by inviting them as a participant to a report in a controlled program and then fetching the report details via API. The email is exposed in the activities data without any redaction or access controls, enabling de-anonymization and potential mass collection of user data.

## Description

The attack targets the HackerOne platform's report management API (/v1/reports/{report_id}), where inviting a user by username to a report includes their private email in the subsequent API response under activities.data.attributes.email. This occurs because the invitation activity logs the email without proper privacy controls. The scenario requires a HackerOne account with program access (e.g., sandbox) and knowledge of the victim's public username. Outcomes include direct access to private emails, which can lead to phishing, spam, or further social engineering. Prerequisites include authenticated API access; no victim interaction is needed, making it highly efficient for enumeration.

## Requirements

1. Valid HackerOne account with access to a program allowing report creation/invitation (e.g., sandbox program)
2. Target victim's public username (discoverable via HackerOne sitemap or user profiles)
3. API token with read permissions for reports
4. Command-line tool like curl for API requests

## Defense

Defensive measures and detection strategies:

- Implement strict access controls on API responses to redact private fields like emails for non-owners
- Audit invitation activities and API calls for anomalous patterns (e.g., mass invitations to reports)
- Monitor for unusual API token usage or report participant additions from low-privilege accounts
- Educate users on privacy settings and limit public username exposure

## Objectives

1. Expose private email of any HackerOne user without consent or interaction
2. Enable mass enumeration of user emails using public usernames
3. De-anonymize users for further attacks like targeted phishing
4. Demonstrate API privacy flaw in bug bounty platforms

## Instructions

### Step 1: Access or Create a Report

**Context**: Select a report in your HackerOne program to use as the base for inviting the victim. This provides the report_id needed for API fetching.

**Instructions**: Log in to HackerOne, navigate to your program dashboard, and open an existing report or submit a dummy one.

> Note the report_id from the URL (e.g., https://hackerone.com/reports/12345).

### Step 2: Invite Victim by Username

**Context**: Add the target user as a participant to trigger the email logging in activities.

**Instructions**: In the report view, click 'Add Participant' or 'Invite', enter the victim's username, and send the invitation. No acceptance is required.

> The invitation creates an activity log including the victim's email.

### Step 3: Generate API Token

**Context**: Create credentials for authenticated API access to fetch unredacted data.

**Instructions**: Go to Account Settings > API Tokens, create a new token with 'reports:read' scope, and note the identifier:token pair.

> Store securely; this enables basic auth for API calls.

### Step 4: Fetch Report Details via API

**Context**: Query the API to retrieve the report, exposing the email in the response.

**Command** ([[commands/curl-hackerone-report-fetch]]):
```bash
curl "https://api.hackerone.com/v1/reports/[report_id]" -u "api_identifier:token"
```

> This GET request returns JSON with the full report, including activities array. Look for type: 'activity-external-user-invited' and extract attributes.email for the victim's private address. Replace [report_id] with the actual ID and api_identifier:token with your credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-hackerone-report-fetch]]

## Tools Used

- [[tools/Curl]]

## Tags

- information-disclosure
- api-abuse
- email-leak
- hackerone
