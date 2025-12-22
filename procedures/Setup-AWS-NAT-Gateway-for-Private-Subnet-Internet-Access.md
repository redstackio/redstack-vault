---
type: procedure
description: >-
  Configures a NAT Gateway in AWS to enable outbound internet access from
  instances in a private subnet, facilitating data exfiltration or command and
  control operations.
verified: true
submitted: true
tactics:
  - '[[Persistence]]'
techniques:
  - '[[T1078.004]]'
sub_techniques: []
tags:
  - aws
  - cloud
  - nat-gateway
  - exfiltration
  - persistence
commands:
  - '[[commands/aws-ec2-allocate-elastic-ip-in-vpc]]'
  - '[[commands/aws-ec2-create-nat-gateway-in-subnet]]'
  - '[[commands/aws-ec2-create-route-to-nat-gateway]]'
platforms:
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# Setup-AWS-NAT-Gateway-for-Private-Subnet-Internet-Access

## Summary

This procedure sets up a NAT Gateway in an AWS VPC to provide outbound internet access to resources in a private subnet. It is useful in post-compromise scenarios where an attacker with valid AWS credentials needs to enable data exfiltration or C2 communications from air-gapped or private environments without exposing the instances directly to the internet.

## Description

In AWS, private subnets lack direct internet access by design for security. A NAT Gateway, placed in a public subnet, translates traffic from private instances to the internet while preventing inbound connections. This procedure allocates an Elastic IP, creates the NAT Gateway, and configures a route table entry to direct 0.0.0.0/0 traffic through the NAT. It assumes the attacker has IAM permissions for EC2 operations (e.g., ec2:AllocateAddress, ec2:CreateNatGateway, ec2:CreateRoute). The setup supports tactics like persistence via cloud resource modification and enables exfiltration over standard protocols.

## Requirements

1. Valid AWS credentials with EC2 permissions (e.g., AmazonEC2FullAccess policy or equivalent).
2. An existing VPC with at least one public subnet (for NAT placement) and one private subnet.
3. AWS CLI installed and configured with access keys (via `aws configure`).
4. Knowledge of the target region, public subnet ID, and private route table ID.

## Defense

- Monitor CloudTrail logs for EC2 API calls like AllocateAddress, CreateNatGateway, and CreateRoute.
- Implement least-privilege IAM policies to restrict NAT and route modifications.
- Use AWS Config rules to alert on unauthorized VPC changes.
- Enable VPC Flow Logs to detect unusual outbound traffic patterns post-setup.

## Objectives

1. Allocate a static Elastic IP for the NAT Gateway.
2. Deploy the NAT Gateway in a public subnet.
3. Update the private subnet's route table to route internet traffic via the NAT.
4. Verify outbound connectivity from private instances.

## Instructions

### Step 1: Allocate Elastic IP Address

**Context**: An Elastic IP provides a static public IP for the NAT Gateway, ensuring consistent outbound addressing and avoiding IP changes on restarts. This step uses the VPC domain to associate it within the target VPC.

**Command** ([[commands/aws-ec2-allocate-elastic-ip-in-vpc]]):
```bash
aws ec2 allocate-address --domain vpc --region $AWS_REGION
```

This command requests a new Elastic IP. Note the AllocationId from the output for the next step. If the quota is exceeded, request an increase via AWS support.

### Step 2: Create NAT Gateway

**Context**: The NAT Gateway is created in a public subnet using the allocated Elastic IP. It acts as the egress point for private subnet traffic, allowing outbound connections while blocking inbound.

**Command** ([[commands/aws-ec2-create-nat-gateway-in-subnet]]):
```bash
aws ec2 create-nat-gateway --subnet-id $AWS_SUBNET_ID --allocation-id $AWS_ALLOCATION_ID --region $AWS_REGION
```

This deploys the NAT in the specified public subnet. The status will initially be 'pending'; wait 5-10 minutes for 'available' before proceeding. Use `aws ec2 describe-nat-gateways` to check status.

### Step 3: Update Route Table for Private Subnet

**Context**: To enable internet access, add a default route (0.0.0.0/0) in the private subnet's route table pointing to the NAT Gateway. This directs all outbound traffic through the NAT without exposing private instances.

**Command** ([[commands/aws-ec2-create-route-to-nat-gateway]]):
```bash
aws ec2 create-route --route-table-id $ROUTE_TABLE_ID --destination-cidr-block 0.0.0.0/0 --nat-gateway-id $NAT_GATEWAY_ID --region $AWS_REGION
```

Replace $ROUTE_TABLE_ID with the private subnet's route table ID (find via `aws ec2 describe-route-tables`). The $NAT_GATEWAY_ID comes from Step 2's output. Verify with `aws ec2 describe-route-tables --route-table-ids $ROUTE_TABLE_ID` to confirm the route is 'active'.

### Step 4: Verify Setup

**Context**: Test outbound connectivity from a private subnet instance to ensure the NAT is functional. This confirms the setup allows exfiltration or C2 without direct exposure.

Launch or use an existing EC2 instance in the private subnet and run a simple curl command:
```bash
curl https://www.example.com
```

Success is indicated by a valid HTTP response. Monitor VPC Flow Logs for the traffic to confirm routing via the NAT IP.
