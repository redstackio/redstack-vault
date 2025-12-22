---
type: command
executor: bash
data: aws gamelift describe-matchmaking-rule-sets
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - gamelift
  - discovery
verified: true
validated: true
---

# aws-gamelift-describe-matchmaking-rule-sets

## Command

```bash
aws gamelift describe-matchmaking-rule-sets
```

## Description

Describes all matchmaking rule sets in AWS GameLift. Verifies read access to game matchmaking configurations, part of broader service discovery in IAM enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters required | No |

## Examples

### Basic Usage

```bash
aws gamelift describe-matchmaking-rule-sets
```

## Expected Output

JSON {"RuleSets": [{"RuleSetName": "MyRules", "RuleSetBody": "..."}]}. Errors on denial.

## Related

- [[procedures/AWS-IAM-Permissions-Enumeration]]
