---
tags:
  - azure
  - cloud-takeover
  - registration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Azure
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.692Z'
sub_techniques: []
id: 39456a94-23e9-472e-b799-1593ef3ba734
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Unclaimed-Azure-VM

## Summary

This procedure claims an unclaimed Azure Cloud App Virtual Machine, redirecting subdomain traffic to the attacker's controlled instance for full OS and network access.

## Description

After verification, register feuscspma3fcvapi.eastus.cloudapp.azure.com in the Azure portal. This grants control over the VM's OS, allowing traffic interception for the linked subdomain. Requires an Azure account; outcomes include DNS propagation to the new VM, enabling exploits like phishing.

## Requirements

1. Valid Azure subscription (free tier works)
2. Portal access with registration permissions
3. Target resource name and region confirmed

## Defense

Defensive measures and detection strategies:

- Audit and delete dangling cloud resources regularly
- Use Azure Policy to restrict VM creation in legacy namespaces
- Monitor for new registrations matching old DNS pointers

## Objectives

1. Secure ownership of the unclaimed VM
2. Configure VM to handle subdomain traffic
3. Enable OS-level access for further exploitation

## Instructions

### Step 1: Initiate Registration in Azure Portal

**Context**: Log in and claim the available resource.

No CLI; use Azure portal: Go to Virtual Machines > Create > Select Cloud App > Enter feuscspma3fcvapi.eastus.cloudapp.azure.com.

> Portal confirms registration; VM becomes active under your account.

### Step 2: Configure VM Networking and OS

**Context**: Set up the VM to receive and process traffic.

Post-registration, SSH/RDP into VM and install web server/email handlers.
```bash
# Example: Install Apache on Linux VM
apt update && apt install apache2
```

> Ensure ports 80/443/25 open; traffic from subdomain now routes here.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- [[azure]]
- [[cloud-takeover]]
- [[registration]]
