---
id: ed3264d5-292f-4362-a5ac-68cfa7549eae
name: aws-ec2-describe-network-acls
type: command
executor: bash
data: >-
  aws ec2 describe-network-acls --network-acl-ids $_NETWORK_ACL_ID --region
  $_AWS_REGION
output: null
created_at: '2023-04-06T03:56:14.406297+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - ec2
  - network-acl
verified: true
validated: true
---

# aws-ec2-describe-network-acls

## Command

```bash
aws ec2 describe-network-acls --network-acl-ids $_NETWORK_ACL_ID --region $_AWS_REGION
```

## Description

This command lists details of network ACLs in an AWS account, including rules for inbound and outbound traffic. It is used to enumerate security configurations for VPC subnets, such as those hosting RDS instances, to identify permissive rules.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--network-acl-ids` ($_NETWORK_ACL_ID) | Comma-separated list of ACL IDs (e.g., acl-12345678). Omit for all ACLs. | No |
| `--region` ($_AWS_REGION) | AWS region (e.g., us-east-1). | No |
| `--filters` | Filters like Name=association.subnet-id,Values=subnet-abc123 to scope results. | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-network-acls --region us-east-1
```

### Specific ACL

```bash
aws ec2 describe-network-acls --network-acl-ids acl-12345678 --region us-west-2
```

## Expected Output

JSON example:

```json
{
  "NetworkAcls": [
    {
      "NetworkAclId": "acl-12345678",
      "Entries": [
        {
          "RuleNumber": 100,
          "Protocol": "-1",
          "PortRange": {"From": 0, "To": 65535},
          "CidrBlock": "0.0.0.0/0",
          "Egress": false,
          "RuleAction": "allow"
        }
      ]
    }
  ]
}
```

Review `Entries` for allow rules on sensitive ports. Empty results indicate no matching ACLs.

## Related

- [[procedures/Enumerate-Network-ACLs-for-RDS-Instances]]
- [[commands/aws-ec2-describe-subnets]]
