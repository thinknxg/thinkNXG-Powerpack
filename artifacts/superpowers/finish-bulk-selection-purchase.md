# Finish: bulk selection - Purchase Order buying prices

## Summary of changes
- `thinknxg_powerpack/api.py`: `get_bulk_item_details` branches on `doctype == 'Purchase Order'`:
  Item Price `buying: 1` (was always `selling: 1`), Item `is_purchase_item` (was
  `is_sales_item`), tax template read as Purchase Taxes and Charges Template. Both the
  optimized and the standard path. Sales doctypes unchanged.
- `thinknxg_powerpack/tests/test_bulk_selection_purchase.py`: PO buying price (both paths),
  Sales Order still skips purchase-only items, PO reads the purchase tax template.
- The client already passed the PO's `buying_price_list` (filled from the supplier's
  default); no JS change.

## Review (Blocker/Major/Minor/Nit)
- No Blocker / Major.
- Minor (pre-existing, accepted): the dialog price is a per-price-list lookup; it ignores
  supplier/customer-specific Item Prices, UOM and validity dates. Rows still get
  thinkNXG ERP's exact rate from the item_code trigger on insert.

## Verification
- `bench --site dev.localhost run-tests --module thinknxg_powerpack.tests.test_bulk_selection_purchase` -> red before fix, 3 OK after.
- `bench --site dev.localhost run-tests --app thinknxg_powerpack` -> 63 + 10 + 233 + 83 = 389 OK (skipped=1).
- Browser e2e (dev.localhost): new PO, Supplier A -> dialog shows F049 Buy Price KES 400.00.

## Deploy
Python only: no build, no migrate.
