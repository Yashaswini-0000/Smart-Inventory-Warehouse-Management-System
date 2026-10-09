# Swagger testing checklist

1. `POST /auth/login`
2. Authorize with Bearer token
3. `GET /auth/me`
4. Create warehouse
5. Create category
6. Create supplier
7. Create product
8. Create customer
9. Create purchase order
10. Approve PO
11. Receive PO (stock increases + movement)
12. Inspect `/inventory`
13. Create sales order
14. Confirm (stock reserved)
15. Pick
16. Pack
17. Dispatch (stock decreases + movement)
18. Deliver
19. Create return
20. Inspect return
21. Approve return (Good items return to stock)
22. Create transfer
23. Dispatch transfer
24. Receive transfer
25. Create adjustment
26. Approve adjustment
27. View `/reports/dashboard`
28. View `/reports/low-stock`
29. Download `/reports/export`
30. View `/audit-logs`

Bonus:
- Create batches with expiry dates
- Use FEFO-ready batch ordering endpoint `/batches`
- Low stock endpoint identifies reorder quantity and supplier
- Excel inventory export
