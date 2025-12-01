import re
import json

# -------------------------------
# SQL to NoSQL
# Convert SQL INSERT statements to NoSQL JSON format
# Supports multiple tables and multiple INSERT statements
# -------------------------------
def sql_to_nosql(sql_text):
    
    # create a pattern that describe the INSERT command syntax
    pattern = r"insert\s+into\s+(\w+)\s*\((.*?)\)\s*values\s*\((.*?)\);"
    # find all matches in sql_text of INSERT command
    matches = re.findall(pattern, sql_text, flags=re.IGNORECASE | re.DOTALL)

    # dictionary that will store all the converted data, organized by table
    nosql_data = {}

    # Loop through all INSERT statements
    for table, cols, vals in matches:
        # create a list of table columns
        columns = [c.strip() for c in cols.split(",")]
        # create a list of initial values
        initial_values = [v.strip() for v in split_values(vals)]
        # convert the initial values in a new list
        parsed_values = [convert_value(v) for v in initial_values]
        # create one row dictionary from the pairs (columns, parsed_values)
        row_dict = dict(zip(columns, parsed_values))

        # add row to the corresponding table 
        # or create a new table structure if not already exists
        if table not in nosql_data:
            nosql_data[table] = []
        nosql_data[table].append(row_dict)

    # return the data as json format
    return json.dumps(nosql_data, indent=4)

# -------------------------------
# Helper function 
# Split values correctly even when strings contain commas
# -------------------------------
def split_values(values_string):
    # prepare a list of splited values
    values = []
    current = ""
    inside_quotes = False

    # Loop through the initial values string, char by char
    for char in values_string:
        # set a flag to indicate we are inside quotes
        if char == "'" and not inside_quotes:
            inside_quotes = True
        # set the flag to false to indicate we are outside quotes
        elif char == "'" and inside_quotes:
            inside_quotes = False
        # split if "," and outside quotes
        if char == "," and not inside_quotes:
            values.append(current.strip())
            current = ""
        # else continue to concatinate the characters
        else:
            current += char

    # add the value to the list
    values.append(current.strip())
    return values

# -------------------------------
# Helper function 
# Convert SQL value to Python type
# -------------------------------
def convert_value(v):
    # if quoted string then remove quotes
    if v.startswith("'") and v.endswith("'"):
        return v[1:-1]
    # if null then return None
    if v.lower() == "null":
        return None
    # if contains "." then return as float
    try:
        if "." in v:
            return float(v)
    except:
        pass
    # otherwise try to return as integer
    try:
        return int(v)
    except:
        pass
    return v


# -------------------------------
# NoSQL to SQL
# Convert NoSQL JSON text to SQL INSERT statements 
# -------------------------------
def nosql_to_sql(json_text):
    # Create a Python dictionary from the JSON string
    data = json.loads(json_text)
    # Prepare a list to store all SQL INSERT statements as strings
    sql_output = []

    # iterate over each table in the dictionary
    for table, rows in data.items():
        # iterate over each row in the table
        for row in rows:
            # extract the column names from the dictionary
            columns = ", ".join(row.keys())
            # extracts the values from the dictionary and 
            # use format_sql_value(v) for each value to convert to correct SQL value 
            values = ", ".join(format_sql_value(v) for v in row.values())
            # create and append the INSERT statement
            sql_output.append(
                f"INSERT INTO {table} ({columns}) VALUES ({values});"
            )

    # Joins all SQL statements in the list into a single string, 
    # separated by newline characters
    return "\n".join(sql_output)

# -------------------------------
# Helper function 
# Convert Python type to SQL value  
# -------------------------------
def format_sql_value(v):
    if v is None:
        return "NULL"
    # if the variable v is a string in Python the add quotes
    if isinstance(v, str):
        return f"'{v}'"
    return str(v)
