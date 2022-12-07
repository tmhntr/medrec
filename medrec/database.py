import random
import sqlite3
import os

from medrec.entry import DoctorVisitEntry, Entry, EntryType, HealthDataEntry, MedicationEntry
# Establish a connection to the Database and create
# a connection object

if os.environ.get('RESOURCEPATH'):
    db_path = os.path.join(os.environ['RESOURCEPATH'], "medrec.db")
else:
    db_path = os.path.join("data/medrec.db")


def adapt_entrydata(entry: Entry):
    return entry.adapt().encode('ascii')


def convert_entrydata(s: bytes):
    data = list(map(str.strip, s.decode('ascii').strip("()").split(';')))
    entry_type = EntryType[data[2]]
    if entry_type == EntryType.MEDICATION:
        return MedicationEntry(*data)
    elif entry_type == EntryType.HEALTH_DATA:
        return HealthDataEntry(*data)
    elif entry_type == EntryType.DOCTOR_VISIT:
        return DoctorVisitEntry(*data)
    else:
        raise ValueError("Invalid entry type")


# Register the adapter
sqlite3.register_adapter(Entry, adapt_entrydata)
sqlite3.register_adapter(MedicationEntry, adapt_entrydata)
sqlite3.register_adapter(DoctorVisitEntry, adapt_entrydata)
sqlite3.register_adapter(HealthDataEntry, adapt_entrydata)

# Register the converter
sqlite3.register_converter("entrydata", convert_entrydata)


def create_entry_table(cursor: sqlite3.Cursor) -> None:
    """Create the entries table"""
    query = '''CREATE TABLE IF NOT EXISTS entries
                (id text primary key, date text, entry_type text, entrydata entrydata)'''
    cursor.execute(query)


def create_db() -> None:
    """Create the database and tables"""
    # create a connection to the database
    conn = sqlite3.connect(db_path)
    # create a cursor object
    cursor = conn.cursor()
    # create the tables
    create_entry_table(cursor)
    # commit the changes
    conn.commit()
    # close the connection
    conn.close()


def add_entry(entry: Entry) -> None:
    """Add an entry to the database"""

    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    query = '''INSERT INTO entries VALUES (?, ?, ?, ?)'''
    cursor.execute(query, (entry.id, entry.date, entry.entry_type.name, entry))
    conn.commit()
    conn.close()


def get_entries(start_date: str = None, end_date: str = None, entry_type: EntryType = None, limit: int = None, offset: int = None, order_by: str = None) -> list[Entry]:
    """Get entries from the database

    Args: start_date (str): The start date of the entries to get
          end_date (str): The end date of the entries to get
          entry_type (EntryType): The type of entries to get
          limit (int): The maximum number of entries to get
          offset (int): The number of entries to skip
          order_by (str): The column to order the entries by"""

    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    query = '''SELECT entrydata FROM entries'''
    if start_date or end_date or entry_type:
        query += ' WHERE '
        if start_date:
            query += f'date >= "{start_date}"'
        if end_date:
            if start_date:
                query += ' AND '
            query += f'date <= "{end_date}"'
        if entry_type:
            if start_date or end_date:
                query += ' AND '
            query += f'entry_type = "{entry_type.name}"'
    if order_by:
        query += f' ORDER BY {order_by}'
    if limit:
        query += f' LIMIT {limit}'
    if offset:
        query += f' OFFSET {offset}'

    cursor.execute(query)
    entries = cursor.fetchall()
    conn.close()
    return entries


def get_entry(id) -> Entry:
    """Get an entry from the database
    and return it as an Entry object

    Args: id (str): The id of the entry to get"""
    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    query = '''SELECT entrydata FROM entries WHERE id = ?'''
    cursor.execute(query, (id,))
    entry = cursor.fetchone()
    conn.close()
    return entry


def update_entry(entry: Entry) -> None:
    """Update an entry in the database"""

    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    query = '''UPDATE entries SET entrydata = ? WHERE id = ?'''
    cursor.execute(query, (entry, entry.id))
    conn.commit()
    conn.close()


def delete_entry(id) -> None:
    """Delete an entry from the database"""

    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    query = '''DELETE FROM entries WHERE id = ?'''
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()


def get_medication_entries() -> list[MedicationEntry]:
    """Get medication entries from the database"""

    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    query = '''SELECT entrydata FROM entries WHERE entry_type = ?'''
    cursor.execute(query, (EntryType.MEDICATION.name,))
    entries = cursor.fetchall()
    conn.close()
    return entries


def get_health_data_entries() -> list[HealthDataEntry]:
    """Get health data entries from the database"""

    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    query = '''SELECT entrydata FROM entries WHERE entry_type = ?'''
    cursor.execute(query, (EntryType.HEALTH_DATA.name,))
    entries = cursor.fetchall()
    conn.close()
    return entries


def get_doctor_visit_entries() -> list[DoctorVisitEntry]:
    """Get doctor visit entries from the database"""

    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    query = '''SELECT entrydata FROM entries WHERE entry_type = ?'''
    cursor.execute(query, (EntryType.DOCTOR_VISIT.name,))
    entries = cursor.fetchall()
    conn.close()
    return entries


def get_entry_count() -> int:
    """Get the number of entries in the database"""

    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    query = '''SELECT COUNT(*) FROM entries'''
    cursor.execute(query)
    count = cursor.fetchone()
    conn.close()
    return count


if __name__ == '__main__':
    create_db()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    entry = MedicationEntry(
        date="2020-01-0{}".format(random.randint(1, 9)),
        medication_name="Aspirin",
        dosage="500mg",
        frequency="2x daily",
        route="Oral",
        reason="Headache"
    )

    add_entry(entry)

    entries = get_entries()
    print(entries)
