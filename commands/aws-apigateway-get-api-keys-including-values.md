---
id: 2f397be0-b792-4bf7-8f0e-e3061e1a02f8
name: aws-apigateway-get-api-keys-including-values
type: command
executor: bash
data: aws apigateway get-api-keys --include-values
output: null
created_at: '2023-04-06T03:56:11.484717+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tags:
  - cloud
  - enumeration
  - aws-cli
verified: true
validated: true
---

# aws-apigateway-get-api-keys-including-values

## Command

```bash
aws apigateway get-api-keys --include-values
```

## Description

This command queries the AWS API Gateway service to retrieve a list of all API keys associated with the account, including their secret values. It is used in discovery phases to enumerate credentials for potential reuse in API calls or further cloud attacks. Requires AWS CLI v2 and authenticated credentials with appropriate IAM permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--include-values` | Includes the secret API key values in the response (sensitive; use cautiously) | No (but recommended for full enumeration) |
| `$_REGION` | AWS region (default: us-east-1; set via `--region $_REGION` if needed) | No |
| `$_PROFILE` | AWS profile name (set via `--profile $_PROFILE` for multi-account setups) | No |

## Examples

### Basic Usage

```bash
aws apigateway get-api-keys --include-values
```

Retrieves keys in the default region.

### Advanced Usage

```bash
aws apigateway get-api-keys --include-values --region us-west-2 --profile compromised-account
```

Targets a specific region and profile.

### With Output Parsing

```bash
aws apigateway get-api-keys --include-values | jq '.items[] | select(.enabled == true) | {id: .id, value: .value}'
```

Filters for enabled keys only.

## Expected Output

JSON response with an `items` array containing API key details. Successful execution returns:
```
{
    "items": [
        {
            "id": "a1b2c3d4e5f6",
            "value": "sk-abcdefghijklmnopqrstuvwxyz1234567890",
            "enabled": true,
            "stageKeys": [
                {
                    "restApiId": "abc123",
                    "stageName": "prod"
                }
            ],
            "createdDate": 1696118400,
            "lastUpdatedDate": 1696204800
        }
    ],
    "position": "initial"
}
```

Empty `items` array indicates no keys. Errors (e.g., AccessDenied) suggest insufficient permissions.

## Related

- [[procedures/AWS API Key Enumeration]] (procedure using this command)
- [[commands/aws-sts-get-caller-identity]] (for credential verification)
