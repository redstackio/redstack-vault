---
id: 47ef6c68-ea61-45c3-9db9-fe92730bb0e7
name: Neo4j
type: tool
verified: true
created_at: '2020-03-12T21:04:39.211694+00:00'
updated_at: '2023-05-30T01:07:27.396827+00:00'
platforms:
  - Linux
  - Windows
tags:
  - database
  - graph-database
url: 'https://neo4j.com/'
validated: true
---

# Neo4j

**Status**: ✓ Verified

## Overview

Neo4j is a high-performance graph database that stores data using nodes and relationships instead of traditional tables. It is widely used in security operations for modeling complex relationships, such as attack paths in MITRE ATT&CK frameworks, threat intelligence analysis, and network mapping during red team engagements.

## Description

Neo4j provides robust features for querying graph data with Cypher, its declarative query language. In offensive security, it can be used to visualize and analyze reconnaissance data, privilege escalation chains, or lateral movement patterns. It supports ACID transactions, high availability clustering, and integrates with tools like BloodHound for Active Directory graph analysis.

## Features

- Graph storage with native nodes and relationships for efficient traversal
- Cypher query language for complex pattern matching
- Bolt protocol for high-speed data access
- Web-based browser interface for visualization
- Plugins and extensions for security-specific use cases (e.g., ATT&CK navigator integration)

## Installation

### Requirements

- Java SE 11 or later (Neo4j requires a compatible JDK)
- At least 2GB RAM for basic operations
- Administrative privileges for installation

### Install Commands

#### Linux (Ubuntu/Kali)

```bash
sudo apt update
sudo apt install neo4j
sudo systemctl start neo4j
```

Alternatively, download the tarball from the official site and extract:

```bash
wget https://neo4j.com/download/community-edition
# Extract and set JAVA_HOME
export JAVA_HOME=/path/to/java
bin/neo4j start
```

#### Windows

1. Download and install Java SE 11 from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html) or use the archive from [JDK Archive](https://jdk.java.net/archive/) to avoid sign-up. Set JAVA_HOME environment variable to the Java installation directory.

2. Download Neo4j Community Edition from [Neo4j Download Center](https://neo4j.com/download-center/#community).

3. Extract the archive to a directory (e.g., C:\neo4j).

## Basic Usage

After installation, launch Neo4j in console mode to run it in the foreground. Access the web interface at http://localhost:7474.

Default credentials: neo4j/neo4j (change on first login).

### Common Options

| Option | Description |
|--------|-------------|
| `console` | Run Neo4j in foreground console mode |
| `start` | Start Neo4j as a background service |
| `stop` | Stop the running Neo4j instance |
| `status` | Check the status of the Neo4j service |

## Examples

### Example 1: Launch on Windows

Navigate to the bin directory and run:

See [[commands/neo4j-launch-windows-console]] for details.

### Example 2: Launch on Linux

```bash
cd /usr/share/neo4j/bin
./neo4j console
```

See [[commands/neo4j-launch-linux-console]] for details.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for graph-based reconnaissance modeling)
- [[System Information Discovery]] System Information Discovery (for mapping relationships)

### Tactics

- [[Impact]] Impact (data analysis in post-exploitation)
- [[Discovery]] Discovery (relationship discovery in networks)

## Detection

- Monitor for Java processes spawning neo4j.jar or bin/neo4j executables
- Network traffic on ports 7474 (HTTP) or 7687 (Bolt)
- Logins to localhost:7474 from security tools
- Unusual graph queries in Cypher logs for sensitive data patterns

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/BloodHound]] (Active Directory graph analysis)
- [[Graphistry]] (graph visualization)

## References

- Official Documentation: https://neo4j.com/docs/
- Cypher Manual: https://neo4j.com/docs/cypher-manual/current/
- Security Use Cases: https://neo4j.com/use-cases/security-intelligence/
