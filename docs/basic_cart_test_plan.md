# Test Plan for Basic Cart App

## Overview
The Basic Cart app allows browsing products, adding to cart, viewing cart, managing items, and checking out. It includes pagination for products.

## Test Cases

### 1. Load Products Page
- **Steps**:
  1. Navigate to https://testpages.eviltester.com/apps/basiccart/?page=1&limit=10
- **Expected Result**: Page loads with product list and cart count 0
- **Type**: Positive

### 2. Add Item to Cart
- **Steps**:
  1. Load products page
  2. Click "Add to Cart" for first product
- **Expected Result**: Cart count increases to 1
- **Type**: Positive

### 3. View Cart with Item
- **Steps**:
  1. Add item to cart
  2. Click cart icon
- **Expected Result**: Cart page shows the added item with quantity 1 and price
- **Type**: Positive

### 4. Increase Quantity in Cart
- **Steps**:
  1. In cart, change quantity of item to 2
- **Expected Result**: Quantity shows 2, total price updated correctly
- **Type**: Positive

### 5. Decrease Quantity in Cart
- **Steps**:
  1. In cart with quantity 2, change to 1
- **Expected Result**: Quantity shows 1, total updated
- **Type**: Positive

### 6. Remove Item from Cart
- **Steps**:
  1. In cart, click remove for the item
- **Expected Result**: Item removed, cart empty
- **Type**: Positive

### 7. Add Multiple Items
- **Steps**:
  1. Add 2 different items to cart
- **Expected Result**: Cart shows both items, total correct
- **Type**: Positive

### 8. Checkout
- **Steps**:
  1. Add item to cart
  2. Go to cart
  3. Click "Checkout"
- **Expected Result**: Checkout page or success message
- **Type**: Positive

### 9. Empty Cart Checkout
- **Steps**:
  1. Go to cart when empty
  2. Click "Checkout"
- **Expected Result**: Error or no action
- **Type**: Negative

### 10. Pagination
- **Steps**:
  1. Load page 1
  2. Click next page
- **Expected Result**: Page 2 loads with different products
- **Type**: Positive

### 11. Full Buying Flow
- **Steps**:
  1. Navigate to products page
  2. Add an item to the cart
  3. View the cart
  4. Click "Checkout"
  5. On login page, enter valid customer ID and password
  6. Submit login
- **Expected Result**: Navigate away from login page (successful login attempt)
- **Type**: Positive

## Test Environment
- Browser: Chromium (headed)
- Framework: Playwright Python
- Assertions: Check cart count, item presence, prices, totals

## Notes
- Cart state is session-based.
- Assume cart page at /apps/basiccart/cart.html
- Add CartPage class for cart-specific actions.