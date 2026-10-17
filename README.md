# Greenhill Food Co-op Ordering System

A runnable **local coordinator demo** using Flask and a persistent SQLite database.
Based on the team repository at `9ee3267`; see `Project_Charter.md` for the intended project scope.

## Windows: start the application

1. Install Python 3.10 or newer (tested here with Python 3.12).
2. Download/extract the complete project into a new folder.
3. Double-click `start.bat`. The first run downloads dependencies, so internet access is needed.
4. Keep the terminal open and visit **http://127.0.0.1:5000**.
5. Press Ctrl+C in the terminal to stop. Run `start.bat` again to resume with saved data.

If double-click does not work, open PowerShell in the project folder:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m flask --app app run --host 127.0.0.1
```

No PowerShell activation script is necessary. If `py` is unavailable, use your installed
`python` command for the first line. If port 5000 is occupied, add `--port 5001` and
open http://127.0.0.1:5001 instead.

## macOS / Linux

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m flask --app app run --host 127.0.0.1
```

## Demonstration workflow

Use fictional data:

1. Add a member (e.g. M01 / Demo Member).
2. Add Oats at 3.40 per kg and Jars at 5.00 per unit.
3. Open a round and create an order for the member; record the coordinator name in
   “Entered by (proxy)”. Add 0.333 kg of oats and 2 jars. The exact total is 11.13220.
4. Edit quantities or remove lines while the round is open. Cancelled orders remain
   visible in history but are excluded from packing totals.
5. Changing a product price does not change prices already stored on order lines.
6. Close ordering. Orders can no longer be added/edited/cancelled in that round.
7. Open each order, record actual packed quantities (zero is permitted for a shortage)
   and any substitution note. Complete packing only after all active lines have actual quantities.
8. Open “Totals & printable packing sheet” and select Print / Save as PDF. The resulting
   paper/PDF can be used offline. The application itself requires the local server to run.

An empty order is a draft: add items before closing ordering. Round transitions are
one-way: open → closed → packed. Create a new round for subsequent ordering.

## Data, configuration and backup

The database is created automatically at `instance/greenhill.sqlite`. It persists
across restarts. SQLite is included with Python; no PostgreSQL account is needed.
`DATABASE_URL` is not used by this local version. PostgreSQL deployment remains future work.

To back up: stop the server and copy `instance/greenhill.sqlite` to a safe location.
To restore: stop the server, preserve the current file, and replace it with the backup.
Restart and verify the member/order records. Do not commit the database or real member data.

The default session key is generated at startup; this invalidates old forms on restart.
Refresh the browser after restarting. Optionally copy `.env.example` to `.env` and set
`SECRET_KEY` to a random value for stable local sessions; never publish `.env`.

## Verification

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

On Linux use `.venv/bin/python -m pytest -q`.
Tests cover the original model/pricing examples plus web requests, CSRF, rejected
quantities, historical prices, round locks, cancellation, packing and database persistence
when the app is recreated. See `docs/VERIFICATION.md` for the actual recorded results.

## Implementation and limits

- `app/__init__.py`: Flask factory, SQLite initialization, CSRF checks.
- `app/web.py`: persistent coordinator workflows, server-side validation and Decimal calculations.
- `app/templates/`: browser forms and printable packing sheets.
- `app/models/` and `app/services/pricing.py`: original teammate domain examples, retained
  for compatibility. Their legacy rounded calculations are not used by the new web workflow.
- `start.bat`: Windows setup/start helper. `deploy.sh`: local Unix validation/start helper.

This is **not a public production deployment**. It has no login, role-based authorization
or member self-service accounts; anyone with access to the running interface can perform
coordinator actions. Keep it bound to 127.0.0.1 and use fictional data. Production use
requires authentication, permissions, a production server and a reviewed deployment plan.

Packing substitutions are recorded as notes; they do not create replacement products or
change the stored price. Packed values use actual quantity × historical unit price.
There are no payments, banking/accounting integrations, notifications, delivery management,
full inventory controls, schema migrations or immutable audit logs.

## Team and attribution

Yuhang Zheng, Xuan Xie, Bowen Zhou. Original teammate files and project documents are retained.
The runnable local extension and its tests were prepared with AI assistance and require
team review. Repository authorship and assessment declarations should reflect actual work.

## License

MIT (see LICENSE).
