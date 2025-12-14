---
tags:
  - http-request-smuggling
  - cloudflare
  - transform-rules
  - header-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Cloud (Cloudflare)
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 34849f79-5287-4040-bb66-117daa61947a
created_at: '2025-12-14T17:28:36.459Z'
updated_at: '2025-12-14T17:28:36.459Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Newline-into-Headers-Using-Hex-Escapes-in-Concat-Function

## Summary

This procedure exploits a lack of output sanitation in Cloudflare's Transform Rules concat() function by using hexadecimal escape sequences to inject newlines into HTTP headers, enabling manipulation of transfer encoding for request smuggling.

## Description

In Cloudflare's Edge Rules engine, the concat() function processes string inputs without properly sanitizing hexadecimal escapes like \x0d\x0a, which resolve to carriage return and newline (\r\n). By crafting a rule that appends these escapes to a header value, an attacker can inject arbitrary headers, such as 'Transfer-Encoding: chunked', into responses. This sets up the target for TE.CL smuggling attacks. The procedure requires access to create or modify Transform Rules in the Cloudflare dashboard and targets applications using Cloudflare as a proxy with internal origin servers protected by Access policies. Successful execution allows subsequent smuggling of requests to internal hosts.

## Requirements

1. Administrative access to the Cloudflare dashboard to create Transform Rules
2. Knowledge of the target header to rewrite (e.g., a custom or existing header)
3. HTTP client for testing (e.g., curl) to verify injection

## Defense

Defensive measures and detection strategies:

- Enable strict input validation and sanitation for all rule expressions in Cloudflare, blocking hex escapes
- Monitor rule creations for suspicious concat() usage with escapes via Cloudflare Logs or Audit Logs
- Implement WAF rules to detect anomalous Transfer-Encoding headers in responses

## Objectives

1. Inject control characters (newlines) into HTTP headers via rule engine
2. Add a forged Transfer-Encoding: chunked header to enable body smuggling
3. Prepare for bypassing security controls like Cloudflare Access

## Instructions

### Step 1: Access Cloudflare Dashboard and Navigate to Rules

**Context**: Log in to create a new Transform Rule targeting header rewriting.

No specific command; use the web interface:

- Go to Rules > Transform Rules > Create Rule
- Set the rule to trigger on requests (e.g., match a path or header)

### Step 2: Craft and Set the Dynamic Header Rewrite Expression

**Context**: Use concat() with hex escapes to inject the newline and new header.

In the rule editor, set the header rewrite value to:

```javascript
concat('existing-header-value-', '\x0d\x0aTransfer-Encoding: chunked')
```

> This expression appends '-\r\nTransfer-Encoding: chunked' to the target header (replace 'existing-header-value-' with actual value or empty string). Save and deploy the rule.

### Step 3: Test the Rule Injection

**Context**: Send a test request to verify the header injection.

Use curl to send a request to the proxied endpoint:

```bash
curl -v -H "Target-Header: test" https://target.cloudflare.com/
```

> Inspect the response headers for the injected 'Transfer-Encoding: chunked' after the newline. Success is confirmed if the header appears malformed or additional headers are present.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[http-request-smuggling]]
- [[cloudflare]]
- [[transform-rules]]
- [[header-injection]]
