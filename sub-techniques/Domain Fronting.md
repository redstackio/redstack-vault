---
id: f0a1fe8a-e4f8-4497-ad48-797deae5e46f
name: Domain Fronting
type: sub-technique
mitre_id: T1090.004
mitre_url: null
created_at: '2023-04-06T00:31:26.927358+00:00'
updated_at: '2023-04-06T00:31:26.927358+00:00'
parent_technique: '[[Connection Proxy|T1090 - Connection Proxy]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[Cobalt Strike Malleable C2 Profile Checking]]'
---

# Domain Fronting

**MITRE ID**: T1090.004

**Parent Technique**: [[Connection Proxy|T1090 - Connection Proxy]]

This is a sub-technique of T1090 - Connection Proxy.

## Summary

Adversaries may take advantage of routing schemes in Content Delivery Networks (CDNs) and other services which host multiple domains to obfuscate the intended destination of HTTPS traffic or traffic tunneled through HTTPS. (Citation: Fifield Blocking Resistent Communication through domain fronting 2

## Description

Adversaries may take advantage of routing schemes in Content Delivery Networks (CDNs) and other services which host multiple domains to obfuscate the intended destination of HTTPS traffic or traffic tunneled through HTTPS. (Citation: Fifield Blocking Resistent Communication through domain fronting 2015) Domain fronting involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. If both domains are served from the same CDN, then the CDN may route to the address specified in the HTTP header after unwrapping the TLS header. A variation of the the technique, "domainless" fronting, utilizes a SNI field that is left blank; this may allow the fronting to work even when the CDN attempts to validate that the SNI and HTTP Host fields match (if the blank SNI fields are ignored).

For example, if domain-x and domain-y are customers of the same CDN, it is possible to place domain-x in the TLS header and domain-y in the HTTP header. Traffic will appear to be going to domain-x, however the CDN may route it to domain-y.

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Cobalt Strike Malleable C2 Profile Checking]]
