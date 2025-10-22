---
id: c59bf4f2-c3f1-4098-927e-39108039fb11
name: AWS Cloudfront Distribution Invalidate File
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:30.306255+00:00'
updated_at: '2023-05-25T20:05:36.608030+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws cloudfront invalidate file from distribution]]'
- '[[aws cloudfront invalidate files with wildcard from distribution]]'
---

# AWS Cloudfront Distribution Invalidate File

**Status**: ✓ Verified

## Summary

Invalidating a file from a cloudfront distribution to refresh the CDN and serve a current version of the file. 

## Description

# Description

Invalidating a file from a cloudfront distribution to refresh the CDN and serve a current version of the file.

##  Instructions

1. To invalidate index and error HTML files from the distribution: use the distribution ID and file path locations

**Command** ([[aws cloudfront invalidate file from distribution]]):

```bash
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID  --paths $FILE_PATH $FILE_PATH_2

```

2. To invalidate everything in the distribution:

**Command** ([[aws cloudfront invalidate files with wildcard from distribution]]):

```bash
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID  --paths $FILE_PATH

```

## Platforms

- Cloud

## Commands Used

- [[aws cloudfront invalidate file from distribution]]
- [[aws cloudfront invalidate files with wildcard from distribution]]

## Tags

- [[AWS]]
- [[Cloud]]
