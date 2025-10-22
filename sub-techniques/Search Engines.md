---
id: fabc6fae-070c-4066-9311-612a96940135
name: Search Engines
type: sub-technique
mitre_id: T1593.002
mitre_url: null
created_at: '2023-04-06T00:31:26.322324+00:00'
updated_at: '2023-04-06T00:31:26.322324+00:00'
parent_technique: '[[Search Open Websites/Domains|T1593 - Search Open Websites/Domains]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Search Engines

**MITRE ID**: T1593.002

**Parent Technique**: [[Search Open Websites/Domains|T1593 - Search Open Websites/Domains]]

This is a sub-technique of T1593 - Search Open Websites/Domains.

## Summary

Adversaries may use search engines to collect information about victims that can be used during targeting. Search engine services typical crawl online sites to index context and may provide users with specialized syntax to search for specific keywords or specific types of content (i.e. filetypes).(C

## Description

Adversaries may use search engines to collect information about victims that can be used during targeting. Search engine services typical crawl online sites to index context and may provide users with specialized syntax to search for specific keywords or specific types of content (i.e. filetypes).(Citation: SecurityTrails Google Hacking)(Citation: ExploitDB GoogleHacking)

Adversaries may craft various search engine queries depending on what information they seek to gather. Threat actors may use search engines to harvest general information about victims, as well as use specialized queries to look for spillages/leaks of sensitive information such as network details or credentials. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Valid Accounts](https://attack.mitre.org/techniques/T1078) or [Phishing](https://attack.mitre.org/techniques/T1566)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
