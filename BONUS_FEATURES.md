# Bonus features implemented

## Stock transfers
- POST /transfers
- GET /transfers
- PUT /transfers/{id}/dispatch
- PUT /transfers/{id}/receive
- PUT /transfers/{id}/cancel
- Transfer Out / Transfer In stock movement entries
- Source/destination warehouse role checks
- Destination capacity check
- Shortage quantity field is recorded

## Stock adjustments
- POST /adjustments
- GET /adjustments
- PUT /adjustments/{id}/approve
- PUT /adjustments/{id}/reject
- Reasons: Damaged, Lost, Expired, Found, Count Correction
- Stock changes only after approval

## Batch / expiry / FEFO
- POST /batches
- GET /batches
- Batches are ordered by earliest expiry
- Dispatch consumes batch quantities using FEFO when batch stock is available

## Automatic draft purchase orders
- When available stock falls below reorder level after stock-changing workflows, a draft PO is automatically created for the preferred supplier if no open PO already exists.

## Weighted average cost
- Every purchase receipt recalculates product cost price using:
  `(old_qty * old_cost + received_qty * receipt_cost) / (old_qty + received_qty)`

## Excel export
- GET /reports/export returns `inventory_report.xlsx`
