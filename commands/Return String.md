---
id: c55279d9-37bc-49aa-8c33-29ca2c2fc6ce
name: Return String
type: command
executor: bash
data: public String index(@RequestHeader(\"X-Api-Version\") String apiVersion) {\n    logger.info(\"Received
  a request for API version \" + apiVersion);\n    return \"Hello, world!\";\n}
output: null
created_at: '2023-04-06T03:55:56.633643+00:00'
updated_at: '2023-04-06T03:55:56.643524+00:00'
---

# Return String

```bash
public String index(@RequestHeader(\"X-Api-Version\") String apiVersion) {\n    logger.info(\"Received a request for API version \" + apiVersion);\n    return \"Hello, world!\";\n}
```
