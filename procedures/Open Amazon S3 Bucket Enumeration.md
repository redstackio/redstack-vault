---
id: ed2dacfb-8c3c-4fcf-a6a1-edc7c19dbe24
name: Open Amazon S3 Bucket Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.559394+00:00'
updated_at: '2023-04-06T03:55:53.576680+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[Amazon Bucket S3 AWS]]'
- '[[Open Bucket]]'
---

# Open Amazon S3 Bucket Enumeration

## Summary

Open Amazon S3 Bucket Enumeration is a technique that allows an attacker to browse publicly accessible Amazon S3 buckets. Amazon S3 buckets are often used to store sensitive data such as database backups, user data, and application source code. An attacker can use this technique to discover sensiti

## Description

# Description

Open Amazon S3 Bucket Enumeration is a technique that allows an attacker to browse publicly accessible Amazon S3 buckets. Amazon S3 buckets are often used to store sensitive data such as database backups, user data, and application source code. An attacker can use this technique to discover sensitive information that can be used for further attacks. This technique is often used in the initial stages of an attack to gather intelligence.

## Requirements

1. Access to the internet.

1. Knowledge of the name of the Amazon S3 bucket.

## Defense

1. Ensure that Amazon S3 buckets are not publicly accessible.

1. Use access control lists (ACLs) and bucket policies to restrict access to Amazon S3 buckets.

1. Use encryption to protect sensitive data stored in Amazon S3 buckets.

## Objectives

1. Discover sensitive data stored in publicly accessible Amazon S3 buckets.

1. Gather intelligence for further attacks.

# Instructions

1. To browse an open bucket, replace [bucket_name] with the name of the bucket you want to browse.

**Code**: [[http://s3.amazonaws.com/[bucket_name]/
http://[buc]]

> This command provides URLs that can be used to browse open Amazon S3 buckets. The URLs are in the format http://s3.amazonaws.com/[bucket_name]/ and http://[bucket_name].s3.amazonaws.com/. By replacing [bucket_name] with the name of the bucket you want to browse, you can access the contents of the bucket if it is open.

2. To list the names of buckets, send a GET request to the following URL: http://s3.amazonaws.com/

**Code**: [[<ListBucketResult xmlns="http://s3.amazonaws.com/d]]

> This command lists the names of Amazon S3 buckets if the listing is enabled. The names are listed in XML format and can be accessed by sending a GET request to http://s3.amazonaws.com/.

3. To extract the name of an Amazon S3 bucket, use the following URL encoding: %C0

**Code**: [[%C0]]

> This command extracts the name of an Amazon S3 bucket from an inside-site URL by using URL encoding. The URL encoding %C0 is used to extract the name of the bucket.

4. To browse an inside-site Amazon S3 bucket, replace [bucket_name] with the name of the bucket you want to browse and use the following URL: http://example.com/resources/id%C0

**Code**: [[http://example.com/resources/id%C0

eg: http://red]]

> This command provides a URL that can be used to browse an inside-site Amazon S3 bucket. By replacing [bucket_name] with the name of the bucket you want to browse and using the URL http://example.com/resources/id%C0, you can access the contents of the bucket if it is open.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Tags

- [[Amazon Bucket S3 AWS]]
- [[Open Bucket]]
