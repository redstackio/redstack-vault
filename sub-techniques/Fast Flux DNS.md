---
id: 295b8ed9-6385-4a78-bd48-326c028df422
name: Fast Flux DNS
type: sub-technique
mitre_id: T1568.001
mitre_url: null
created_at: '2023-04-06T00:31:25.779979+00:00'
updated_at: '2023-04-06T00:31:25.779979+00:00'
parent_technique: '[[Dynamic Resolution|T1568 - Dynamic Resolution]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Fast Flux DNS

**MITRE ID**: T1568.001

**Parent Technique**: [[Dynamic Resolution|T1568 - Dynamic Resolution]]

This is a sub-technique of T1568 - Dynamic Resolution.

## Summary

Adversaries may use Fast Flux DNS to hide a command and control channel behind an array of rapidly changing IP addresses linked to a single domain resolution. This technique uses a fully qualified domain name, with multiple IP addresses assigned to it which are swapped with high frequency, using a c

## Description

Adversaries may use Fast Flux DNS to hide a command and control channel behind an array of rapidly changing IP addresses linked to a single domain resolution. This technique uses a fully qualified domain name, with multiple IP addresses assigned to it which are swapped with high frequency, using a combination of round robin IP addressing and short Time-To-Live (TTL) for a DNS resource record.(Citation: MehtaFastFluxPt1)(Citation: MehtaFastFluxPt2)(Citation: Fast Flux - Welivesecurity)

The simplest, "single-flux" method, involves registering and de-registering an addresses as part of the DNS A (address) record list for a single DNS name. These registrations have a five-minute average lifespan, resulting in a constant shuffle of IP address resolution.(Citation: Fast Flux - Welivesecurity)

In contrast, the "double-flux" method registers and de-registers an address as part of the DNS Name Server record list for the DNS zone, providing additional resilience for the connection. With double-flux additional hosts can act as a proxy to the C2 host, further insulating the true source of the C2 channel.

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
