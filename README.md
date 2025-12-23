## Overview

This project demonstrates an asynchronous data pipeline for fetching, normalizing, unifying, and serializing menu combo data coming from multiple inconsistent sources.


## How to run the script
1. Requirements
Python 3.9+

2. Create and activate virtual environment
```bash
python3 -m venv .venv

source .venv/bin/activate   # macOS/Linux
.\.venv\Scripts\activate    # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Input configuration
The file `input_data.json` must contain a list of URLs to download

5. Run the script
```bash
python main.py
```
6. Optional: S3 upload
Configure AWS credentials via environment variables

---

## Why `dataclass` was chosen

Python `dataclass` was used for all domain models because it provides:

* Each entity (Menu, Combo, Subitem) is represented as a plain data container with well-defined fields.

* Automatic generation of `__init__`, `__repr__`, and equality logic keeps the code concise and readable.

* `dataclasses.asdict()` allows straightforward conversion of nested objects into JSON-compatible dictionaries.

This approach balances structure and flexibility without introducing unnecessary complexity.

---

### High-level structure

```
Menu
 └── combos: dict[combo_id, ComboVersion]

ComboVersion
 └── combo_versions: dict[source_file, Combo]

Combo
 ├── source_file: str
 ├── name: str
 └── slots: list[Subitem]

Subitem
 ├── category: str
 └── name: str
```

---

## Assumptions

* Combo uniqueness is determined by `combo_id` and `source_file`
* Subitem uniqueness is determined by `(category, name)` within a single combo
* S3 upload is optional and intended to demonstrate intent rather than production readiness
