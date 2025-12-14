---
id: proc-uuid-1
tags:
  - idor
  - traffic-interception
  - twitter-ads
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:36.676Z'
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
# Capture Blobstore Path in Victim Account

## Summary

This procedure authenticates into a victim Twitter Ads account, uses Burp Suite to intercept traffic during audience list creation, and captures the blobstore_path parameter from the uploaded CSV file, which follows a predictable format like /ta_data/<account_id>/<timestamp>.txt.

## Description

In the context of exploiting an IDOR vulnerability in Twitter's audience manager, this step involves setting up a proxy to monitor HTTP requests while creating an audience list. The blobstore_path is generated upon CSV upload to upload.twitter.com and included in the POST to ads.twitter.com. This path lacks account-specific authorization, making it exploitable later. Prerequisites include valid credentials for the victim account and Burp Suite configured as a proxy.

## Requirements

1. Valid Twitter Ads account credentials with Analytics enabled
2. Burp Suite installed and running as an HTTP proxy (e.g., port 8080)
3. Browser configured to route traffic through the proxy
4. Sample CSV file with audience data (e.g., 10001 records)

## Defense

Defensive measures and detection strategies:

- Implement proxy detection (e.g., JA3 fingerprinting for Burp traffic)
- Rate-limit or monitor unusual CSV uploads in audience manager
- Log all blobstore_path usages and validate against account ownership

## Objectives

1. Authenticate and access the audience manager securely
2. Intercept and extract the blobstore_path for later use
3. Ensure the path is in URL-encoded format (e.g., %2Fta_data%2F...)

## Instructions

### Step 1: Authenticate and Configure Proxy

**Context**: Log into the victim account and ensure all traffic is proxied through Burp to capture requests.

No specific command; configure browser proxy settings to 127.0.0.1:8080 and use Burp's Intercept feature.

> Start Burp Suite, turn on Intercept in the Proxy tab, then log in at ads.twitter.com using the victim credentials. Verify dashboard access at https://ads.twitter.com/accounts/<account_id>/audience_manager.

### Step 2: Navigate to Audience Creation and Upload CSV

**Context**: Access the creation endpoint and upload a CSV to trigger path generation.

No specific command; manually navigate to https://ads.twitter.com/accounts/<redacted>/audience_manager/create_list_audience and upload CSV to upload.twitter.com.

> Fill in list details (e.g., name="test", type=3), upload CSV, and observe the blobstore_path in the subsequent POST.

### Step 3: Intercept and Note the Path

**Context**: Capture the full POST request details for the blobstore_path.

Use Burp to view the request body.

> The POST to https://ads.twitter.com/accounts/<redacted>/audience_manager/create_list_audience includes parameters like blobstore_path=%2Fta_data%2F2812522204%2F1413168758432.txt, account=<redacted>, name=test, audience_identification_type=3, input_file_record_count=10001. Copy the encoded path.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- proxy-interception
- authentication
