---
id: 18801813-b836-451b-8253-cabc04a106bc
name: Local Email Collection
type: sub-technique
mitre_id: T1114.001
mitre_url: null
created_at: '2023-04-06T00:31:25.685227+00:00'
updated_at: '2023-04-06T00:31:25.685227+00:00'
parent_technique: '[[Email Collection|T1114 - Email Collection]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Local Email Collection

**MITRE ID**: T1114.001

**Parent Technique**: [[Email Collection|T1114 - Email Collection]]

This is a sub-technique of T1114 - Email Collection.

## Summary

Adversaries may target user email on local systems to collect sensitive information. Files containing email data can be acquired from a user’s local system, such as Outlook storage or cache files.

Outlook stores data locally in offline data files with an extension of .ost. Outlook 2010 and later su

## Description

Adversaries may target user email on local systems to collect sensitive information. Files containing email data can be acquired from a user’s local system, such as Outlook storage or cache files.

Outlook stores data locally in offline data files with an extension of .ost. Outlook 2010 and later supports .ost file sizes up to 50GB, while earlier versions of Outlook support up to 20GB.(Citation: Outlook File Sizes) IMAP accounts in Outlook 2013 (and earlier) and POP accounts use Outlook Data Files (.pst) as opposed to .ost, whereas IMAP accounts in Outlook 2016 (and later) use .ost files. Both types of Outlook data files are typically stored in `C:\Users\<username>\Documents\Outlook Files` or `C:\Users\<username>\AppData\Local\Microsoft\Outlook`.(Citation: Microsoft Outlook Files)

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
