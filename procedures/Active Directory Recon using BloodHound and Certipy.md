---
id: 2b9a8e82-66b5-46c3-b97c-80cfead2fd56
name: Active Directory Recon using BloodHound and Certipy
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.135872+00:00'
updated_at: '2023-04-10T20:26:14.170120+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Recon]]'
- '[[Using BloodHound]]'
commands:
- '[[Find Bloodhound Data]]'
- '[[Find Old Bloodhound Data]]'
- '[[Find Vulnerable Data]]'
- '[[Install BloodHound]]'
- '[[Linux with username:password and ADCS module]]'
- '[[Run BloodHound]]'
- '[[Start BloodHound and the database]]'
- '[[Use Docker]]'
- '[[Windows/Linux simple bind connection]]'
- '[[Windows with GSSAPI session]]'
---

# Active Directory Recon using BloodHound and Certipy

## Summary

Active Directory Recon using BloodHound and Certipy is a technique used by attackers to gain a deeper understanding of the target Active Directory environment. BloodHound is a tool used for visualizing and analyzing relationships within an Active Directory domain. Certipy is a Python tool used to e

## Description

# Description

Active Directory Recon using BloodHound and Certipy is a technique used by attackers to gain a deeper understanding of the target Active Directory environment. BloodHound is a tool used for visualizing and analyzing relationships within an Active Directory domain. Certipy is a Python tool used to exploit certificate-related vulnerabilities in the target environment. By combining these two tools, attackers can identify high-value targets within the domain and potentially gain access to sensitive information. This technique is commonly used in advanced persistent threat (APT) attacks.

From a technical perspective, this technique involves using Certipy to exploit certificate-related vulnerabilities in the target environment. Once access has been gained, BloodHound is used to visualize and analyze the relationships within the Active Directory domain. This allows attackers to identify high-value targets and potential attack paths.

From a business perspective, this technique can be used to gain access to sensitive information such as intellectual property, financial data, and customer information. This can result in reputational damage, legal liabilities, and financial losses for the target organization.

## Requirements

1. Authenticated access to the target Active Directory domain

1. Python installed with Certipy and BloodHound libraries

1. Network access to the target environment

## Defense

1. Implement least privilege access control to limit access to sensitive information

1. Regularly monitor and analyze Active Directory logs for suspicious activity

1. Implement certificate revocation to mitigate against Certipy attacks

## Objectives

1. Identify high-value targets within the target Active Directory domain

1. Gain access to sensitive information within the target environment

# Instructions

1. To use Certipy for certificate exploitation, use the following commands:
- certipy find 'target' -bloodhound
- certipy find 'target' -old-bloodhound
- certipy find 'target' -vulnerable -hide-admins -username user@domain -password Password123

Replace 'target' with the target server you want to exploit. 

The -bloodhound flag is used to search for Active Directory objects that are related to the target certificate. 

The -old-bloodhound flag is used to search for outdated certificates that may be vulnerable to exploitation. 

The -vulnerable flag is used to search for certificates that are vulnerable to exploitation. The -hide-admins flag is used to hide administrator accounts from the search results. The -username and -password flags are used to specify the credentials to use for the search.

**Code**: [[certipy find 'corp.local/john:Passw0rd@dc.corp.loc]]

> Certipy is a tool used for certificate exploitation. The 'find' command is used to search for certificates that may be vulnerable to exploitation. The 'target' parameter specifies the target server to search on. The -bloodhound flag searches for Active Directory objects related to the certificate. The -old-bloodhound flag searches for outdated certificates that may be vulnerable. The -vulnerable flag searches for certificates that are vulnerable to exploitation. The -hide-admins flag hides administrator accounts from the search results. The -username and -password flags are used to specify the credentials to use for the search.

**Command** ([[Find Bloodhound Data]]):

```bash
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -bloodhound
```

**Command** ([[Find Old Bloodhound Data]]):

```bash
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -old-bloodhound
```

**Command** ([[Find Vulnerable Data]]):

```bash
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -vulnerable -hide-admins -username user@domain -password Password123
```

2. The RustHound tool can be used to perform reconnaissance on a Windows domain. It supports simple bind connections with username and password, as well as GSSAPI sessions. It also has an ADCS module for BloodHound version @ly4k. The following commands can be used with RustHound:

**Code**: [[# Windows with GSSAPI session
rusthound.exe -d dom]]

> 1. `rusthound.exe -d domain.local --ldapfqdn domain`: This command is used to perform a GSSAPI session with the specified domain and LDAP FQDN.

2. `rusthound.exe -d domain.local -u user@domain.local -p Password123 -o output -z`: This command is used to perform a simple bind connection with the specified domain, username, and password. The output will be saved to the specified file path.

3. `rusthound -d domain.local -u 'user@domain.local' -p 'Password123' -o /tmp/adcs --adcs -z`: This command is used to perform a simple bind connection with the specified domain, username, and password, and also uses the ADCS module for BloodHound version @ly4k. The output will be saved to the specified file path.

**Command** ([[Windows with GSSAPI session]]):

```bash
rusthound.exe -d domain.local --ldapfqdn domain
```

**Command** ([[Windows/Linux simple bind connection]]):

```bash
rusthound.exe -d domain.local -u user@domain.local -p Password123 -o output -z
```

**Command** ([[Linux with username:password and ADCS module]]):

```bash
rusthound -d domain.local -u 'user@domain.local' -p 'Password123' -o /tmp/adcs --adcs -z
```

3. To install BloodHound, run the command 'apt install bloodhound'. After installation, start BloodHound and the database using the command 'neo4j console' or 'docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/bloodhound neo4j'. Then run the command './bloodhound --no-sandbox'. After starting BloodHound, go to http://127.0.0.1:7474, use db:bolt://localhost:7687, user:neo4J, pass:neo4j to access the application. To import zip/json files into the Neo4J database, use the appropriate import functionality within BloodHound.

**Code**: [[root@payload$ apt install bloodhound 

# start Blo]]

> This command installs BloodHound and provides instructions for starting the application and accessing it. It also explains how to import zip/json files into the Neo4J database and query them within the BloodHound application.

**Command** ([[Install BloodHound]]):

```bash
apt install bloodhound
```

**Command** ([[Start BloodHound and the database]]):

```bash
neo4j console
```

**Command** ([[Use Docker]]):

```bash
docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/bloodhound neo4j
```

**Command** ([[Run BloodHound]]):

```bash
./bloodhound --no-sandbox
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Find Bloodhound Data]]
- [[Find Old Bloodhound Data]]
- [[Find Vulnerable Data]]
- [[Install BloodHound]]
- [[Linux with username:password and ADCS module]]
- [[Run BloodHound]]
- [[Start BloodHound and the database]]
- [[Use Docker]]
- [[Windows/Linux simple bind connection]]
- [[Windows with GSSAPI session]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Recon]]
- [[Using BloodHound]]
