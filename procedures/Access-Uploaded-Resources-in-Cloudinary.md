---
tags:
  - cloudinary
  - file-access
  - unauthorized
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Cloud
techniques:
  - '[[Cloud Instance Metadata API]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 887f4801-b5a1-42e1-b3ce-0a2a4dddbc1c
created_at: '2025-12-14T17:32:48.325Z'
updated_at: '2025-12-14T17:32:48.325Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
---
# Access-Uploaded-Resources-in-Cloudinary

## Summary

This procedure leverages authenticated access to list, view, replace, or delete all uploaded resources in a Cloudinary account, compromising sensitive media like user photos on platforms such as Reverb.com.

## Description

Post-authentication, Cloudinary's dashboard or API allows full CRUD operations on resources tied to the cloud_name (e.g., 'reverb'). This exposes potentially sensitive user uploads. The attack scenario involves navigating the dashboard or calling list endpoints. Prerequisites: Active session with valid credentials. Outcomes: Unauthorized data access and potential tampering.

## Requirements

1. Successful authentication to Cloudinary.
2. Access to dashboard or API endpoints.
3. Knowledge of resource management APIs.

## Defense

Defensive measures and detection strategies:

- Use signed URLs and access controls for resources.
- Audit and log all API calls for delete/replace actions.
- Implement multi-factor auth for account management.

## Objectives

1. Enumerate all uploaded files.
2. View or download sensitive media.
3. Demonstrate manipulation capabilities.

## Instructions

### Step 1: Navigate to Resources

**Context**: Use the dashboard to list uploads.

Log in at res.cloudinary.com and select the 'reverb' account.

### Step 2: List and View Resources

**Context**: Query the API for resource details.

```bash
curl -u '434762629765715:█████' "https://api.cloudinary.com/v1_1/reverb/resources/image?max_results=10"
```

> Returns JSON with resource metadata and URLs for viewing.

**Expected Output**: Array of resources with public IDs and URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Cloud Instance Metadata API]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cloudinary]]
- [[file-access]]
- [[unauthorized]]
