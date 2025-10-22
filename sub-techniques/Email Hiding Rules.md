---
id: 9c822e9d-9e49-42b9-8646-caeb7b60a7b2
name: Email Hiding Rules
type: sub-technique
mitre_id: T1564.008
mitre_url: null
created_at: '2023-04-06T00:31:25.514482+00:00'
updated_at: '2023-04-06T00:31:25.514482+00:00'
parent_technique: '[[Hide Artifacts|T1564 - Hide Artifacts]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Email Hiding Rules

**MITRE ID**: T1564.008

**Parent Technique**: [[Hide Artifacts|T1564 - Hide Artifacts]]

This is a sub-technique of T1564 - Hide Artifacts.

## Summary

Adversaries may use email rules to hide inbound emails in a compromised user's mailbox. Many email clients allow users to create inbox rules for various email functions, including moving emails to other folders, marking emails as read, or deleting emails. Rules may be created or modified within emai

## Description

Adversaries may use email rules to hide inbound emails in a compromised user's mailbox. Many email clients allow users to create inbox rules for various email functions, including moving emails to other folders, marking emails as read, or deleting emails. Rules may be created or modified within email clients or through external features such as the <code>New-InboxRule</code> or <code>Set-InboxRule</code> [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlets on Windows systems.(Citation: Microsoft Inbox Rules)(Citation: MacOS Email Rules)(Citation: Microsoft New-InboxRule)(Citation: Microsoft Set-InboxRule)

Adversaries may utilize email rules within a compromised user's mailbox to delete and/or move emails to less noticeable folders. Adversaries may do this to hide security alerts, C2 communication, or responses to [Internal Spearphishing](https://attack.mitre.org/techniques/T1534) emails sent from the compromised account.

Any user or administrator within the organization (or adversary with valid credentials) may be able to create rules to automatically move or delete emails. These rules can be abused to impair/delay detection had the email content been immediately seen by a user or defender. Malicious rules commonly filter out emails based on key words (such as <code>malware</code>, <code>suspicious</code>, <code>phish</code>, and <code>hack</code>) found in message bodies and subject lines. (Citation: Microsoft Cloud App Security)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
