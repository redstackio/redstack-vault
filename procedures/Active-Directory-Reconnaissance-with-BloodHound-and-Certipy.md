---
id: 2b9a8e82-66b5-46c3-b97c-80cfead2fd56
name: Active-Directory-Reconnaissance-with-BloodHound-and-Certipy
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:02.135872+00:00'
updated_at: '2023-10-10T20:26:14.170120+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Domain-Trust-Discovery|T1482 - Domain Trust Discovery]]'
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/Permission-Groups-Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Recon]]'
  - '[[tags/Using BloodHound]]'
commands:
  - '[[commands/certipy-find-bloodhound-data]]'
  - '[[commands/certipy-find-old-bloodhound-data]]'
  - '[[commands/certipy-find-vulnerable-certificates]]'
  - '[[commands/install-bloodhound-on-kali]]'
  - '[[commands/start-neo4j-console]]'
  - '[[commands/start-neo4j-with-docker]]'
  - '[[commands/run-bloodhound-application]]'
  - '[[commands/rusthound-gssapi-session]]'
  - '[[commands/rusthound-simple-bind-connection]]'
  - '[[commands/rusthound-adcs-module]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/Certipy]]'
  - '[[tools/BloodHound]]'
  - '[[tools/RustHound]]'
  - '[[tools/Neo4j]]'
validated: true
---

# Active-Directory-Reconnaissance-with-BloodHound-and-Certipy

## Summary

This procedure outlines how to perform comprehensive Active Directory reconnaissance using Certipy to identify vulnerable certificates and BloodHound (with RustHound for data collection) to map domain relationships and attack paths. It enables attackers to discover high-value targets, trust relationships, and potential privilege escalation vectors in an AD environment.

## Description

Active Directory reconnaissance involves enumerating domain objects, certificates, and relationships to identify weaknesses. Certipy exploits certificate services to find vulnerable or outdated certificates that could lead to privilege escalation. RustHound collects AD data in BloodHound format, which visualizes paths to domain admin. This is typically used post-initial access in a domain-joined environment to map the attack surface. The procedure assumes authenticated access and focuses on non-intrusive enumeration to avoid detection.

## Requirements

1. Authenticated domain credentials (username/password or Kerberos ticket)
2. Python 3 environment with Certipy installed ([[tools/Certipy]])
3. BloodHound and Neo4j installed or Docker access for setup ([[tools/BloodHound]], [[tools/Neo4j]])
4. RustHound binary for data collection ([[tools/RustHound]])
5. Network access to domain controllers (ports 88, 389, 636, 445 open)

## Defense

- Monitor certificate issuance and revocation logs in AD CS for anomalous requests
- Implement application whitelisting to block unauthorized BloodHound/RustHound execution
- Enable advanced auditing for LDAP queries and restrict anonymous binds
- Use network segmentation to limit lateral movement tools like Certipy

## Objectives

1. Identify vulnerable certificates and related AD objects for potential exploitation
2. Collect and visualize AD relationships to discover attack paths to high-value targets
3. Map domain trusts, groups, and permissions for privilege escalation planning

## Instructions

### Step 1: Enumerate BloodHound-Compatible Data with Certipy

**Context**: Use Certipy to query AD for certificate-related objects that can be ingested into BloodHound, revealing relationships like service principals and trusts.

**Command** ([[commands/certipy-find-bloodhound-data]]):
```bash
certipy find $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC -bloodhound
```

> This command searches for AD objects linked to certificates in BloodHound format. Replace placeholders with domain details. Expected output includes JSON files with nodes and edges for import into BloodHound.

### Step 2: Find Outdated Certificates with Certipy

**Context**: Identify legacy or misconfigured certificates that may allow unauthorized access or escalation.

**Command** ([[commands/certipy-find-old-bloodhound-data]]):
```bash
certipy find $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC -old-bloodhound
```

> This flags outdated certificates vulnerable to exploits. Output lists certificates with expiration dates and potential risks, exportable to BloodHound.

### Step 3: Locate Vulnerable Certificates with Certipy

**Context**: Specifically hunt for exploitable certificates, hiding admin accounts to focus on service accounts.

**Command** ([[commands/certipy-find-vulnerable-certificates]]):
```bash
certipy find $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC -vulnerable -hide-admins -username $_USERNAME -password $_PASSWORD
```

> Filters for vulnerable certs like ESC1/ESC4. Output details vulnerable templates, usernames, and hashes for cracking.

### Step 4: Collect AD Data Using RustHound GSSAPI Session

**Context**: On a Windows host with domain auth, use GSSAPI for stealthy data collection without explicit credentials.

**Command** ([[commands/rusthound-gssapi-session]]):
```bash
rusthound.exe -d $_DOMAIN --ldapfqdn $_LDAP_FQDN
```

> Leverages current session for LDAP queries. Output: ZIP file with BloodHound JSON data on users, groups, trusts.

### Step 5: Perform Simple Bind Data Collection with RustHound

**Context**: For Linux/Windows without tickets, use username/password for basic AD enumeration.

**Command** ([[commands/rusthound-simple-bind-connection]]):
```bash
rusthound.exe -d $_DOMAIN -u $_USERNAME@$_DOMAIN -p $_PASSWORD -o $_OUTPUT_DIR -z
```

> Compresses output for easy transfer. Generates BloodHound-compatible files on domain structure.

### Step 6: Collect ADCS Data with RustHound

**Context**: Target Active Directory Certificate Services for BloodHound @ly4k version, focusing on cert vulnerabilities.

**Command** ([[commands/rusthound-adcs-module]]):
```bash
rusthound -d $_DOMAIN -u '$_USERNAME@$_DOMAIN' -p '$_PASSWORD' -o $_OUTPUT_DIR --adcs -z
```

> Includes ADCS-specific edges. Output: Enhanced JSON with cert templates and paths.

### Step 7: Install BloodHound

**Context**: Set up BloodHound on a Kali-like system for visualization.

**Command** ([[commands/install-bloodhound-on-kali]]):
```bash
apt install bloodhound
```

> Installs BloodHound and dependencies. Verify with `bloodhound --version`.

### Step 8: Start Neo4j Database Console

**Context**: Launch the Neo4j backend for BloodHound data storage.

**Command** ([[commands/start-neo4j-console]]):
```bash
neo4j console
```

> Starts in foreground. Access at http://127.0.0.1:7474 with neo4j/bloodhound.

### Step 9: Start Neo4j with Docker (Alternative)

**Context**: Use Docker for isolated Neo4j instance if console fails.

**Command** ([[commands/start-neo4j-with-docker]]):
```bash
docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/bloodhound neo4j
```

> Maps ports for web and bolt access. Change password on first login.

### Step 10: Run BloodHound Application

**Context**: Launch the GUI to import and query collected data.

**Command** ([[commands/run-bloodhound-application]]):
```bash
./bloodhound --no-sandbox
```

> Opens Electron app. Connect to bolt://localhost:7687, import ZIP/JSON from prior steps, and run queries like Shortest Paths to Domain Admins.
