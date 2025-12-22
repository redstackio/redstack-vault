---
id: proc-nextcloud-test-ssrf-bypass
tags:
  - ssrf
  - bypass
  - google-cloud
  - alibaba-cloud
  - metadata
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Google Cloud
  - Alibaba Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T03:53:38.310Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
---
# Test SSRF Bypass with Cloud Metadata Endpoints

## Summary

This procedure tests the SSRF bypass in Nextcloud's preventLocalAddress function by submitting cloud metadata URLs to a vulnerable feature, confirming access to internal services and potential data exfiltration.

## Description

When Nextcloud is deployed on Google Cloud or Alibaba Cloud, the preventLocalAddress function's incomplete checks allow SSRF payloads targeting metadata endpoints. For Google Cloud, http://metadata.google.internal/computeMetadata/v1/ can be used to fetch instance details and tokens. For Alibaba Cloud, http://100.100.100.200/latest/meta-data/ exposes similar info. This procedure assumes knowledge of the vulnerable URL parameter (e.g., in sharing or import features) and demonstrates payload injection to validate the exploit, leading to collection of sensitive cloud credentials.

## Requirements

1. Running Nextcloud instance on Google Cloud or Alibaba Cloud.
2. User access to a feature invoking preventLocalAddress (e.g., via web interface or API).
3. Network connectivity to the instance; internal cloud access is implicit via SSRF.

## Defense

Defensive measures and detection strategies:

- Enhance preventLocalAddress with cloud-specific blocklists (e.g., explicit deny for metadata.* domains).
- Deploy network segmentation to isolate app servers from metadata services.
- Log and alert on HTTP requests to internal IPs or domains from application logs.

## Objectives

1. Confirm SSRF success by retrieving metadata via bypassed URL.
2. Extract actionable data like service account tokens.
3. Assess impact on cloud environment security.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate a Nextcloud feature or API endpoint that processes user-supplied URLs through preventLocalAddress.

Review documentation or test features like calendar subscriptions (webcal://) or external shares. Assume an endpoint like /apps/files_sharing/ajax/share.php?action=sendPassword with a URL parameter.

### Step 2: Craft Google Cloud Payload

**Context**: Prepare and submit a request targeting Google metadata service.

Use the browser or a request tool to submit http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token as the URL input. Include the Metadata-Flavor header if proxied.

Example request (adapt to actual endpoint):

```bash
curl -X POST "https://nextcloud-instance.com/vulnerable-endpoint" -d "url=http://metadata.google.internal/computeMetadata/v1/" -H "Content-Type: application/x-www-form-urlencoded"
```

### Step 3: Craft Alibaba Cloud Payload

**Context**: Test bypass for Alibaba's metadata IP.

Submit http://100.100.100.200/latest/meta-data/iam/security-credentials/ as the URL. This IP is not caught by private/reserved range flags.

Example request:

```bash
curl -X POST "https://nextcloud-instance.com/vulnerable-endpoint" -d "url=http://100.100.100.200/latest/meta-data/instance-id" -H "Content-Type: application/x-www-form-urlencoded"
```

### Step 4: Validate Response

**Context**: Check for successful metadata retrieval.

Inspect the response for JSON or text containing cloud details (e.g., token or instance ID). If blocked, the function throws an error; success indicates bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[bypass]]
- [[google-cloud]]
- [[alibaba-cloud]]
- [[metadata]]
