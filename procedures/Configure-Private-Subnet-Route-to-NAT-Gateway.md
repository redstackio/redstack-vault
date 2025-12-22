---
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:33.457118+00:00'
updated_at: '2023-05-25T20:07:30.574223+00:00'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Other Network Medium|T1011 - Exfiltration
    Over Other Network Medium]]
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/AWS]]'
  - '[[tags/Cloud]]'
commands:
  - '[[commands/aws-ec2-create-route-table]]'
  - '[[commands/aws-ec2-create-route-to-nat-gateway]]'
  - '[[commands/aws-ec2-associate-route-table-with-subnet]]'
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Configure-Private-Subnet-Route-to-NAT-Gateway

## Summary

This procedure enables internet access for instances in a private AWS subnet by creating a custom route table and directing outbound traffic through an existing NAT Gateway. It is particularly useful in scenarios requiring outbound connectivity from isolated environments, such as data exfiltration from compromised cloud resources without direct public exposure.

## Description

In AWS VPCs, private subnets lack direct internet access by default to enhance security. To allow outbound traffic (e.g., for updating malware or exfiltrating data), you can associate a route table with the private subnet that routes 0.0.0.0/0 traffic to a NAT Gateway in a public subnet. This setup ensures instances can initiate connections to the internet while preventing inbound access. The procedure assumes an existing NAT Gateway and VPC; it focuses on route table configuration. This aligns with exfiltration tactics by providing a controlled egress path in cloud environments.

## Requirements

1. AWS CLI installed and configured with credentials that have EC2 permissions (e.g., ec2:CreateRouteTable, ec2:CreateRoute, ec2:AssociateRouteTable).
2. Existing VPC ID, private subnet ID, NAT Gateway ID, and AWS region.
3. The NAT Gateway must be deployed in a public subnet with an Elastic IP.
4. Network access to run AWS CLI commands (e.g., from a bastion host or local machine with VPN).

## Defense

Defensive measures and detection strategies:

- Monitor CloudTrail logs for API calls like CreateRouteTable, CreateRoute, and AssociateRouteTable, especially from unexpected IAM principals.
- Use AWS Config rules to alert on unauthorized route table associations in private subnets.
- Implement VPC Flow Logs to detect unusual outbound traffic patterns from private subnets to NAT Gateways.
- Enforce least-privilege IAM policies to restrict EC2 route modifications to approved roles.

## Objectives

1. Create a dedicated route table for the private subnet to isolate routing configuration.
2. Add a default route (0.0.0.0/0) pointing to the NAT Gateway for outbound internet access.
3. Associate the route table with the target private subnet to apply the routing rules.
4. Enable controlled exfiltration or C2 communication from private instances without compromising subnet isolation.

## Instructions

### Step 1: Create Route Table

**Context**: Optionally create a new route table for the VPC if one does not exist. This provides a clean slate for routing rules specific to the private subnet, avoiding interference with existing public subnet routes.

**Command** ([[commands/aws-ec2-create-route-table]]):
```bash
aws ec2 create-route-table --vpc-id $AWS_VPC_ID --region $AWS_REGION
```

> This command creates a new route table associated with the specified VPC. Capture the returned RouteTableId for use in subsequent steps. If a suitable route table already exists, skip this step and use its ID.

### Step 2: Create Route to NAT Gateway

**Context**: Add a default route to the route table that directs all outbound traffic (0.0.0.0/0) to the NAT Gateway. This enables private instances to reach the internet via the NAT Gateway's Elastic IP, facilitating exfiltration while maintaining inbound isolation.

**Command** ([[commands/aws-ec2-create-route-to-nat-gateway]]):
```bash
aws ec2 create-route --route-table-id $AWS_ROUTE_TABLE_ID --destination-cidr-block 0.0.0.0/0 --nat-gateway-id $AWS_NAT_GATEWAY_ID --region $AWS_REGION
```

> Replace $IP_ADDRESS_CIDR with 0.0.0.0/0 for default internet routing. Success is indicated by a JSON response with "Return": true. Verify with `aws ec2 describe-route-tables` to confirm the route entry.

### Step 3: Associate Route Table with Subnet

**Context**: Link the configured route table to the private subnet, replacing any main route table association. This applies the NAT Gateway routing to all instances in the subnet, enabling outbound access.

**Command** ([[commands/aws-ec2-associate-route-table-with-subnet]]):
```bash
aws ec2 associate-route-table --route-table-id $AWS_ROUTE_TABLE_ID --subnet-id $AWS_SUBNET_ID --region $AWS_REGION
```

> This disassociates the subnet from its current route table (if any) and applies the new one. Capture the AssociationId for management. Test by launching an instance in the subnet and pinging an external host (e.g., 8.8.8.8) to verify outbound connectivity.
