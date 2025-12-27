A mini **Django-based restaurant management system** to handle dine-in tables, live orders, and billing with role-based access.  
Built as part of a **Full Stack Django Developer Take-Home Assignment**.

### 1. Table Management
- Multiple tables with seating capacity
- Table statuses:
  - Available
  - Occupied
  - Bill Requested
  - Closed
- Live table status dashboard (API)

### 2. Menu & Orders
- Menu items with:
  - Name
  - Category (Starter / Main / Drink / Dessert)
  - Price
  - Availability
- Create orders mapped to tables
- Multiple items per order with quantities
- Order status:
  - Placed
  - In Kitchen
  - Served
- Table auto-switches to **Occupied** when an order is placed

### 3. Billing
- Generate bill per table
- Shows:
  - Items & quantities
  - Total amount
  - Flat tax
- Bill status:
  - Not Generated
  - Pending Payment
  - Paid
- Once paid → table becomes **Available**

### 4. Role-Based Access (RBAC)
- **Waiter**: Create orders, update order status  
- **Cashier**: Generate bills, mark payment  
- **Manager**: Manage tables & menu, view reports 
