---
id: 46cf9104-f552-498b-88e2-fa0ae5b22e5c
type: command
executor: bash
data: ./bucket_finder.rb --download --region ie my_words
output: null
created_at: '2023-04-06T03:56:08.937909+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - s3
  - download
verified: true
validated: true
---

# Download Public S3 Buckets Region IE

## Command

```bash
./bucket_finder.rb --download --region ie my_words
```

## Description

Downloads contents from public buckets in the IE region.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --download | Enable download | Yes |
| --region ie | Region | Yes |
| my_words | Wordlist | Yes |

## Examples

### Basic Usage

```bash
./bucket_finder.rb --download --region ie my_words
```

## Expected Output

Downloading from bucket-ie... files saved.
