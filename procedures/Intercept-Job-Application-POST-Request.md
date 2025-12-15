---
tags:
  - intercept
  - http-proxy
  - burp
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
updated_at: '2025-12-14T17:24:26.768Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a3817e70-117c-41f7-b79f-ce29668421a6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Job-Application-POST-Request

## Summary

This procedure captures the multipart/form-data POST request during Greenhouse job application submission using Burp Suite, allowing inspection of S3 URLs in resume_url and cover_letter_url parameters for subsequent tampering.

## Description

As part of a penetration test, configure Burp Suite to act as a proxy between the browser and the server. When the user submits the job application form after uploading files, the request to POST /scout24/jobs/{job_id} is intercepted. This request includes form fields with S3 URLs for the attachments. The procedure ensures the request is paused for modification without alerting the server. Target environment is a web application on Greenhouse.io leveraging AWS S3 for storage; outcomes include visibility into unvalidated parameters enabling open redirect exploitation.

## Requirements

1. Burp Suite installed and running with proxy listener on 127.0.0.1:8080
2. Browser proxy settings configured to route through Burp
3. Completed job application form ready for submission

## Defense

Defensive measures and detection strategies:

- Enable HTTPS interception only with user consent or in controlled environments
- Log proxy usage and anomalous request pauses
- Use certificate pinning to detect man-in-the-middle attempts

## Objectives

1. Capture the exact POST request structure
2. Identify S3 URLs in vulnerable parameters
3. Prepare for parameter modification without resubmission failure

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp to intercept traffic from the browser.

No command required; in Burp, go to Proxy > Options, ensure Intercept is on, and configure browser (e.g., Firefox) to use HTTP proxy 127.0.0.1:8080, installing Burp's CA certificate for HTTPS.

> Expected: All traffic routed through Burp; HTTPS sites load without certificate errors.

### Step 2: Trigger and Intercept Submission

**Context**: Submit the form to capture the request.

No command required; with Intercept on, click 'Submit' on the job application form; Burp will pause the request in the Proxy > Intercept tab, displaying the multipart/form-data body with job_application parameters.

> Expected: Request details show Content-Type: multipart/form-data, including job_application[resume_url] and job_application[cover_letter_url] with S3 links.

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

- [[intercept]]
- [[http-proxy]]
- [[tools/Burp]]
