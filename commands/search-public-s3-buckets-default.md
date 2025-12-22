---
id: 3d8766a9-1e0a-4f94-aaa0-6c4abdfe27d3
type: command
executor: bash
data: ./bucket_finder.rb my_words
output: null
created_at: '2023-04-06T03:56:08.937686+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - s3
  - public
verified: true
validated: true
---

# Search Public S3 Buckets Default Region

## Command

```bash
./bucket_finder.rb my_words
```

## Description

Searches for public S3 buckets using a wordlist in the default region.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| my_words | Wordlist file | Yes |

## Examples

### Basic Usage

```bash
./bucket_finder.rb my_words
```

## Expected Output

Public bucket: company-data found.
