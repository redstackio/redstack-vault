---
tags:
  - job-application
  - file-upload
  - greenhouse
type: procedure
tools:
  - '[[tools/Burp]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.778Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 61feea98-a706-4c2f-8551-edbf487426ef
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Greenhouse-Job-Application

## Summary

This procedure outlines the legitimate initiation of a job application on the Greenhouse platform, including file uploads that generate S3 URLs, setting the stage for subsequent interception and tampering in an open redirect attack.

## Description

In the context of exploiting an open redirect vulnerability, this step involves navigating to a Greenhouse job board (e.g., scout24.greenhouse.io), selecting a job posting, completing personal information fields, and uploading resume and cover letter files as PDFs. The uploaded files are automatically stored in an AWS S3 bucket, and their URLs are inserted into the form parameters job_application[resume_url] and job_application[cover_letter_url]. This prepares the POST request for interception. No malicious actions occur here; it's the baseline user workflow discovered during penetration testing.

## Requirements

1. Public internet access to https://boards.greenhouse.io/scout24
2. Browser configured for proxy interception (e.g., via Burp Suite)
3. Sample PDF files for upload (e.g., neu.pdf for resume)

## Defense

Defensive measures and detection strategies:

- Implement client-side validation on file upload domains
- Monitor for unusual file upload patterns or external URL submissions
- Use web application firewalls (WAF) to scan form parameters for non-S3 URLs

## Objectives

1. Generate a valid job application form with S3-hosted file URLs
2. Position the workflow for request interception
3. Ensure the application appears legitimate to avoid suspicion

## Instructions

### Step 1: Navigate to Job Board and Select Job

**Context**: Access the target job board and choose a specific opening to start the application process.

No command required; use browser to visit https://boards.greenhouse.io/scout24 and click on a job like https://boards.greenhouse.io/scout24/jobs/503488.

> Expected: Job application form loads with fields for personal info and attachments.

### Step 2: Complete Form and Upload Files

**Context**: Fill required fields and attach documents to trigger S3 upload and URL generation.

No command required; enter personal details, then click 'Attach' under Resume/CV and Cover Letter, select PDF files (e.g., neu.pdf), and proceed to submission.

> Expected: Files upload to S3, form now contains parameters like job_application[resume_url] = https://grnhse-prod-jben-*.s3.amazonaws.com/.../neu.pdf.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp]]

## Tags

- [[job-application]]
- [[file-upload]]
- [[greenhouse]]
