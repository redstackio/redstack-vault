---
id: 547af745-06ab-40ea-82d8-285d1fd8c8a3
type: tool
verified: true
created_at: '2019-08-28T21:17:36.232187+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Cloud
tags:
  - evasion
  - domain-fronting
  - c2
  - proxy
url: >-
  https://cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service
validated: true
---

# Domain Fronting Google App Engine

**Status**: Unverified

## Overview

Domain Fronting with Google App Engine is a technique and setup using Google's cloud infrastructure to mask the true destination of network traffic. It leverages the shared domain (e.g., googleapis.com) for the TLS SNI handshake while routing the actual request to a custom App Engine application, commonly used in offensive security for command-and-control (C2) communications, bypassing censorship, or evading network defenses.

## Description

This setup involves deploying a simple proxy application to Google App Engine that forwards incoming requests to backend servers. The key evasion comes from using a legitimate Google domain in the Host header and SNI, making the traffic appear as normal Google API calls. It's particularly useful in red team operations for maintaining persistence without triggering domain-based blocks. Note that Google has restricted domain fronting in recent years, so compatibility should be verified.

## Features

- Feature 1: Proxy requests through Google's global CDN for obfuscation
- Feature 2: Supports HTTP/HTTPS forwarding with custom routing logic
- Feature 3: Scalable deployment without managing servers

## Installation

### Requirements

- Google Cloud SDK (gcloud) installed
- A Google Cloud project with App Engine enabled and billing activated
- Python 3 environment for the app

### Install Commands

```bash
# Install Google Cloud SDK (Ubuntu/Debian)
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Initialize gcloud
 gcloud init

# Enable App Engine
 gcloud app create --region=us-central
```

## Basic Usage

```bash
gcloud app deploy --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| --project | Specify the Google Cloud project |
| --version | Specify the app version |

## Examples

### Example 1: Basic Usage

Deploy a sample proxy app:

```bash
gcloud app deploy
```

### Example 2: Advanced Usage

Deploy with a specific version and project:

```bash
gcloud app deploy --project=my-fronting-project --version=front1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy
- [[Protocol Tunneling]] Protocol Tunneling

### Tactics

- [[Command and Control]] Command And Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual App Engine deployments with proxy-like code
- Detection method 2: Analyze traffic patterns showing Google domain SNI but non-API payloads
- Detection method 3: Log reviews for gcloud deploy commands in cloud audit logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/gcloud]]
- [[tools/cURL]]

## References

- Official documentation: https://cloud.google.com/appengine/docs
- Related resources: https://www.blackhat.com/docs/us-17/thursday/us-17-Fredrikson-Hiding-Among-The-Clouds-Your-Fronting-Service-Is-My-Fronting-Service.pdf
