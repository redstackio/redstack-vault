---
id: 69c95c3f-3c4f-4db2-b1a2-0824b42afb59
name: Cloud-Instance-Rancher-Metadata-Retrieval-via-SSRF
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.800958+00:00'
updated_at: '2023-04-10T20:24:14.009532+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
sub_techniques: []
tags:
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/SSRF URL for Cloud Instances]]'
  - '[[tags/SSRF URL for Rancher]]'
commands:
  - '[[commands/curl-fetch-rancher-metadata]]'
platforms:
  - Cloud
  - Kubernetes
  - Web
tools: []
validated: true
---

# Cloud-Instance-Rancher-Metadata-Retrieval-via-SSRF

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in a web application to force the server to request internal Rancher metadata endpoints on a cloud instance, retrieving sensitive information such as container details, IP addresses, and potentially access credentials. Rancher, a Kubernetes management platform, exposes a metadata service at http://rancher-metadata that provides instance-specific data, which can be accessed via SSRF if the vulnerable application runs on the same host or network.

## Description

Server-Side Request Forgery (SSRF) allows attackers to make unauthorized requests from the server-side to internal or external resources. In cloud environments managed by Rancher, the metadata API (similar to AWS IMDS or GCP metadata) contains critical information about the instance, including network configuration, container names, and service account tokens. By identifying an SSRF-vulnerable input in a web application (e.g., a URL fetcher, image loader, or webhook), the attacker crafts a payload directing the server to query http://rancher-metadata/<version>/<path>. This technique is particularly effective in containerized environments where the application lacks network restrictions, enabling discovery of cloud infrastructure details and potential lateral movement. The procedure assumes the target application is deployed on a Rancher-managed cluster and focuses on blind SSRF scenarios where direct responses may not be visible, relying on out-of-band techniques or error messages for confirmation.

## Requirements

1. Access to a web application with an SSRF vulnerability, such as an unprotected URL parameter that the server fetches (e.g., via GET/POST requests).
2. The target server must be running on a Rancher-managed cloud instance with access to the internal metadata service (http://rancher-metadata).
3. Knowledge of the Rancher metadata API version (e.g., 2016-07-29) and desired paths (e.g., self/container/name, self/ip).
4. Tools for crafting and sending HTTP requests, such as curl or a proxy like Burp Suite.
5. Optional: Out-of-band monitoring (e.g., DNS exfiltration) if the SSRF is blind.

## Defense

- Implement strict input validation and whitelisting for URL parameters to block internal IP ranges (e.g., 169.254.169.254, localhost, 127.0.0.1) and non-routable addresses.
- Use network segmentation and firewall rules to restrict server outbound traffic to metadata endpoints, or disable the Rancher metadata service if unnecessary.
- Enable application-level protections like Content Security Policy (CSP) for resource fetches and monitor server logs for anomalous internal requests.
- Regularly scan for SSRF vulnerabilities using tools like SSRFmap or automated scanners, and implement rate limiting on user-controlled endpoints.

## Objectives

1. Exploit SSRF to access internal Rancher metadata without direct instance access.
2. Extract sensitive instance information, such as container IDs, IPs, and credentials, for further reconnaissance or privilege escalation.
3. Demonstrate the impact of SSRF in cloud-native environments to inform defensive hardening.

## Instructions

### Step 1: Identify the SSRF-Vulnerable Endpoint

**Context**: Locate an input field or parameter in the web application that causes the server to make HTTP requests based on user-supplied data. Common vectors include file imports, webhooks, or preview features. Test for SSRF by submitting external URLs (e.g., http://your-controlled-server.com/test) and checking for interactions on your server.

No specific command required for identification; use manual testing or tools like Burp Suite to intercept and modify requests.

> Probe the endpoint with a known external URL to confirm SSRF. If your server receives the request, the vulnerability is confirmed.

### Step 2: Determine Rancher Metadata API Version

**Context**: The Rancher metadata service uses versioned endpoints. Common versions include 2015-12-19 or 2016-07-29. Start with the latest known version and iterate if responses indicate errors. This step ensures the payload targets a valid API path.

**Command** ([[commands/curl-fetch-rancher-metadata]]):
```bash
curl http://rancher-metadata/2016-07-29/
```

> This command fetches the root of the metadata API. If successful via SSRF, it should return a JSON or XML listing available paths (e.g., {"self": "/self", "stack": "/stack"}). In a blind SSRF, use error messages or timing to infer success. Adjust the version if a 404 or empty response occurs.

### Step 3: Craft and Submit the SSRF Payload

**Context**: Replace the vulnerable URL parameter with the Rancher metadata endpoint. For example, if the app fetches http://user-input.com, set user-input to rancher-metadata/2016-07-29/self/container/name. Submit via the application's form or API. If the response echoes the fetched content, extract it directly; otherwise, use out-of-band channels (e.g., append ?@your-dns-server.com to trigger DNS queries).

**Command** ([[commands/curl-fetch-rancher-metadata]]):
```bash
curl "http://vulnerable-app.com/fetch?url=http://rancher-metadata/2016-07-29/self/container/name"
```

> The command simulates the SSRF request. Expected output from the metadata fetch includes details like container name (e.g., {"name": "my-container-123"}). Monitor the application's response for leaked data or errors indicating internal access. Repeat for paths like /self/ip or /self/links/service-accounts to gather more info.

### Step 4: Verify and Extract Sensitive Data

**Context**: Confirm success by checking for instance-specific details that shouldn't be public. If credentials or tokens are retrieved (e.g., from /self/links/kubeconfig), validate them against the cloud environment. Document findings for chaining to other attacks like privilege escalation.

No specific command; parse the response manually or with jq for JSON output.

> Success is indicated by unique instance data (e.g., internal IPs starting with 10.x.x.x or container UUIDs). If blind, correlate with DNS logs or timing differences.
