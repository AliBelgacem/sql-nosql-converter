📘 SQL / NoSQL Converter (Python GUI)

A simple and efficient SQL to NoSQL and NoSQL to SQL Python-based tool converter.
This application provides a user-friendly Tkinter GUI to load SQL/JSON files, 
convert data formats, and save the results instantly.

- Ideal for students, developers, and anyone working with database transformations.
- Supports multi-table SQL inserts and nested JSON structures.


🖼️ Screenshot

	screenshots/SQL_to_NoSQL_View.png
	screenshots/NoSQL_to_SQL_View.png


🚀 Features

- Convert Between SQL & NoSQL

	SQL INSERT statements to JSON (NoSQL)

	JSON (NoSQL) to SQL INSERT statements

- Smart Parsing

	Multiple INSERT statements

	Strings with commas

	NULL values

	Auto-detection of integers & floats

	Multiple tables in the same input

- Clean GUI

	Tab-based interface (SQL to NoSQL and NoSQL to SQL)

	Load SQL/JSON from files

	Save results in .sql or .json

	Scrolling text editors for easy review


🗂️ Project Structure

sql-nosql-converter/
|
|-- main.py         # Main launcher (Tkinter root)
|-- gui.py          # Graphical interface (tabs, widgets, loaders)
|-- converter.py    # Conversion engine (logic)
|
|-- README.md
|-- requirements.txt
└-- screenshots/


🛠️ Technologies Used

- Python 3.8.10
- Tkinter (built-in GUI library)
- JSON handling
- Regular expressions (regex)
# No external dependencies required.


📥 Installation & Usage

- Clone the repository :
	git clone https://github.com/AliBelgacem/sql-nosql-converter.git
	cd sql-nosql-converter
- Run the application
	python main.py


📌 Usage Guide

- SQL to NoSQL
	Paste SQL INSERT INTO ... statements
	Or load .sql file
	Click Convert to NoSQL
	Copy JSON output from the output text area
	Or Save JSON output to .JSON file

- NoSQL to SQL
	Paste JSON formatted tables
	Or load .json file
	Click Convert to SQL
	Copy sql output from the output text area
	Save sql output to .sql file


🧩 Example

- SQL Input

INSERT INTO insert into client (id, name, address, age) values (1, 'ali', 'saida', 42.5);
INSERT INTO client (id, name, address, age) values (2, 'moh', 'saida', 43);
INSERT INTO product (id, designation, qty) values (1, 'sugar', 30);

- JSON Output

{
    "client": [
        {
            "id": 1,
            "name": "ali",
            "address": "saida",
            "age": 42.5
        },
        {
            "id": 2,
            "name": "moh",
            "address": "saida",
            "age": 43
        }
    ],
    "product": [
        {
            "id": 1,
            "designation": "Sugar",
            "qty": 30
        }
    ]
}


🧠 How It Works

- SQL to NoSQL

	Regex detects table, columns, and values
	Values are split safely even inside quotes
	Types are converted automatically
	Data is grouped by tables

- NoSQL to SQL

	JSON parsed to Python dictionary
	Each row converted to an SQL INSERT statement
	Types are normalized for SQL


📌 Future Improvements 

- Add CSV import/export
- Add MongoDB export
- Add SQL SELECT parsing


👤 Author

Ali Belgacem
Computer Engineer • Python Developer • AI Researcher

📧 Email: alibelgacem1983@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/ali-belgacem-500106170
🐱 GitHub: https://github.com/AliBelgacem


⭐ Support the Project


If this project helped you, please consider giving it a ⭐ on GitHub — it really helps!

