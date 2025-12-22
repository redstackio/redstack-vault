---
id: 235c11d2-3486-493c-8ef4-d79b7b327987
name: aws-rds-describe-db-proxies
type: command
executor: bash
data: aws rds describe-db-proxies
output: null
created_at: '2023-04-06T03:56:13.939873+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - rds
  - discovery
verified: true
validated: true
---

# aws-rds-describe-db-proxies

## Command

```bash
aws rds describe-db-proxies $_DB_PROXY_NAME --region $_REGION --output $_OUTPUT_FORMAT
```

## Description

This command retrieves detailed information about one or all RDS database proxies in the specified AWS region. It is used for discovering proxy configurations, endpoints, and associated resources during reconnaissance or auditing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DB_PROXY_NAME | The name of a specific DB proxy to describe (omit for all proxies) | No |
| --region $_REGION | AWS region (e.g., us-east-1); defaults to configured region | No |
| --output $_OUTPUT_FORMAT | Output format (json, table, text); defaults to json | No |
| --query $_QUERY | JMESPath query to filter output (e.g., 'DBProxies[].DBProxyName') | No |

## Examples

### Basic Usage

```bash
aws rds describe-db-proxies
```

Lists all proxies in the default region.

### Advanced Usage

```bash
aws rds describe-db-proxies --db-proxy-name my-proxy --region us-west-2 --output table
```

Describes a specific proxy in a given region with table-formatted output.

## Expected Output

Successful execution returns a JSON structure like:

```json
{
  "DBProxies": [
    {
      "DBProxyName": "my-proxy",
      "Status": "available",
      "Endpoint": "my-proxy.proxy-abc123.us-east-1.rds.amazonaws.com",
      "EngineFamily": "MYSQL",
      "VpcSecurityGroupIds": ["sg-12345678"],
      "Auth": [...]
    }
  ]
}
```

If no proxies exist, "DBProxies" is an empty array. Errors include permission denied or invalid region.

## Related

- [[procedures/Enumerate-RDS-Database-Proxies]]
- [[commands/aws-rds-describe-db-instances]]
