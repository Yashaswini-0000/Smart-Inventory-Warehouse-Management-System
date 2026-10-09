# Smart Inventory & Warehouse Management System

Complete FastAPI + MySQL backend implementing the supplied project specification, including the bonus features.

## Included
- JWT authentication with Admin, Inventory Manager, Warehouse Staff
- Categories, products, warehouses, suppliers
- Inventory and immutable stock movement ledger
- Purchase orders with partial receiving
- Customers and sales orders
- Stock reservation, pick, pack, dispatch, delivery
- Returns/refunds and inspection
- Background SMTP notifications
- Audit logs
- Dashboard and operational reports
- Stock transfers and adjustments
- Batch/expiry tracking with FEFO dispatch
- Automatic draft purchase orders for low stock
- Weighted average cost
- Excel report export
- Alembic migrations only; no `create_all`
- Pytest test suite

## Windows setup
```powershell
py -3.11 -m venv venv
.env\Scriptsctivate
pip install -r requirements.txt
copy .env.example .env
```

Create a MySQL database:
```sql
CREATE DATABASE smart_inventory CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Edit `.env` with your MySQL URL and JWT secret.

Run migrations:
```powershell
python -m alembic upgrade head
```

Start:
```powershell
uvicorn app.main:app --reload
```

Swagger:
http://127.0.0.1:8000/docs

Health:
http://127.0.0.1:8000/health

## First admin
For a simple local demo, register the first user by temporarily using the seed script:
```powershell
python seed_admin.py
```
Then login at `POST /auth/login`.

The normal `POST /auth/register` endpoint is intentionally Admin-only after the first account exists.

## Notes
- `quantity_available` is always calculated as `quantity_on_hand - quantity_reserved`.
- Stock is changed only through receipt, dispatch, return, transfer, or approved adjustment workflows.
- Inventory writes use row locks where supported by the database.
- SMTP failures are logged and do not fail the main business transaction.
