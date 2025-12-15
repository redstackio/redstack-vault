---
id: proc-uuid-002
name: Analyze-GraphQL-Response-for-Undisclosed-Reports
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.383Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - information-disclosure
  - json-parsing
  - metadata-extraction
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---

# Analyze-GraphQL-Response-for-Undisclosed-Reports

## Summary

This procedure parses the JSON response from a HackerOne GraphQL query to identify and extract metadata from undisclosed reports in the report_retests nodes.

## Description

Following the GraphQL query, this procedure involves manual or scripted analysis of the response to locate nodes where 'report' is null, signifying undisclosed reports. It extracts key fields like asset_name, asset_type, severity_rating, weakness_name, report_state, report_substate, and retester usernames. This reveals sensitive information about private programs and vulnerabilities, aiding in further reconnaissance. No special tools are needed beyond JSON viewers or parsers like jq.

## Requirements

1. JSON response from the GraphQL query
2. JSON processing tool (e.g., jq, or manual inspection in a text editor)
3. Basic scripting knowledge for automation if scaling analysis

## Defense

Defensive measures and detection strategies:

- Sanitize GraphQL responses to exclude metadata for undisclosed reports
- Log and alert on anomalous data extraction patterns from API responses
- Use data loss prevention (DLP) tools to monitor for leaked metadata in logs

## Objectives

1. Filter response for undisclosed report indicators
2. Extract and document sensitive metadata fields
3. Correlate findings to identify program or asset patterns

## Instructions

### Step 1: Inspect Response Structure

**Context**: Load the JSON response and navigate to data.user.report_retests.nodes to review the array of retest objects.

Look for patterns manually or with a JSON viewer, noting entries where "report": {"_id": null} or simply "report": null.

### Step 2: Extract Metadata

**Context**: Filter and pull specific fields from qualifying nodes to compile the disclosed information.

Use jq for extraction:

```bash
echo '{"data":{"user":{"report_retests":{"nodes":[{"report":null,"asset_name":"https://www.hackerone.com","asset_type":"URL","severity_rating":"low","weakness_name":"Information Disclosure","report_state":"closed","report_substate":"resolved","report_retest_users":{"nodes":[{"user":{"username":"retester1"}}]}}, ... ]}}}}' | jq '.data.user.report_retests.nodes[] | select(.report == null) | {asset_name, asset_type, severity_rating, weakness_name, report_state, report_substate, retester: .report_retest_users.nodes[0].user.username}'
```

> This filters nodes with null report and outputs a structured object with extracted fields. Expected output includes arrays of metadata like asset details and severity ratings for undisclosed items.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[json-parsing]]
- [[metadata-extraction]]
