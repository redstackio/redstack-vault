---
id: proc-xss-setup-react-001
tags:
  - xss
  - react
  - setup
type: procedure
tools:
  - '[[tools/React]]'
  - '[[tools/react-autolinker-wrapper]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/import-react-and-autolinkerwrapper]]'
  - '[[commands/define-react-app-component]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.640Z'
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
# Set-Up-Vulnerable-React-Application

## Summary

This procedure sets up a basic React application that incorporates the vulnerable react-autolinker-wrapper component, enabling the demonstration of XSS through unsanitized user input processing.

## Description

In a client-side web application using React, import the react-autolinker-wrapper library (v1.1.0) which depends on Autolinker.js. This setup creates a foundation for injecting text that will be processed without sanitization, leading to innerHTML injection and JavaScript execution. The target environment is a Node.js-based React app running in a browser, with NPM for dependency management. Prerequisites include Node.js installed and a basic understanding of React components.

## Requirements

1. Node.js and NPM installed for package management
2. A code editor and browser for testing
3. Access to install react-autolinker-wrapper v1.1.0 via NPM

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before passing to Autolinker using libraries like DOMPurify
- Use React's dangerouslySetInnerHTML sparingly and with validation
- Monitor for unexpected script execution in browser dev tools

## Objectives

1. Establish a working React component structure for vulnerability testing
2. Integrate the vulnerable library to process text inputs
3. Prepare for payload injection without immediate execution

## Instructions

### Step 1: Import Modules

**Context**: Begin by importing React and the vulnerable wrapper to enable component usage.

**Command** ([[commands/import-react-and-autolinkerwrapper]]):
```javascript
import React from 'react';
import AutolinkerWrapper from 'react-autolinker-wrapper';
```

> This imports the core React library and the wrapper, allowing the component to be used in the app. Expected output: No errors on import in a Node.js or browser environment.

### Step 2: Define Base Component

**Context**: Create the App class component as the entry point for the vulnerable setup.

**Command** ([[commands/define-react-app-component]]):
```javascript
class App extends React.Component {
  // Placeholder for constructor, methods, and render
}

export default App;
```

> Defines the component skeleton. Expected output: Component exports successfully for use in index.js or similar entry file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/import-react-and-autolinkerwrapper]]
- [[commands/define-react-app-component]]

## Tools Used

- [[tools/React]]
- [[tools/react-autolinker-wrapper]]

## Tags

- xss
- react
- setup
