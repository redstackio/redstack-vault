---
id: b4369bb7-ce4b-4c5a-8b64-d5c2756c7ff1
name: netdom-trust-create-transitive
type: command
executor: cmd
data: 'netdom trust $_TRUSTING_DOMAIN /domain:$_TRUSTED_DOMAIN /ForestTransitive:Yes'
output: null
created_at: '2023-04-06T03:56:07.394167+00:00'
updated_at: '2023-04-10T20:26:01.511941+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - trust
verified: true
validated: true
---

# netdom-trust-create-transitive

## Command

```cmd
netdom trust $_TRUSTING_DOMAIN /domain:$_TRUSTED_DOMAIN /ForestTransitive:Yes
```

## Description

This command uses netdom to create a forest-transitive trust relationship between two Active Directory domains, allowing authentication to propagate across the entire forest. Use this as the first step in establishing bidirectional trusts for PAM scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TRUSTING_DOMAIN | The local domain establishing the trust (e.g., lab.local) | Yes |
| $_TRUSTED_DOMAIN | The remote domain to trust (e.g., bastion.local) | Yes |
| /ForestTransitive:Yes | Makes the trust transitive across forests | Built-in |

## Examples

### Basic Usage

```cmd
netdom trust lab.local /domain:bastion.local /ForestTransitive:Yes
```

### Reciprocal Usage

```cmd
netdom trust bastion.local /domain:lab.local /ForestTransitive:Yes
```

## Expected Output

The trust relationship between the domains has been established successfully.

The command completed successfully.

## Related

- [[procedures/Establish-and-Enumerate-PAM-Trust-Between-Domains]]
- [[commands/netdom-trust-enable-pam-options]]
