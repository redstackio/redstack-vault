---
id: 0e78decb-4ac9-43da-aed6-d96c19b4cbe7
name: neo4j-launch-console
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
  - neo4j
verified: true
validated: true
---

# neo4j-launch-console

## Command

```cmd
neo4j.bat console
```

## Description

This command launches the Neo4j database server in console mode, which is required for running BloodHound. It starts the server in the foreground, displaying logs and enabling the Bolt protocol on port 7687 and the HTTP interface on port 7474. Use this from the Neo4j bin directory after extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| console | Runs Neo4j in console/foreground mode for development and testing. | Yes |

No additional parameters are needed for basic launch; advanced options like --home or --config can be added if customizing the Neo4j home directory.

## Examples

### Basic Usage

Navigate to the Neo4j bin directory and run:

```cmd
cd C:\neo4j\bin
neo4j.bat console
```

### Advanced Usage

Launch with a custom config:

```cmd
neo4j.bat console --config neo4j.conf
```

## Expected Output

The command outputs startup logs indicating the server status:

```
PS C:\Users\Victim\Desktop\neo4j-community-4.0.1\bin> .\neo4j.bat console
2020-03-09 21:13:06.960+0000 INFO  ======== Neo4j 4.0.1 ========
2020-03-09 21:13:06.967+0000 INFO  Starting...
2020-03-09 21:13:13.508+0000 INFO  Bolt enabled on localhost:7687.
2020-03-09 21:13:13.511+0000 INFO  Started.
2020-03-09 21:13:13.937+0000 WARN  The client is unauthorized due to authentication failure.
2020-03-09 21:13:14.743+0000 INFO  Remote interface available at http://localhost:7474/
```

Success is indicated by 'Started.' and the availability of the remote interface. Access the browser at http://localhost:7474 to complete setup.

## Related

- [[tools/BloodHound]]
- [[neo4j-stop]] (for stopping the instance)
