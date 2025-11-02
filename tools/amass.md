---
id: dc8a43c5-14d6-49b1-a2db-8957b7604e35
name: amass
type: tool
verified: true
created_at: '2020-06-29T16:46:00.895094+00:00'
updated_at: '2023-05-30T01:09:16.934789+00:00'
commands:
- '[[amass db list previous scans]]'
- '[[amass enumerate company properties]]'
- '[[amass enumerate domain passively]]'
- '[[amass enumerate domains and ip by ASN]]'
- '[[amass enumerate domains by ASN]]'
- '[[amass enumerate domains from cidr ip range]]'
- '[[amass visualize assets using d3 from a previous scan]]'
- '[[sort amass results into IPv4 file]]'
- '[[sort amass results into domain file]]'
- '[[sort amass results into ip file]]'
tags:
- '[[Brute Force]]'
- '[[dns]]'
- '[[Enumeration]]'
- '[[OSINT]]'
---

# amass

**Status**: ✓ Verified

## Overview

The OWASP Amass Project has developed a tool to help information security professionals perform network mapping of attack surfaces and perform external asset discovery using open source information gathering and active reconnaissance techniques. amass has 5 subcommands used to enumerate information

## Description

## Description

The OWASP Amass Project has developed a tool to help information security professionals perform network mapping of attack surfaces and perform external asset discovery using open source information gathering and active reconnaissance techniques.



amass has 5 subcommands used to enumerate information

- intel - discover target properties and information

- enum - enumerate dns and network information

- viz - visualize the enumerated results

- track - differentiate results between enumerations

- db - work with the graph database



These subcommands can be used together to create automated scripts.



## Example



{{EMBEDDED_COMMAND_ed440e9d-f373-4cee-abfd-dbb36948de91}}



## Notes

amass enum has a -passive flag that will not actively validate the DNS information. There are a few reasons to do this, one is if the nameservers are run by the organization and could be monitoring a DNS brute force lookup. Although this is most likely very common to any server on the public internet, you may not want to alert specific organizations they are being enumerated or about to be attacked.

Another reason is the -passive flag can bring up cached information for domains that are not currently active any more, this information can tip you off on "services that used to be running" or perhaps services that have been migrated to a different framework. For example elk.domain.com is expired but splunk.domain.com is active. It would be safe to assume they transitioned stacks, and residual information or backups might exist.





{{EMBEDDED_COMMAND_9dbc5701-85d0-4084-97e4-27ebb9db88bb}}





## Installation





# Usage

## Intel





## Enum





## Viz

## 



## DB





## DNS

## 



## Services

- dns

## Commands (2)

- [[amass enumerate domain passively]]
- [[amass enumerate domains by ASN]]

## Tags

- [[Brute Force]]
- [[dns]]
- [[Enumeration]]
- [[OSINT]]


