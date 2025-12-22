---
id: 7159b747-083e-4f86-9648-369fe4e37b53
name: rds-lateral-movement-via-vpc-peering-connections
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.434883+00:00'
updated_at: '2023-10-10T20:20:49.206858+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Lateral Movement and Pivoting]]'
  - '[[tags/Listing VPC peering connections]]'
  - '[[tags/RDS - Relational Database Service]]'
  - '[[tags/AWS]]'
  - '[[tags/Scenario]]'
commands:
  - '[[commands/aws-ec2-describe-vpc-peering-connections]]'
  - '[[commands/nmap-scan-connected-vpc-cidrs]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
  - '[[tools/Nmap]]'
validated: true
---

# RDS Lateral Movement via VPC Peering Connections

## Summary

This procedure enables attackers with AWS API access to discover VPC peering connections, identify linked VPCs, and pivot laterally to access RDS instances in peered networks. By enumerating peering connections and scanning associated CIDR blocks, attackers can map the network topology and target exposed database services for exploitation, facilitating data exfiltration or further compromise.

## Description

Amazon RDS (Relational Database Service) is a managed database offering in AWS. VPC peering connections enable private connectivity between VPCs across accounts or regions, allowing traffic to flow as if within the same network. An attacker with compromised credentials in one VPC can use this procedure to list peering connections, determine connected VPCs and their CIDR ranges, and then scan for open services like RDS endpoints (typically on port 3306 for MySQL, 5432 for PostgreSQL, etc.). This supports lateral movement by identifying pivot points to RDS instances, potentially leading to unauthorized database access. The technique assumes API access via AWS CLI and network reachability within the peered VPCs. It maps to MITRE ATT&CK for discovery of network infrastructure and remote service exploitation.

## Requirements

1. Valid AWS credentials with permissions to call EC2 API operations (e.g., `ec2:DescribeVpcPeeringConnections`).
2. AWS CLI installed and configured with the target account's access key and secret key.
3. Network access from the attacker's position to instances or endpoints in the peered VPCs (e.g., via a compromised EC2 instance).
4. Knowledge of the target VPC ID or region to filter results.

## Defense

- Implement least-privilege IAM policies to restrict `ec2:DescribeVpcPeeringConnections` and related APIs.
- Monitor CloudTrail logs for unusual API calls from EC2 instances or IAM users.
- Use VPC flow logs and GuardDuty to detect anomalous network scanning or peering enumeration.
- Segment RDS instances with security groups and NACLs limiting access to trusted CIDRs only.

## Objectives

1. Enumerate active VPC peering connections to map connected networks.
2. Identify CIDR blocks of peered VPCs for targeted scanning.
3. Scan peered networks for exposed RDS services to enable lateral movement and database access.

## Instructions

### Step 1: Configure AWS CLI and List VPC Peering Connections

**Context**: Begin by ensuring AWS CLI is set up with credentials for the compromised account. Use the describe command to retrieve details on VPC peering connections, including accepter/requester VPC IDs, CIDR blocks, and status. This reveals potential pivot targets.

**Command** ([[commands/aws-ec2-describe-vpc-peering-connections]]):
```bash
aws ec2 describe-vpc-peering-connections --region $_AWS_REGION --vpc-id $_TARGET_VPC_ID
```

This command queries the EC2 API for peering connections associated with the specified VPC. Filter by region and VPC ID to narrow results. Expected output includes JSON with peering connection details like `VpcPeeringConnectionId`, `AccepterVpcInfo`, `RequesterVpcInfo`, and `Status`. Parse the JSON (e.g., using jq) to extract connected VPC IDs and CIDRs for further steps.

### Step 2: Extract Connected VPC CIDRs

**Context**: From the peering connection output, identify the CIDR blocks of connected VPCs. This provides the network ranges to scan for services. If multiple connections exist, prioritize active ones (status: 'active').

**Command** (use jq for parsing, assuming installed):
```bash
aws ec2 describe-vpc-peering-connections --region $_AWS_REGION --vpc-id $_TARGET_VPC_ID | jq '.VpcPeeringConnections[].AccepterVpcInfo.CidrBlock'
```

This extracts CIDR blocks from the JSON response. Expected output: A list of CIDR strings (e.g., "10.0.0.0/16"). Save these to a file for the next scanning step. If no jq, manually review the JSON or use AWS CLI's `--query` option: `aws ec2 describe-vpc-peering-connections --query 'VpcPeeringConnections[].AccepterVpcInfo.CidrBlock' --output text`.

### Step 3: Scan Connected VPCs for RDS Services

**Context**: With CIDR ranges identified, perform network scanning from a compromised instance in the source VPC to discover open ports and services in peered VPCs. Focus on common RDS ports (e.g., 3306, 5432) to locate database instances for lateral movement.

**Command** ([[commands/nmap-scan-connected-vpc-cidrs]]):
```bash
nmap -sV -p 3306,5432,1433 $_CONNECTED_CIDRS --open
```

Run this from an EC2 instance with outbound access to peered networks. The scan probes for RDS-related services. Expected output: Host discovery with service versions (e.g., "3306/tcp open mysql | MySQL 5.7"). Success confirms exposed RDS endpoints; proceed to connect using database credentials or further exploits.

### Step 4: Verify RDS Access and Pivot

**Context**: For discovered RDS endpoints, attempt connection using known credentials or default configs. This completes the lateral movement by querying or exfiltrating data from the database.

**Command** (example MySQL client connection):
```bash
mysql -h $_RDS_ENDPOINT -u $_DB_USER -p$_DB_PASSWORD
```

Replace placeholders with endpoint from scan and any obtained creds. Expected output: Successful login prompt or query results. If access granted, execute SQL commands to dump data or escalate.
