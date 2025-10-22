---
id: 18439cf0-22e1-4e2e-949d-b23b091adc14
name: Return Hello World
type: command
executor: bash
data: public String index(@RequestHeader(\"X-Api-Version\") String apiVersion) {\n    logger.info(\"Received
  a request for API version \" + apiVersion);\n    return \"Hello, world!\";\n}
output: null
created_at: '2023-04-06T03:55:56.458315+00:00'
updated_at: '2023-04-06T03:55:56.468011+00:00'
---

# Return Hello World

```bash
public String index(@RequestHeader(\"X-Api-Version\") String apiVersion) {\n    logger.info(\"Received a request for API version \" + apiVersion);\n    return \"Hello, world!\";\n}
```
