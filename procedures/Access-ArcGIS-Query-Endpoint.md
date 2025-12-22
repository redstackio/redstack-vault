---
id: proc-001
tags:
  - arcgis
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-query-arcgis]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.186Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-ArcGIS-Query-Endpoint

## Summary

This procedure accesses the ArcGIS Server query endpoint to load the web form, identifying the 'where' parameter for subsequent SQL injection testing. It serves as the initial reconnaissance step in exploiting ArcGIS vulnerabilities.

## Description

In the context of a public-facing ArcGIS Server instance, such as the U.S. Department of Defense's setup, navigating to the /query endpoint reveals an HTML form with parameters like 'where', 'outFields', and others. This form allows direct manipulation of SQL queries without authentication. The procedure confirms endpoint accessibility and parameter exposure, setting up for injection payloads. Expected outcomes include viewing the form and understanding the unsanitized input flow, as documented in Esri support for ArcGIS 10.1 SP1 blind SQLi issues.

## Requirements

1. Internet access to the target ArcGIS URL (e.g., https://█████/arcgis/rest/services/...)
2. Web browser or curl tool for HTTP requests
3. No credentials or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to block anomalous query parameters
- Enable ArcGIS Server logging for query endpoint access and monitor for unusual payloads
- Use parameterized queries in backend SQL to prevent injection

## Objectives

1. Load the query interface to inspect parameters
2. Confirm 'where' field availability for injection
3. Establish baseline for vulnerability testing

## Instructions

### Step 1: Fetch the Query Endpoint

**Context**: Send an HTTP GET request to the endpoint with default parameters to display the HTML form.

**Command** ([[commands/curl-query-arcgis]]):
```bash
curl "https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html"
```

> This command retrieves the HTML representation of the query form. Successful output shows the form with an empty 'where' field, indicating direct SQL input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-query-arcgis]]

## Tools Used


## Tags

- [[arcgis]]
- [[recon]]
