---
id: 2ea133ce-c10c-4468-be91-b5db2e7745fa
name: Enumerate-Network-ACLs-for-RDS-Instances
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.411030+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Listing-Network-ACLs]]'
  - '[[tags/RDS-Relational-Database-Service]]'
  - aws
  - cloud-enumeration
commands:
  - '[[commands/aws-rds-describe-db-instances]]'
  - '[[commands/aws-ec2-describe-subnets]]'
  - '[[commands/aws-ec2-describe-network-acls]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-Network-ACLs-for-RDS-Instances

## Summary

This procedure uses AWS CLI commands to enumerate network access control lists (ACLs) associated with subnets hosting RDS instances. By identifying these ACLs, an attacker can map the network topology, discover permissive rules allowing inbound/outbound traffic, and identify potential entry points for lateral movement or data exfiltration in an AWS environment.

## Description

Network ACLs act as stateless firewalls at the subnet level in AWS VPCs, controlling traffic to and from resources like RDS database instances. This procedure starts by querying RDS instance details to retrieve associated subnet IDs, then maps those subnets to their network ACLs, and finally retrieves the detailed rules of the ACLs. It requires AWS credentials with read access to RDS and EC2 services. In an attack scenario, this enumeration helps discover misconfigurations, such as overly permissive rules (e.g., allowing RDP or SSH from anywhere), which could facilitate further exploitation. The technique aligns with cloud environment discovery, revealing infrastructure details without direct interaction with the RDS database itself.

## Requirements

1. [[tools/AWS-CLI]] installed and configured with credentials (e.g., access key ID and secret access key) that have permissions for `rds:DescribeDBInstances`, `ec2:DescribeSubnets`, and `ec2:DescribeNetworkAcls` (such as AmazonEC2ReadOnlyAccess and AmazonRDSReadOnlyAccess policies).
2. Network connectivity to AWS APIs (no direct VPC access needed, but credentials must be for the target account).
3. Knowledge of the target RDS instance identifier (DBInstanceIdentifier) or ability to list all instances if broad enumeration is permitted.

## Defense

- Implement least privilege access in IAM: Restrict `Describe*` API calls to authorized roles only and use conditions to limit to specific resources.
- Enable AWS CloudTrail logging for RDS and EC2 APIs to detect anomalous enumeration queries, such as repeated `describe-network-acls` calls from unusual IPs.
- Use VPC flow logs and GuardDuty to monitor for suspicious API activity tied to credential compromise.

## Objectives

1. Identify subnets associated with target RDS instances.
2. Retrieve network ACL IDs linked to those subnets.
3. Enumerate detailed rules in the network ACLs to assess traffic controls and potential vulnerabilities.

## Instructions

### Step 1: Retrieve RDS Instance Subnet Details

**Context**: Begin by querying the RDS service to obtain the subnet group and identifiers for the target RDS instance. This step identifies the VPC subnets where the database is deployed, which are controlled by network ACLs. Use the DB instance identifier if known; otherwise, omit for a full list (requires broader permissions).

**Command** ([[commands/aws-rds-describe-db-instances]]):
```bash
aws rds describe-db-instances --db-instance-identifier $_DB_INSTANCE_ID --region $_AWS_REGION
```

> This command returns a JSON response with the `DBSubnetGroup` field containing `SubnetIdentifiers`. Note the subnet IDs (e.g., subnet-12345678) for the next step. If no specific instance is targeted, run without `--db-instance-identifier` to list all RDS instances and their subnets. Success is indicated by a 200 OK response with JSON data; errors like AccessDenied suggest insufficient permissions.

### Step 2: Map Subnets to Network ACL Associations

**Context**: Using the subnet IDs from Step 1, query EC2 to get subnet details, including the associated network ACL ID. This links the RDS hosting infrastructure to its traffic controls. If multiple subnets are involved (e.g., for high availability), repeat for each.

**Command** ([[commands/aws-ec2-describe-subnets]]):
```bash
aws ec2 describe-subnets --subnet-ids $_SUBNET_ID --region $_AWS_REGION
```

> The response includes `NetworkAclAssociationSet` with the `NetworkAclId` (e.g., acl-12345678). Extract this ID for the final step. Verify by checking the `AvailabilityZone` matches the RDS deployment. A successful output lists the subnet details without errors; if the subnet is not found, confirm the ID from Step 1.

### Step 3: Retrieve Network ACL Rules and Details

**Context**: With the network ACL ID, fetch the full configuration, including inbound/outbound rules, to analyze permissions. This reveals allowed protocols, ports, and CIDR blocks, potentially exposing weak configurations like unrestricted access to RDS ports (e.g., 3306 for MySQL).

**Command** ([[commands/aws-ec2-describe-network-acls]]):
```bash
aws ec2 describe-network-acls --network-acl-ids $_NETWORK_ACL_ID --region $_AWS_REGION
```

> The JSON output details `Entries` for rules (e.g., rule numbers, ports, protocols, CIDR blocks) and `Associations` confirming subnet links. Look for low rule numbers (e.g., 100) with broad allows (*/*). Success is a complete rule set; pipe to `jq` for parsing if needed (e.g., `| jq '.NetworkAcls[0].Entries[]'`). If the ACL ID is invalid, you'll get a 400 error.
