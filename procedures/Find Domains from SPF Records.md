---
id: 874ec00a-0aff-4eaf-b7e9-25febb747fd7
name: Find Domains from SPF Records
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:28.277682+00:00'
updated_at: '2023-05-25T20:12:15.101840+00:00'
commands:
- '[[assets_from_spf scan for assets from domain]]'
- '[[assets_from_spf scan for assets from domain with ASN to jq]]'
---

# Find Domains from SPF Records

**Status**: ✓ Verified

## Summary

A Python script to parse netblocks & domain names from SPF(Sender Policy Framework) DNS record Assets from SPF 

## Description

# Description

A Python script to parse netblocks & domain names from SPF(Sender Policy Framework) DNS record

[Assets from SPF](https://github.com/yamakira/assets-from-spf)

**Command** ([[assets_from_spf scan for assets from domain]]):

```bash
python assets_from_spf.py owasp.com

```

**Command** ([[assets_from_spf scan for assets from domain with ASN to jq]]):

```bash
python assets_from_spf.py owasp.com --asn | jq .

```

## Commands Used

- [[assets_from_spf scan for assets from domain]]
- [[assets_from_spf scan for assets from domain with ASN to jq]]
