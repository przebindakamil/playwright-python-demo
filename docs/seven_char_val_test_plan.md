# Test Plan for 7 Char Val App

## Overview
The 7 Char Val app validates an input field for exactly 7 characters using only A-Z, a-z, 0-9, and *. It provides feedback on validity.

## Test Cases

### 1. Valid Input (Exactly 7 Valid Characters)
- **Steps**:
  1. Navigate to https://testpages.eviltester.com/apps/7-char-val/
  2. Enter "abc123*" in the input field
  3. Click "Check Input"
- **Expected Result**: Success message (e.g., "Valid")
- **Type**: Positive

### 2. Valid Input (All Letters)
- **Steps**:
  1. Enter "ABCDEFG" 
  2. Click "Check Input"
- **Expected Result**: Success message
- **Type**: Positive

### 3. Valid Input (All Numbers)
- **Steps**:
  1. Enter "1234567"
  2. Click "Check Input"
- **Expected Result**: Success message
- **Type**: Positive

### 4. Invalid: Too Short
- **Steps**:
  1. Enter "abc123"
  2. Click "Check Input"
- **Expected Result**: Error message (e.g., "Invalid length" or "Must be 7 characters")
- **Type**: Negative

### 5. Invalid: Too Long
- **Steps**:
  1. Enter "abc12345"
  2. Click "Check Input"
- **Expected Result**: Error message
- **Type**: Negative

### 6. Invalid: Invalid Characters
- **Steps**:
  1. Enter "abc!@#$"
  2. Click "Check Input"
- **Expected Result**: Error message (e.g., "Invalid characters")
- **Type**: Negative

### 7. Invalid: Empty Input
- **Steps**:
  1. Leave input empty
  2. Click "Check Input"
- **Expected Result**: Error message
- **Type**: Negative

### 8. Invalid: Mixed Valid/Invalid
- **Steps**:
  1. Enter "abc123!"
  2. Click "Check Input"
- **Expected Result**: Error message for invalid character
- **Type**: Negative

## Test Environment
- Browser: Chromium (headed for visibility)
- Framework: Playwright Python
- Assertions: Check for presence of success/error messages in page content

## Notes
- Assume input has id or name like "7charval" or similar.
- Button is "Check Input".
- Results may appear in a div or alert; adjust locators based on actual behavior.
- Add page object for reusability.