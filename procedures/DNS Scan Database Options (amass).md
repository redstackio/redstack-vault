---
id: 58d95743-d89e-4371-a91c-384fc41b3541
name: DNS Scan Database Options (amass)
type: procedure
verified: false
submitted: false
created_at: '2020-07-02T14:58:21.105013+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[amass db display assets from previous scan]]'
- '[[amass db list previous scans]]'
---

# DNS Scan Database Options (amass)

## Summary

The DB subcommand can be used to present information from previous scans back to you. List all of the previous scans 

## Description

# Description

The DB subcommand can be used to present information from previous scans back to you.

List all of the previous scans

**Command** ([[amass db list previous scans]]):

```bash
amass db -dir $_OUTPUT_DIRECTORY -list
```

Show the assets that where identified in that scan, the -enum # should match one of the scans listed in the above command.

**Command** ([[amass db display assets from previous scan]]):

```bash
amass db -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -enum $_LIST_NUMBER -show
```

## Commands Used

- [[amass db display assets from previous scan]]
- [[amass db list previous scans]]
