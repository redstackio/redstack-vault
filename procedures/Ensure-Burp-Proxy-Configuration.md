---
id: proc-uuid-2
tags:
  - proxy
  - interception
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Standard Application Layer Protocol]]'
updated_at: '2025-12-14T17:29:56.917Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Standard Application Layer Protocol]]'
---
# Ensure-Burp-Proxy-Configuration

## Summary

This procedure sets up Burp Suite as a proxy to intercept and modify HTTP/HTTPS traffic from the browser, essential for tampering with GraphQL requests in web-based attacks.

## Description

Burp Suite acts as a man-in-the-middle proxy to capture requests to the Shopify Plus API. Configuration involves setting the browser to route traffic through Burp's listener (default port 8080) and handling HTTPS with CA certificate installation. This enables observation and modification of GraphQL payloads in real-time. Target environment is any web application; prerequisites include Burp Suite installation. Expected outcome is full visibility and control over outgoing requests.

## Requirements

1. Burp Suite Community or Professional edition installed
2. Browser (e.g., Firefox or Chrome) configured for proxying
3. Target site's CA certificate imported to trust intercepted HTTPS traffic
4. Administrative access for certificate installation if needed

## Defense

Defensive measures and detection strategies:

- Monitor for proxy artifacts like unusual User-Agent strings or CA mismatches in logs
- Enforce certificate pinning in applications to detect MITM attempts
- Use HSTS and strict TLS policies to block untrusted proxies
- Detect anomalous request patterns indicative of interception tools

## Objectives

1. Route all browser traffic through Burp for interception
2. Enable HTTPS decryption for payload inspection
3. Prepare for request modification without disrupting the session

## Instructions

### Step 1: Launch Burp Suite and Configure Proxy Listener

**Context**: Start the proxy service to listen for incoming traffic.

Open Burp Suite, navigate to Proxy > Options, ensure the listener is running on 127.0.0.1:8080.

### Step 2: Configure Browser Proxy Settings

**Context**: Direct browser traffic to Burp.

In browser settings (e.g., Firefox: Preferences > Network Settings), set HTTP Proxy to 127.0.0.1 port 8080, enable for HTTPS.

### Step 3: Install Burp CA Certificate

**Context**: Trust Burp's certificate to avoid HTTPS warnings.

Visit http://burp/cert in the proxied browser, download the CA certificate, and import it into the browser's trust store.

### Step 4: Verify Interception

**Context**: Test the setup with a sample request.

Navigate to a test site; confirm requests appear in Burp's Proxy > HTTP history.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- proxy
- interception
- burp
- setup
