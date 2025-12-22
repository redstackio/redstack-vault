---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - csrf
  - exploit
  - file-upload
  - web
  - aws
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.200Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate CSRF Attack via Malicious Webpage

## Summary

This procedure demonstrates exploiting a CSRF vulnerability by hosting a malicious webpage that auto-submits a file upload form to the target's S3 bucket endpoint, enabling unauthorized uploads when visited by an authenticated user.

## Description

Targeting Udemy's staging S3 upload, this involves creating an HTML form that mimics the legitimate upload but submits automatically from an attacker-controlled site. The attack relies on the victim's active session cookies being sent with the cross-origin request. Outcomes include arbitrary file placement in the staging bucket, potentially abusing processing pipelines, though Udemy rated it low-risk due to the staging nature.

## Requirements

1. Hosting capability for a malicious webpage (e.g., GitHub Pages, local server)
2. Knowledge of the vulnerable endpoint URL and form parameters from prior reconnaissance
3. A test file to upload for proof-of-concept

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies (Lax/Strict) to prevent cross-site submission
- Implement origin/referer header validation on sensitive endpoints
- Log and alert on uploads with mismatched or missing referers

## Objectives

1. Trick an authenticated user into uploading files via a forged request
2. Verify file arrival and processing in the S3 staging bucket
3. Demonstrate the full impact of missing CSRF controls

## Instructions

### Step 1: Craft Malicious HTML Form

**Context**: Build an HTML page with an auto-submitting form targeting the S3 upload endpoint.

Create a file named csrf-poc.html with content that includes a hidden file input and JavaScript to submit on load:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body>
  <form id="uploadForm" action="https://staging.udemy.com/upload-s3" method="POST" enctype="multipart/form-data">
    <input type="hidden" name="file" value="malicious-content.txt">
    <!-- Simulate file upload; in practice, use iframe or actual file -->
  </form>
  <script>document.getElementById('uploadForm').submit();</script>
</body>
</html>
```

Adjust parameters based on the endpoint's expected form fields.

**Expected Output**: Form ready for hosting; no output yet.

### Step 2: Host and Test the Attack

**Context**: Deploy the HTML to an external domain and lure a victim (or self in authenticated session) to visit it.

Upload the HTML to a hosting service and visit the URL while logged into the target site. Monitor the network tab for the cross-origin POST and check the S3 bucket (if accessible) or server logs for the uploaded file.

**Expected Output**: Successful POST response from the endpoint, with the file stored in the staging S3 bucket.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
- [[file-upload]]
- [[web]]
- [[aws]]
