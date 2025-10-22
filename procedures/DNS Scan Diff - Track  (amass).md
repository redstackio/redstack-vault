---
id: 2838ee6c-c272-40c5-8b9c-fb54eb29cb80
name: DNS Scan Diff / Track  (amass)
type: procedure
verified: false
submitted: false
created_at: '2020-07-02T14:57:18.386822+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[amass diff previous scans]]'
---

# DNS Scan Diff / Track  (amass)

## Summary

When amass is used with the directory output for the DB file, you can diff the results from previous scans. This is handy when doing a re-pentest for a client, and you have a scan from 3 -6 months ago, this is a quick and easy technique to identify and new domains without having to look up your exc

## Description

# Description

When amass is used with the directory output for the DB file, you can diff the results from previous scans. This is handy when doing a re-pentest for a client, and you have a scan from 3 -6 months ago, this is a quick and easy technique to identify and new domains without having to look up your excel spreadsheet or old reports.

**Command** ([[amass diff previous scans]]):

```bash
amass track -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -last 2
```

## Commands Used

- [[amass diff previous scans]]
