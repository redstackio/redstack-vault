---
tags:
  - recon
  - endpoint-discovery
  - linkedin
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:47.182Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 459654f5-dbea-42d3-8276-3d33b6e653ee
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify LinkedIn Resume Download Endpoint

## Summary

This procedure outlines how to identify the API endpoint used for downloading resumes in LinkedIn's Easy Apply or Recruiter features, serving as the entry point for testing access controls.

## Description

In the context of testing LinkedIn's job application features, recruiters or applicants can attach or upload resumes. The download functionality relies on a specific web API endpoint that references files by ID. By inspecting network traffic during a legitimate download, attackers can map the endpoint structure, including URL patterns and required authentication headers. This step is crucial for subsequent IDOR testing, as it reveals how file access is normally handled—limited to the applicant, posting recruiter, or company recruiters.

## Requirements

1. Authenticated LinkedIn account with recruiter access or ability to apply to jobs.
2. Web browser with developer tools (e.g., Chrome DevTools).
3. Stable internet connection to LinkedIn services.

## Defense

Defensive measures and detection strategies:

- Monitor API endpoint access logs for unusual patterns in file ID requests.
- Implement rate limiting on download endpoints to prevent enumeration.
- Use client-side certificate pinning or additional session validation.

## Objectives

1. Locate and document the resume download API endpoint.
2. Capture a sample authorized file ID and request format.
3. Establish baseline for authorization testing.

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Gain access to a resume download scenario to trigger the endpoint.

Log in to LinkedIn and navigate to a job post with Easy Apply or access the Recruiter dashboard with an uploaded resume. Initiate a download.

### Step 2: Inspect Network Traffic

**Context**: Capture the API call details using browser tools.

Open developer tools (F12), go to the Network tab, and filter for XHR/Fetch requests. Perform the download and identify the request to the endpoint (e.g., GET /api/resumes/{fileId}/download). Note headers like Authorization: Bearer {token} and the fileId parameter.

**Expected Output**: Endpoint URL, sample fileId (e.g., 12345), and successful response (PDF binary).

### Step 3: Verify Endpoint

**Context**: Confirm the endpoint responds correctly to authorized requests.

Replay the request in a tool like Postman or curl to ensure it works with your session.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Browser-DevTools]]

## Tags

- [[recon]]
- [[endpoint-discovery]]
- [[linkedin]]
