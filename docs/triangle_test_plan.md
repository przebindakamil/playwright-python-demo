# Test Plan for Triangle App

## Overview
The Triangle app allows users to input three side lengths and determines if the triangle is equilateral, isosceles, or scalene. This plan covers functional testing, edge cases, and invalid inputs.

## Test Cases

### 1. Equilateral Triangle
- **Steps**:
  1. Navigate to https://testpages.eviltester.com/apps/triangle
  2. Enter side1: 5, side2: 5, side3: 5
  3. Click "Identify Triangle" button
- **Expected Result**: Output shows "Equilateral"
- **Type**: Positive

### 2. Isosceles Triangle
- **Steps**:
  1. Enter side1: 5, side2: 5, side3: 6
  2. Click "Identify Triangle"
- **Expected Result**: Output shows "Isosceles"
- **Type**: Positive

### 3. Scalene Triangle
- **Steps**:
  1. Enter side1: 3, side2: 4, side3: 5
  2. Click "Identify Triangle"
- **Expected Result**: Output shows "Scalene"
- **Type**: Positive

### 4. Invalid: Not a Triangle (Triangle Inequality)
- **Steps**:
  1. Enter side1: 1, side2: 1, side3: 10
  2. Click "Identify Triangle"
- **Expected Result**: Error message (e.g., "Not a valid triangle")
- **Type**: Negative

### 5. Invalid: Zero Length
- **Steps**:
  1. Enter side1: 0, side2: 5, side3: 5
  2. Click "Identify Triangle"
- **Expected Result**: Error message
- **Type**: Negative

### 6. Invalid: Negative Length
- **Steps**:
  1. Enter side1: -1, side2: 5, side3: 5
  2. Click "Identify Triangle"
- **Expected Result**: Error message
- **Type**: Negative

### 7. Invalid: Non-Numeric Input
- **Steps**:
  1. Enter side1: "abc", side2: 5, side3: 5
  2. Click "Identify Triangle"
- **Expected Result**: Error message or no result
- **Type**: Negative

## Test Environment
- Browser: Chromium (headed for visibility)
- Framework: Playwright Python
- Assertions: Check output text or error messages

## Notes
- Assume inputs are text fields and button is identifiable by text.
- Add page object for reusability (e.g., TrianglePage class).
- Run tests in sequence or parameterized for efficiency.