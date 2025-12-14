---
id: proc-create-slack-post-json
tags:
  - slack
  - api
type: procedure
tools:
  - '[[tools/Slack-API-files-info]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/slack-api-files-info]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:15.171Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Slack-Post-and-Retrieve-JSON

## Summary

This procedure creates a new Slack Post to generate an editable JSON file on files.slack.com and retrieves its private URL via API for subsequent HTML injection.

## Description

Slack Posts create JSON files with 'full' and 'preview' fields containing HTML content. Using the /api/files.info endpoint, attackers retrieve the url_private for direct editing. This exploits the editable nature of Post metadata.

## Requirements

1. Authenticated Slack session (valid token).
2. Access to Slack web or API client.
3. Team ID and file ID from post creation.

## Defense

Defensive measures and detection strategies:

- Sanitize all editable file metadata inputs.
- Rate-limit API calls to files.info.
- Log and monitor JSON edits for anomalous HTML.

## Objectives

1. Generate target JSON file for injection.
2. Obtain private URL for editing.
3. Set up for HTML payload insertion.

## Instructions

### Step 1: Create New Slack Post

**Context**: Initiate a post to create the JSON structure.

Use Slack web UI to create a post with sample content like <p>Test</p>.

> This generates files-pri/{TEAM_ID}-{FILE_ID}/TITLE.json.

### Step 2: Retrieve Private URL

**Context**: Call API to get editable URL.

**Command** ([[commands/slack-api-files-info]]):
```bash
curl -H "Authorization: Bearer YOUR_SLACK_TOKEN" "https://slack.com/api/files.info?file={FILE_ID}"
```

> Parses response for url_private: https://files.slack.com/files-pri/{TEAM_ID}-{FILE_ID}/TITLE.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/slack-api-files-info]]

## Tools Used

- [[tools/Slack-API-files-info]]

## Tags

- slack
- api
