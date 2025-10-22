---
id: 4ab67ed1-c1a4-463a-a41b-d862c3d2bd6c
name: Scan public S3 Buckets from sub-domains list (s3scanner)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:52.495114+00:00'
updated_at: '2023-05-25T20:06:46.524788+00:00'
commands:
- '[[aws-cli list data inside the s3 buckets]]'
- '[[s3scanner scan for public s3 buckets from list of sub-domains]]'
---

# Scan public S3 Buckets from sub-domains list (s3scanner)

**Status**: ✓ Verified

## Summary

S3 buckets with misconfigured permissions can leak important information. We have found configuration xml / json scripts. API keys. Credentials and more. s3scanner 

## Description

# Description

S3 buckets with misconfigured permissions can leak important information.

We have found configuration xml / json scripts. API keys. Credentials and more.

[s3scanner](https://github.com/sa7mon/S3Scanner)

##  Instructions

1. Scan a list of public subdomains from a list of domains in a text file.

**Command** ([[s3scanner scan for public s3 buckets from list of sub-domains]]):

```bash
python3 ./s3scanner.py -l domains.txt -o buckets.txt

```

2. Enumerate all of the data inside the buckets

**Command** ([[aws-cli list data inside the s3 buckets]]):

```bash
for i in $(cat buckets.txt); do aws s3 ls s3://$i; done;

```

## Commands Used

- [[aws-cli list data inside the s3 buckets]]
- [[s3scanner scan for public s3 buckets from list of sub-domains]]
