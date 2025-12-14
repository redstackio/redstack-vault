---
id: cmd-001
data: >-
  curl
  "https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html"
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.176Z'
verified: false
validated: true
submitted: true
---
# curl-query-arcgis

## Command

```bash
curl "https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html"
```

## Description

This curl command fetches the default ArcGIS query endpoint in HTML format, displaying the form for parameter inspection. Use it to baseline the interface before SQL injection testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target ArcGIS query endpoint with default params | Yes |
| -s | Silent mode (optional) | No |
| -o | Output to file (optional) | No |

## Examples

### Basic Usage

```bash
curl "https://target/arcgis/.../query?..."
```

### Advanced Usage

```bash
curl -s -o form.html "https://target/arcgis/.../query?..."
```

## Expected Output

HTML page with query form, including 'where' input field and parameter list. No data returned initially.

## Related

- [[Related Procedure: Access-ArcGIS-Query-Endpoint]]
