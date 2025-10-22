---
id: 98e0671a-d9f4-486e-a49c-57a33d35c097
name: Email Forwarding Rule
type: sub-technique
mitre_id: T1114.003
mitre_url: null
created_at: '2023-04-06T00:31:26.434432+00:00'
updated_at: '2023-04-06T00:31:26.434432+00:00'
parent_technique: '[[Email Collection|T1114 - Email Collection]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Email Forwarding Rule

**MITRE ID**: T1114.003

**Parent Technique**: [[Email Collection|T1114 - Email Collection]]

This is a sub-technique of T1114 - Email Collection.

## Summary

Adversaries may setup email forwarding rules to collect sensitive information. Adversaries may abuse email-forwarding rules to monitor the activities of a victim, steal information, and further gain intelligence on the victim or the victim’s organization to use as part of further exploits or operati

## Description

Adversaries may setup email forwarding rules to collect sensitive information. Adversaries may abuse email-forwarding rules to monitor the activities of a victim, steal information, and further gain intelligence on the victim or the victim’s organization to use as part of further exploits or operations.(Citation: US-CERT TA18-068A 2018) Furthermore, email forwarding rules can allow adversaries to maintain persistent access to victim's emails even after compromised credentials are reset by administrators.(Citation: Pfammatter - Hidden Inbox Rules) Most email clients allow users to create inbox rules for various email functions, including forwarding to a different recipient. These rules may be created through a local email application, a web interface, or by command-line interface. Messages can be forwarded to internal or external recipients, and there are no restrictions limiting the extent of this rule. Administrators may also create forwarding rules for user accounts with the same considerations and outcomes.(Citation: Microsoft Tim McMichael Exchange Mail Forwarding 2)(Citation: Mac Forwarding Rules)

Any user or administrator within the organization (or adversary with valid credentials) can create rules to automatically forward all received messages to another recipient, forward emails to different locations based on the sender, and more. Adversaries may also hide the rule by making use of the Microsoft Messaging API (MAPI) to modify the rule properties, making it hidden and not visible from Outlook, OWA or most Exchange Administration tools.(Citation: Pfammatter - Hidden Inbox Rules)

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
