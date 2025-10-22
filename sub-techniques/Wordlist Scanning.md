---
id: dcf37a5f-fc5a-4230-b11f-a6a0de7eca4e
name: Wordlist Scanning
type: sub-technique
mitre_id: T1595.003
mitre_url: null
created_at: '2023-04-06T00:31:26.839873+00:00'
updated_at: '2023-04-06T00:31:26.839873+00:00'
parent_technique: '[[Active Scanning|T1595 - Active Scanning]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Wordlist Scanning

**MITRE ID**: T1595.003

**Parent Technique**: [[Active Scanning|T1595 - Active Scanning]]

This is a sub-technique of T1595 - Active Scanning.

## Summary

Adversaries may iteratively probe infrastructure using brute-forcing and crawling techniques. While this technique employs similar methods to [Brute Force](https://attack.mitre.org/techniques/T1110), its goal is the identification of content and infrastructure rather than the discovery of valid cred

## Description

Adversaries may iteratively probe infrastructure using brute-forcing and crawling techniques. While this technique employs similar methods to [Brute Force](https://attack.mitre.org/techniques/T1110), its goal is the identification of content and infrastructure rather than the discovery of valid credentials. Wordlists used in these scans may contain generic, commonly used names and file extensions or terms specific to a particular software. Adversaries may also create custom, target-specific wordlists using data gathered from other Reconnaissance techniques (ex: [Gather Victim Org Information](https://attack.mitre.org/techniques/T1591), or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).

For example, adversaries may use web content discovery tools such as Dirb, DirBuster, and GoBuster and generic or custom wordlists to enumerate a website’s pages and directories.(Citation: ClearSky Lebanese Cedar Jan 2021) This can help them to discover old, vulnerable pages or hidden administrative portals that could become the target of further operations (ex: [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190) or [Brute Force](https://attack.mitre.org/techniques/T1110)).  

As cloud storage solutions typically use globally unique names, adversaries may also use target-specific wordlists and tools such as s3recon and GCPBucketBrute to enumerate public and private buckets on cloud infrastructure.(Citation: S3Recon GitHub)(Citation: GCPBucketBrute) Once storage objects are discovered, adversaries may leverage [Data from Cloud Storage](https://attack.mitre.org/techniques/T1530) to access valuable information that can be exfiltrated or used to escalate privileges and move laterally. 

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
