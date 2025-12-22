---
id: 1ef5924b-f806-4971-a9b0-0a2d56f4f2a0
type: command
executor: bash
data: ./bucket_finder.rb --log-file bucket.out my_words
output: null
created_at: '2023-04-06T03:56:08.937932+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - s3
  - log
verified: true
validated: true
---

# Search Public S3 Buckets with Log

## Command

```bash
./bucket_finder.rb --log-file bucket.out my_words
```

## Description

Searches public buckets and logs output to file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --log-file bucket.out | Log file | Yes |
| my_words | Wordlist | Yes |

## Examples

### Basic Usage

```bash
./bucket_finder.rb --log-file bucket.out my_words
```

## Expected Output

Logged to bucket.out
Public buckets: X found.
