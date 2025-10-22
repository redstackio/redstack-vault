---
id: 2fcae15d-7878-4aa5-8913-2a49be386547
name: Reflection Amplification
type: sub-technique
mitre_id: T1498.002
mitre_url: null
created_at: '2023-04-06T00:31:25.911071+00:00'
updated_at: '2023-04-06T00:31:25.911071+00:00'
parent_technique: '[[Network Denial of Service|T1498 - Network Denial of Service]]'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Reflection Amplification

**MITRE ID**: T1498.002

**Parent Technique**: [[Network Denial of Service|T1498 - Network Denial of Service]]

This is a sub-technique of T1498 - Network Denial of Service.

## Summary

Adversaries may attempt to cause a denial of service (DoS) by reflecting a high-volume of network traffic to a target. This type of Network DoS takes advantage of a third-party server intermediary that hosts and will respond to a given spoofed source IP address. This third-party server is commonly t

## Description

Adversaries may attempt to cause a denial of service (DoS) by reflecting a high-volume of network traffic to a target. This type of Network DoS takes advantage of a third-party server intermediary that hosts and will respond to a given spoofed source IP address. This third-party server is commonly termed a reflector. An adversary accomplishes a reflection attack by sending packets to reflectors with the spoofed address of the victim. Similar to Direct Network Floods, more than one system may be used to conduct the attack, or a botnet may be used. Likewise, one or more reflectors may be used to focus traffic on the target.(Citation: Cloudflare ReflectionDoS May 2017) This Network DoS attack may also reduce the availability and functionality of the targeted system(s) and network.

Reflection attacks often take advantage of protocols with larger responses than requests in order to amplify their traffic, commonly known as a Reflection Amplification attack. Adversaries may be able to generate an increase in volume of attack traffic that is several orders of magnitude greater than the requests sent to the amplifiers. The extent of this increase will depending upon many variables, such as the protocol in question, the technique used, and the amplifying servers that actually produce the amplification in attack volume. Two prominent protocols that have enabled Reflection Amplification Floods are DNS(Citation: Cloudflare DNSamplficationDoS) and NTP(Citation: Cloudflare NTPamplifciationDoS), though the use of several others in the wild have been documented.(Citation: Arbor AnnualDoSreport Jan 2018)  In particular, the memcache protocol showed itself to be a powerful protocol, with amplification sizes up to 51,200 times the requesting packet.(Citation: Cloudflare Memcrashed Feb 2018)

## Tactics

This sub-technique is used in the following tactics:

- [[Impact|TA0040 - Impact]]
