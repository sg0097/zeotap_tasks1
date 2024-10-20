import sqlite3

# Initialize SQLite database and create table
def initialize_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('rule_engine.db')  # This creates a file 'rule_engine.db'
    c = conn.cursor()

    # Create the 'rules' table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT,
            ast BLOB
        )
    ''')

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
    print("Database initialized and 'rules' table created.")

# Save a rule with its abstract syntax tree (AST)
def save_rule(rule_string, ast):
    conn = sqlite3.connect('rule_engine.db')
    c = conn.cursor()

    # Insert rule into 'rules' table
    c.execute("INSERT INTO rules (rule_string, ast) VALUES (?, ?)", (rule_string, repr(ast)))

    # Commit and close
    conn.commit()
    conn.close()
    print("Rule saved successfully!")

# Load all rules from the SQLite database
def load_rules():
    conn = sqlite3.connect('rule_engine.db')
    c = conn.cursor()

    # Query all rules from the 'rules' table
    c.execute("SELECT rule_string, ast FROM rules")
    rules = c.fetchall()

    # Close the connection
    conn.close()
    return rules
