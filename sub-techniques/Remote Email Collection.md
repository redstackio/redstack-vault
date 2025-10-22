---
id: 58290f6e-ecee-409e-b635-1197bb0e40e5
name: Remote Email Collection
type: sub-technique
mitre_id: T1114.002
mitre_url: null
created_at: '2023-04-06T00:31:26.764949+00:00'
updated_at: '2023-04-06T00:31:26.764949+00:00'
parent_technique: '[[Email Collection|T1114 - Email Collection]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Remote Email Collection

**MITRE ID**: T1114.002

**Parent Technique**: [[Email Collection|T1114 - Email Collection]]

This is a sub-technique of T1114 - Email Collection.

## Summary

Adversaries may target an Exchange server, Office 365, or Google Workspace to collect sensitive information. Adversaries may leverage a user's credentials and interact directly with the Exchange server to acquire information from within a network. Adversaries may also access externally facing Exchan

## Description

Adversaries may target an Exchange server, Office 365, or Google Workspace to collect sensitive information. Adversaries may leverage a user's credentials and interact directly with the Exchange server to acquire information from within a network. Adversaries may also access externally facing Exchange services, Office 365, or Google Workspace to access email using credentials or access tokens. Tools such as [MailSniper](https://attack.mitre.org/software/S0413) can be used to automate searches for specific keywords.

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
