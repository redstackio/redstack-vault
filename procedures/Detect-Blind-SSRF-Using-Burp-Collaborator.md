---
id: 14f90ae4-8fca-4514-9e15-3a68ff8ae9b0
name: Detect-Blind-SSRF-Using-Burp-Collaborator
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T10:00:54.169116+00:00'
updated_at: '2023-05-26T01:10:01.246777+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Vulnerability Scanning]]'
sub_techniques: []
tags:
  - ssrf
  - out-of-band
  - web-applications
  - vulnerability-scanning
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Detect-Blind-SSRF-Using-Burp-Collaborator

## Summary

This procedure demonstrates how to identify blind Server-Side Request Forgery (SSRF) vulnerabilities using out-of-band (OOB) techniques with Burp Suite's Collaborator feature. In blind SSRF, the application's response does not reflect the backend request's output, making it hard to detect directly; instead, interactions like DNS lookups or HTTP requests to a controlled external server confirm the vulnerability.

## Description

Blind SSRF occurs when an application fetches resources from user-supplied URLs on behalf of the server, but the response is not returned to the attacker. This procedure exploits potential SSRF entry points, such as URL parameters or headers (e.g., Referer), by redirecting backend requests to a Burp Collaborator payload. The Collaborator server captures OOB interactions, such as DNS resolutions or HTTP connections, verifying the SSRF without relying on in-band responses. This is useful in web penetration testing to confirm SSRF in applications processing external resources, like image loaders or API endpoints. Prerequisites include access to Burp Suite Professional and a proxied connection to the target application.

## Requirements

1. Burp Suite Professional with Collaborator enabled.
2. Proxy interception configured between the browser and the target application.
3. Network access to the target web application.
4. Basic understanding of HTTP requests and headers.

## Defense

Defensive measures and detection strategies:

- Validate and whitelist all user-supplied URLs to prevent access to internal or external resources.
- Implement network segmentation to block server outbound connections to untrusted domains.
- Monitor server logs for unexpected DNS queries or HTTP requests to unknown hosts.
- Use Web Application Firewalls (WAFs) to detect anomalous URL patterns in requests.

## Objectives

1. Generate a unique Collaborator payload to capture OOB interactions.
2. Inject the payload into a potential SSRF vector, such as the Referer header.
3. Confirm the vulnerability by observing DNS or HTTP interactions on the Collaborator server.
4. Expected outcome: Evidence of backend request forgery without in-band response leakage.

## Instructions

### Step 1: Generate Collaborator Payload

**Context**: Start Burp Collaborator to obtain a unique domain for tracking OOB interactions. This domain will be used as the SSRF payload to detect if the server resolves it or makes requests to it.

Open the Burp Suite Collaborator client and click "Copy to clipboard" to get the unique Collaborator URL (e.g., abc123xyz.oastify.com). This URL is controlled by Burp and will log any interactions from the target server.

### Step 2: Intercept and Forward Request to Repeater

**Context**: Capture an incoming request to the target application that may contain an SSRF vector, such as a parameter or header that influences backend fetches. Forward it to the Repeater tab for modification.

In the Burp Proxy history, right-click on a relevant request (e.g., one involving URL processing) and select "Send to Repeater." Ensure the request is intercepted if not already.

### Step 3: Inject Collaborator Payload into SSRF Vector

**Context**: Modify the request to inject the Collaborator URL into a potential SSRF entry point, such as the Referer header, to trick the server into making a backend request to your controlled domain.

In the Repeater tab, edit the Referer header to point to the Collaborator URL from Step 1 (e.g., Referer: http://abc123xyz.oastify.com/malicious). Send the modified request to the server.

### Step 4: Poll for OOB Interactions

**Context**: Check the Collaborator client for evidence of the SSRF. Successful exploitation will trigger DNS lookups or HTTP requests from the target server to your Collaborator domain.

Return to the Burp Collaborator client window and click "Poll now." Review the interactions logged, such as DNS queries or HTTP requests originating from the target's IP.

**Expected Output**: A list of interactions in the Collaborator interface, including DNS resolution for the payload domain and possibly HTTP requests with details like user-agent or timestamps.

### Step 5: Verify and Analyze Results

**Context**: Confirm the interactions indicate a blind SSRF by correlating the timing and source with your sent request. This step ensures the observed OOB activity is due to the payload injection.

Examine the interaction details: Look for the target's IP address in the source column and match the timestamp to your Repeater send time. If present, the SSRF is confirmed as blind since no response was reflected in the application.

**Expected Output**: Confirmed interactions tied to the payload, such as "DNS: abc123xyz.oastify.com resolved by [target IP]."
