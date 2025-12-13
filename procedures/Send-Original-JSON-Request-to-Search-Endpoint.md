---
tags:
  - recon
  - api-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 8c2844cb-ea4b-4430-9c13-33bfee7b5068
created_at: '2025-12-13T09:00:27.558Z'
updated_at: '2025-12-13T09:00:27.558Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Original JSON Request to Search Endpoint

## Summary

This procedure involves sending a standard JSON POST request to the Informatica Marketplace search API endpoint to establish baseline functionality and confirm the endpoint's behavior.

## Description

The procedure targets the /api/rest/mpapi/infaMPAPISearchWebService/query endpoint, sending search parameters in JSON format. It is used to verify that the endpoint processes requests correctly before attempting vulnerability exploitation. The expected outcome is a normal response, indicating the endpoint is active and parsing input.

## Requirements

1. Network access to marketplace.informatica.com
2. Tool for sending HTTP requests (e.g., curl)
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Monitor for unusual POST requests to API endpoints
- Implement rate limiting on search queries

## Objectives

1. Confirm endpoint accessibility
2. Establish baseline response
3. Prepare for payload modification

## Instructions

### Step 1: Prepare and Send JSON Request

**Context**: Send the original JSON payload to observe normal behavior.

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query":"*","rows":10,"offset":0}' https://marketplace.informatica.com/api/rest/mpapi/infaMPAPISearchWebService/query
```

> This command sends a search query and expects a JSON response with results.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[recon]]
- [[api-testing]]
