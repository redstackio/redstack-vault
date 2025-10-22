---
id: 95b34c4a-7225-48d1-bfb1-7029a4c32307
name: Domain Fronting
type: technique
mitre_id: T1172
mitre_url: null
created_at: '2019-08-28T21:17:26.898873+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Domain Fronting

**MITRE ID**: T1172

## Description

Domain fronting takes advantage of routing schemes in Content Delivery Networks (CDNs) and other services which host multiple domains to obfuscate the intended destination of HTTPS traffic or traffic tunneled through HTTPS. [1] The technique involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. If both domains are served from the same CDN, then the CDN may route to the address specified in the HTTP header after unwrapping the TLS header. A variation of the the technique, "domainless" fronting, utilizes a SNI field that is left blank; this may allow the fronting to work even when the CDN attempts to validate that the SNI and HTTP Host fields match (if the blank SNI fields are ignored).For example, if domain-x and domain-y are customers of the same CDN, it is possible to place domain-x in the TLS header and domain-y in the HTTP header. Traffic will appear to be going to domain-x, however the CDN may route it to domain-y.

# Detection

If SSL inspection is in place or the traffic is not encrypted, the Host field of the HTTP header can be checked if it matches the HTTPS SNI or against a blacklist or whitelist of domain names. [1]

# Mitigation

If it is possible to inspect HTTPS traffic, the captures can be analyzed for connections that appear to be Domain Fronting.

In order to use domain fronting, attackers will likely need to deploy additional tools to compromised systems. [3] [2] It may be possible to detect or prevent the installation of these tools with Host-based solutions.

# Footnotes

[1] David Fifield, Chang Lan, Rod Hynes, Percy Wegmann, and Vern Paxson. (2015). Blocking-resistant communication through domain fronting. Retrieved November 20, 2017.

[2] Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved October 4, 2016.

[3] Matthew Dunwoody. (2017, March 27). APT29 Domain Fronting With TOR. Retrieved November 20, 2017.

## Defense

If it is possible to inspect HTTPS traffic, the captures can be analyzed for connections that appear to be Domain Fronting.

In order to use domain fronting, attackers will likely need to deploy additional tools to compromised systems. (Citation: FireEye 

## Tactics

- [[Command and Control|TA0011 - Command and Control]]
