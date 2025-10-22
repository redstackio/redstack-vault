---
id: e4bb54e5-aa4b-4f17-9ad2-139b56145e1c
name: Extract E-mails and Attachments from MS .PST Files
type: procedure
verified: false
submitted: false
created_at: '2019-12-13T22:39:54.291817+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
- '[[extract]]'
commands:
- '[[Extract E-mails and Attachments from a .PST File]]'
---

# Extract E-mails and Attachments from MS .PST Files

## Summary

Microsoft uses .PST files to backup data created with Outlook 2010, Office Outlook 2007, Office Outlook 2003, and Office Outlook 2002. These files may contain sensitive e-mails from a user, and can be enumerated with tools, or simply imported and viewed in Outlook itself. 

## Description

# Description

Microsoft uses .PST files to backup data created with Outlook 2010, Office Outlook 2007, Office Outlook 2003, and Office Outlook 2002. These files may contain sensitive e-mails from a user, and can be enumerated with tools, or simply imported and viewed in Outlook itself.

# Instructions

Install pst-tools, available in most package managers. Eg:

**Code**: [[apt update && apt install pst-tools -y]]

**Command** ([[Extract E-mails and Attachments from a .PST File]]):

```bash
readpst -tea -m $_FILENAME.pst
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]

## Commands Used

- [[Extract E-mails and Attachments from a .PST File]]

## Tags

- [[data exposure]]
- [[extract]]
