---
id: proc-xss-render-components-001
tags:
  - xss
  - react
  - rendering
type: procedure
tools:
  - '[[tools/react-autolinker-wrapper]]'
  - '[[tools/React]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/render-app-components]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.635Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Render-Input-and-Autolinker-Component

## Summary

This procedure implements the render method to display an input field linked to state and the AutolinkerWrapper component, allowing user input to flow into the vulnerable processing pipeline.

## Description

The render method returns JSX with an input element that triggers state updates on change and the AutolinkerWrapper receiving the text prop. In vulnerable apps, this leads to innerHTML setting without sanitization. Applies to browser-based React environments; assumes state initialization is complete.

## Requirements

1. Initialized state and event handler in the component
2. Imported AutolinkerWrapper
3. Running React dev server

## Defense

Defensive measures and detection strategies:

- Escape text props before rendering
- Avoid direct innerHTML in wrappers; use textContent
- Scan for Autolinker usage in dependency audits

## Objectives

1. Display interactive UI for input
2. Integrate vulnerable component into render cycle
3. Enable visual feedback for input processing

## Instructions

### Step 1: Implement Render Method

**Context**: Define the JSX structure to include input and wrapper components.

**Command** ([[commands/render-app-components]]):
```javascript
render(){
  return (
    <div className="App">
      <input placeholder="Place your link here" type="text" onChange={this.changeState}/>
      <AutolinkerWrapper text={this.state.text}/>
    </div>
  )
}
```

> Renders the UI. Expected output: Input field and wrapper appear; text links on benign input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/render-app-components]]

## Tools Used

- [[tools/react-autolinker-wrapper]]
- [[tools/React]]

## Tags

- xss
- react
- rendering
