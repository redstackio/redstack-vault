---
id: 0e78decb-4ac9-43da-aed6-d96c19b4cbe7
name: neo4j-launch-windows-console
type: command
executor: cmd
data: neo4j.bat console
output: >-
  PS C:\Users\Victim\Desktop\neo4j-community-4.0.1\bin> .\neo4j.bat console

  2020-03-09 21:13:06.960+0000 INFO  ======== Neo4j 4.0.1 ========

  2020-03-09 21:13:06.967+0000 INFO  Starting...

  2020-03-09 21:13:13.508+0000 INFO  Bolt enabled on localhost:7687.

  2020-03-09 21:13:13.511+0000 INFO  Started.

  2020-03-09 21:13:13.937+0000 WARN  The client is unauthorized due to
  authentication failure.

  2020-03-09 21:13:14.743+0000 INFO  Remote interface available at
  http://localhost:7474/
created_at: '2020-03-23T21:16:50.675749+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - database
  - launch
verified: true
validated: true
---

# neo4j-launch-windows-console

## Command

```cmd
neo4j.bat console
```

## Description

Launches a Neo4j database instance in console mode on Windows, running in the foreground. This starts the graph database server, enabling the Bolt protocol on port 7687 and the HTTP interface on port 7474. Use this for development or testing environments where you need immediate feedback from startup logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `console` | Runs Neo4j in interactive console mode (foreground) | Yes |

No additional parameters are needed beyond navigating to the bin directory.

## Examples

### Basic Usage

From the Neo4j installation's bin directory (e.g., C:\neo4j\bin):

```cmd
neo4j.bat console
```

### With Environment Variables

Ensure JAVA_HOME is set before running:

```cmd
set JAVA_HOME=C:\Program Files\Java\jdk-11
neo4j.bat console
```

## Expected Output

```
PS C:\Users\Victim\Desktop\neo4j-community-4.0.1\bin> .\neo4j.bat console
2020-03-09 21:13:06.960+0000 INFO  ======== Neo4j 4.0.1 ========
2020-03-09 21:13:06.967+0000 INFO  Starting...
2020-03-09 21:13:13.508+0000 INFO  Bolt enabled on localhost:7687.
2020-03-09 21:13:13.511+0000 INFO  Started.
2020-03-09 21:13:13.937+0000 WARN  The client is unauthorized due to authentication failure.
2020-03-09 21:13:14.743+0000 INFO  Remote interface available at http://localhost:7474/
```

Success is indicated by "Started." and the availability of the remote interface. Access the browser at http://localhost:7474 and log in with default credentials (neo4j/neo4j), changing the password on first use.

## Related

- [[tools/Neo4j]] (parent tool)
- [[commands/neo4j-launch-linux-console]] (Linux equivalent)
