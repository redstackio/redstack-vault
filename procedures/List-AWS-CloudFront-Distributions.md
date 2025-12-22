---
id: d8a07911-d9f8-4100-9181-cb160da767d6
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:16.157383+00:00'
updated_at: '2023-05-25T20:07:17.295732+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Cloud Infrastructure Discovery|T1589 - Cloud Infrastructure
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/AWS]]'
  - '[[tags/Cloud]]'
commands:
  - '[[commands/aws-cloudfront-list-distributions]]'
  - '[[commands/aws-configure-set-cloudfront-preview]]'
platforms:
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# List-AWS-CloudFront-Distributions

## Summary

This procedure lists all AWS CloudFront distributions associated with the account, revealing external endpoints, custom domains, subdomains, and linked internal resources such as S3 buckets or EKS clusters. It is useful during reconnaissance to map the cloud infrastructure and identify potential attack surfaces or data exposure points.

## Description

AWS CloudFront is a content delivery network (CDN) service that accelerates content delivery using edge locations. Distributions represent the configuration for how content is delivered, including origins (e.g., S3 buckets, EC2 instances, or custom servers). By enumerating distributions, attackers or testers can discover public-facing URLs, alternate domain names (CNAMEs), and backend resources, which may expose sensitive data or misconfigurations. This technique aligns with cloud discovery phases in red team engagements, helping to understand the target's web infrastructure without direct network scanning.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., access key and secret key with read permissions on CloudFront).
2. Appropriate IAM permissions: cloudfront:ListDistributions (and optionally cloudfront:GetDistribution for details).
3. Network access to AWS APIs (no VPC endpoints required for basic listing).
4. Optional: Enable CloudFront preview features for advanced querying if needed.

## Defense

- Monitor CloudTrail logs for API calls to CloudFront:ListDistributions and set alerts for unusual access patterns.
- Implement least-privilege IAM policies to restrict ListDistributions to necessary roles.
- Use AWS Config rules to detect overly permissive CloudFront configurations exposing internal resources.
- Enable GuardDuty for cloud API activity monitoring.

## Objectives

1. Enumerate all CloudFront distributions to identify external domains and endpoints.
2. Reveal linked internal assets (e.g., S3 origins) for further enumeration.
3. Map the CDN infrastructure to support targeted attacks on web delivery points.
4. Validate success by confirming distribution details without errors.

## Instructions

### Step 1: (Optional) Enable CloudFront Preview Features

**Context**: Enabling preview mode in AWS CLI allows access to beta or preview features for CloudFront, which may provide additional output fields or options during listing. This step is optional but recommended if the standard list command yields incomplete results due to feature flags.

**Command** ([[commands/aws-configure-set-cloudfront-preview]]):
```bash
aws configure set preview.cloudfront true
```

> This command updates the AWS CLI configuration file (~/.aws/config) to enable CloudFront previews. No output is returned on success; verify by running `aws configure get preview.cloudfront` which should return `true`. If already enabled, this step can be skipped to avoid unnecessary reconfiguration.

### Step 2: List CloudFront Distributions

**Context**: Retrieve a list of all CloudFront distributions, including their IDs, domains, and origins. This reveals the CDN structure and potential entry points for further exploitation, such as origin misconfigurations.

**Command** ([[commands/aws-cloudfront-list-distributions]]):
```bash
aws cloudfront list-distributions
```

> The command queries the CloudFront API and returns a JSON array of distributions. Parse the output for fields like `Id`, `DomainName`, `Aliases` (CNAMEs), and `Origins` to identify assets. Use `--query` for filtering if needed (e.g., `aws cloudfront list-distributions --query 'DistributionList.Items[*].{Id:Id,Domain:DomainName}'`). Success is indicated by a 200 OK response with non-empty `Quantity` in the output.
