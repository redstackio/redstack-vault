---
id: 8b1e94a4-263e-4b71-9afb-f876ccf92b0e
name: Insecure Email Configuration
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T15:31:46.671581+00:00'
updated_at: '2023-05-26T01:05:07.497864+00:00'
platforms:
- Web
tags:
- '[[misconfiguration]]'
- '[[Web Applications]]'
---

# Insecure Email Configuration

**Status**: ✓ Verified

## Summary

Decription Mail servers rely on both SPF and DMARC to properly deal with email spoofing. SPF shows what servers are allowed to send emails for the current domain.When an email does not originate from one of the listed IP's or domains , it should be automatically rejected. If email servers doesnt em

## Description

# Decription

Mail servers rely on both SPF and DMARC to properly deal with email spoofing. SPF shows what servers are allowed to send emails for the current domain.When an email does not originate from one of the listed IP's or domains , it should be automatically rejected. If email servers doesnt employ SPF and DMARC policy,the servers will accept the spam emails.

# Instructions

1.Go to “https://mxtoolbox.com/dmarc.aspx “ and enter the vulnerable domain and hit DMARC Lookup.

2. Observe that no DMARC records can be seen .

3. Go to “http://www.sendanonymousemail.net/ ” or “https://emkei.cz/ “ and enter all required details to send an spam email to the mail server. Observe that you will receive the email from vulnerable email server.

## Platforms

- Web

## Tags

- [[misconfiguration]]
- [[Web Applications]]
