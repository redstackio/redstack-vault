---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - gcs
  - public-access
  - browser
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.481Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Public-GCS-Bucket-via-Browser

## Summary

This procedure demonstrates direct browser-based access to a publicly misconfigured Google Cloud Storage bucket, allowing anonymous listing and downloading of contents without authentication, as exploited in the GitLab incident.

## Description

In scenarios where GCS buckets are set to public read access, attackers can navigate to the bucket's HTTPS URL to browse and retrieve files. This targets the 'about.gitlab.com' bucket, exposing internal files. Prerequisites include internet access; no tools or credentials are needed. Outcomes include immediate visibility of sensitive data, enabling further enumeration.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Internet connectivity
3. Knowledge of the target bucket URL (e.g., https://storage.googleapis.com/about.gitlab.com)

## Defense

Defensive measures and detection strategies:

- Configure IAM policies to restrict anonymous access to buckets
- Enable bucket-level logging and monitor for unusual GET requests from unknown IPs
- Use tools like Google Cloud Audit Logs to detect public object access

## Objectives

1. Confirm public readability of the GCS bucket
2. Browse and identify sensitive files for download
3. Initiate data exfiltration without command-line tools

## Instructions

### Step 1: Navigate to Bucket URL

**Context**: Directly access the public endpoint to verify exposure and list contents.

No command required; use browser:

Visit https://storage.googleapis.com/about.gitlab.com

> This loads an XML or HTML listing of bucket objects, showing files like all-releases.xml and directories like javascripts/.

### Step 2: Download Visible Files

**Context**: Select and retrieve individual files from the listing.

Right-click or use direct links to download files such as https://storage.googleapis.com/about.gitlab.com/mindmap.txt.

> Expected output: File contents displayed or saved locally, revealing internal links and data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gcs]]
- [[public-bucket]]
- [[information-disclosure]]
