---
id: 1f7eedd1-3263-4e5b-89be-a32f8608b844
name: Email Account
type: sub-technique
mitre_id: T1087.003
mitre_url: null
created_at: '2023-04-06T00:31:26.058590+00:00'
updated_at: '2023-04-06T00:31:26.058590+00:00'
parent_technique: '[[Account Discovery|T1087 - Account Discovery]]'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# Email Account

**MITRE ID**: T1087.003

**Parent Technique**: [[Account Discovery|T1087 - Account Discovery]]

This is a sub-technique of T1087 - Account Discovery.

## Summary

Adversaries may attempt to get a listing of email addresses and accounts. Adversaries may try to dump Exchange address lists such as global address lists (GALs).(Citation: Microsoft Exchange Address Lists)

In on-premises Exchange and Exchange Online, the<code>Get-GlobalAddressList</code> PowerShell

## Description

Adversaries may attempt to get a listing of email addresses and accounts. Adversaries may try to dump Exchange address lists such as global address lists (GALs).(Citation: Microsoft Exchange Address Lists)

In on-premises Exchange and Exchange Online, the<code>Get-GlobalAddressList</code> PowerShell cmdlet can be used to obtain email addresses and accounts from a domain using an authenticated session.(Citation: Microsoft getglobaladdresslist)(Citation: Black Hills Attacking Exchange MailSniper, 2016)

In Google Workspace, the GAL is shared with Microsoft Outlook users through the Google Workspace Sync for Microsoft Outlook (GWSMO) service. Additionally, the Google Workspace Directory allows for users to get a listing of other users within the organization.(Citation: Google Workspace Global Access List)

## Tactics

This sub-technique is used in the following tactics:

- [[Discovery|TA0007 - Discovery]]
