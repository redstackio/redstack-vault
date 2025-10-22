---
id: 70df9646-a687-4a59-9675-6446d6cf4f73
name: Confluence
type: sub-technique
mitre_id: T1213.001
mitre_url: null
created_at: '2023-04-06T00:31:26.399569+00:00'
updated_at: '2023-04-06T00:31:26.399569+00:00'
parent_technique: '[[Data from Information Repositories|T1213 - Data from Information
  Repositories]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
procedures:
- '[[Lessjs Server Side Template Injection via Inline Import]]'
---

# Confluence

**MITRE ID**: T1213.001

**Parent Technique**: [[Data from Information Repositories|T1213 - Data from Information Repositories]]

This is a sub-technique of T1213 - Data from Information Repositories.

## Summary

Adversaries may leverage Confluence repositories to mine valuable information. Often found in development environments alongside Atlassian JIRA, Confluence is generally used to store development-related documentation, however, in general may contain more diverse categories of useful information, su

## Description

Adversaries may leverage Confluence repositories to mine valuable information. Often found in development environments alongside Atlassian JIRA, Confluence is generally used to store development-related documentation, however, in general may contain more diverse categories of useful information, such as:

* Policies, procedures, and standards
* Physical / logical network diagrams
* System architecture diagrams
* Technical system documentation
* Testing / development credentials
* Work / project schedules
* Source code snippets
* Links to network shares and other internal resources

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Lessjs Server Side Template Injection via Inline Import]]
