---
id: 0e78decb-4ac9-43da-aed6-d96c19b4cbe7
name: Launch a Neo4j Instance
type: command
executor: command_prompt
data: neo4j.bat console
output: 'PS C:\Users\Victim\Desktop\neo4j-community-4.0.1\bin> .\neo4j.bat console

  2020-03-09 21:13:06.960+0000 INFO  ======== Neo4j 4.0.1 ========

  2020-03-09 21:13:06.967+0000 INFO  Starting...

  2020-03-09 21:13:13.508+0000 INFO  Bolt enabled on localhost:7687.

  2020-03-09 21:13:13.511+0000 INFO  Started.

  2020-03-09 21:13:13.937+0000 WARN  The client is unauthorized due to authentication
  failure.

  2020-03-09 21:13:14.743+0000 INFO  Remote interface available at http://localhost:7474/'
created_at: '2020-03-23T21:16:50.675749+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Neo4j]]'
- '[[ps]]'
---

# Launch a Neo4j Instance

```command_prompt
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


