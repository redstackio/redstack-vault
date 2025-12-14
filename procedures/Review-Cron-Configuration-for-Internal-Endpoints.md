---
id: proc-who-cron-review-001
tags:
  - reconnaissance
  - configuration-review
  - github
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:28.954Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Review-Cron-Configuration-for-Internal-Endpoints

## Summary

This procedure involves examining publicly available cron configuration files, such as cron.yaml in Google App Engine applications, to identify internal endpoints that may be unintentionally exposed. In the WHO COVID-19 App case, this revealed the /internal/cron/refreshCaseStats endpoint scheduled every 5 minutes.

## Description

Attackers often review source code repositories for misconfigurations. Here, the cron.yaml file at https://github.com/WorldHealthOrganization/app/blob/master/server/appengine/src/main/webapp/WEB-INF/cron.yaml#L3 exposed an internal endpoint intended for automated scheduling but accessible publicly due to access control failures post-GCP migration. This step enables discovery of resource-intensive operations that can be abused for DoS.

## Requirements

1. Public access to the target's GitHub repository
2. Basic knowledge of YAML and cron scheduling
3. Web browser or GitHub CLI for file access

## Defense

Defensive measures and detection strategies:

- Restrict repository access to internal teams only
- Avoid committing sensitive configurations like internal endpoints to public repos
- Use secrets management for environment-specific details

## Objectives

1. Identify exposed internal endpoints from cron schedules
2. Understand the frequency and purpose of operations
3. Prepare for testing accessibility

## Instructions

### Step 1: Access the Cron Configuration File

**Context**: Locate and review the cron.yaml file in the public repository to extract endpoint details.

No command required; use a web browser to navigate to https://github.com/WorldHealthOrganization/app/blob/master/server/appengine/src/main/webapp/WEB-INF/cron.yaml and examine line 3.

> This reveals the url: /internal/cron/refreshCaseStats and schedule: every 5 minutes, indicating an internal operation for refreshing case statistics.

### Step 2: Document Endpoint Details

**Context**: Note the endpoint path, schedule, and any HTTP method implied (typically GET for cron).

Manually record: Endpoint /internal/cron/refreshCaseStats is a GET request triggered every 5 minutes.

> Successful review confirms the endpoint's internal nature and potential for abuse.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[configuration-review]]
