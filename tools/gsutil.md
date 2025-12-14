---
id: tool-7
url: 'https://cloud.google.com/storage/docs/gsutil'
tags:
  - gcs
  - storage
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.457Z'
validated: true
submitted: true
---
# gsutil

**Status**: Unverified

## Overview

gsutil is the GCP CLI for Cloud Storage, used for bucket creation and management in kOps setup.

## Description

In this context, gsutil initializes the state store bucket for kOps, but gcloud storage can substitute for cat operations in attacks.

## Features

- Feature 1: Bucket CRUD (mb, ls, rm)
- Feature 2: Object copy and cat
- Feature 3: IAM integration

## Installation

### Requirements

- Part of gcloud SDK

### Install Commands

```bash
# With gcloud
gcloud components install gsutil
```

## Basic Usage

```bash
gsutil --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `mb` | Make bucket |
| `cp` | Copy objects |

## Examples

### Example 1: Basic Usage

```bash
gsutil mb gs://my-bucket/
```

### Example 2: Advanced Usage

```bash
gsutil cat gs://bucket/object.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage

### Tactics

- [[Collection]] Collection

## Detection

- GCS access logs for gsutil
- Bucket creation from service accounts

## Related Procedures

- Setup phase for state store

## Related Tools

- [[tools/gcloud]]
- [[tools/aws-s3-cli]]

## References

- Official: https://cloud.google.com/storage/docs/gsutil
- Commands reference
