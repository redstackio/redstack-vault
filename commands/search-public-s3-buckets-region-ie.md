---
id: 8d617826-22d2-49e5-9b44-2eb895cb0122
type: command
executor: bash
data: ./bucket_finder.rb --region ie my_words
output: null
created_at: '2023-04-06T03:56:08.937826+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - s3
  - region
verified: true
validated: true
---

# Search Public S3 Buckets Region IE

## Command

```bash
./bucket_finder.rb --region ie my_words
```

## Description

Brute-forces public S3 buckets in the Ireland region.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region ie | Target region (Ireland) | Yes |
| my_words | Wordlist | Yes |

## Examples

### Basic Usage

```bash
./bucket_finder.rb --region ie my_words
```

## Expected Output

Region: Ireland
Public: bucket-ie-public
