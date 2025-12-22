---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[T1078.004]]'
sub_techniques: []
tags:
  - aws
  - cloudfront
  - cloud
  - invalidation
  - cdn
commands:
  - '[[commands/aws-cloudfront-create-invalidation-specific-paths]]'
  - '[[commands/aws-cloudfront-create-invalidation-all-paths-wildcard]]'
platforms:
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
validated: true
---

# Invalidate-Files-in-AWS-CloudFront-Distribution

## Summary

This procedure demonstrates how to invalidate specific files or all files in an AWS CloudFront distribution using the AWS CLI. Invalidations force CloudFront to fetch the latest versions of files from the origin server, bypassing the CDN cache. This is useful in red team scenarios to refresh malicious content (e.g., updated web shells or payloads) served via CloudFront or to remove evidence of prior modifications.

## Description

AWS CloudFront is a content delivery network (CDN) that caches content at edge locations for faster delivery. Once content is cached, changes to the origin (e.g., S3 bucket or web server) are not immediately reflected globally. To serve an updated version of a file, you must create an invalidation request, which marks the cached objects as stale and triggers a refresh from the origin. This procedure assumes you have valid AWS credentials with permissions to manage CloudFront distributions (e.g., cloudfront:CreateInvalidation). It covers invalidating specific paths (e.g., /index.html) or all paths using a wildcard (/*). Each invalidation incurs a cost and has quotas (e.g., 1,000 per distribution per month), so use judiciously. In an attack context, this could enable persistence by ensuring modified malicious files are served without caching delays.

## Requirements

1. AWS CLI installed and configured with credentials that have CloudFront read/write access (e.g., attached to a policy allowing cloudfront:CreateInvalidation).
2. The Distribution ID of the target CloudFront distribution (obtainable via AWS Console or aws cloudfront list-distributions).
3. Network access to AWS APIs (no direct target access needed, as this is cloud-native).
4. Basic familiarity with AWS services and CLI usage.

## Defense

- Monitor AWS CloudTrail logs for API calls to CreateInvalidation, filtering by principal and distribution ID to detect unauthorized refreshes.
- Implement least-privilege IAM policies to restrict CreateInvalidation to trusted roles only.
- Use AWS Config rules to alert on unexpected invalidation patterns, such as wildcard invalidations.
- Enable CloudFront logging to track cache hits/misses post-invalidation and correlate with origin access.

## Objectives

1. Force CloudFront to invalidate and refresh specific cached files from the origin.
2. Optionally invalidate the entire distribution cache using a wildcard path.
3. Verify the invalidation status to confirm the cache refresh is in progress or complete.

## Instructions

### Step 1: Invalidate Specific File Paths

**Context**: This step targets individual files or paths (e.g., HTML error pages or specific assets) to refresh only the necessary cached objects, minimizing costs and scope. Obtain the Distribution ID from the AWS Console or CLI beforehand. The --paths parameter accepts multiple space-separated paths starting with /.

**Command** ([[commands/aws-cloudfront-create-invalidation-specific-paths]]):
```bash
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID --paths "/index.html" "/error.html"
```

> This command sends an invalidation request to CloudFront. Replace $DISTRIBUTION_ID with the actual ID (e.g., E123ABC456DEF) and specify the exact paths. The request returns immediately with an Invalidation ID; the status starts as 'InProgress' and changes to 'Completed' after propagation (typically minutes to hours, depending on global edge locations). Check status later with aws cloudfront get-invalidation --distribution-id $DISTRIBUTION_ID --id $INVALIDATION_ID.

### Step 2: Invalidate All Paths with Wildcard

**Context**: Use this step to clear the entire cache when broad refresh is needed, such as after widespread modifications to the origin content. The wildcard path '/*' invalidates everything under the distribution root. Note that this counts as 1,000 paths toward monthly quotas, so it's expensive.

**Command** ([[commands/aws-cloudfront-create-invalidation-all-paths-wildcard]]):
```bash
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID --paths "/*"
```

> Execute this to trigger a full cache purge. The output provides an Invalidation ID for tracking. Monitor completion via the AWS Console (CloudFront > Distributions > Invalidations) or CLI. In a red team scenario, this ensures any updated malicious payloads are immediately available via the CDN without stale cache interference.
