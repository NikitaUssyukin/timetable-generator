# 📅 Timetable Generator

This Python script generates an exam timetable by assigning students to available rooms based on predefined capacities. The script reads student data from CSV files, determines the exam schedule, and saves the final timetable.

---

## 🚀 Features
- Reads student data from CSV files.
- Assigns students to available rooms based on seat capacity.
- Automatically adjusts exam times if rooms are full.
- Saves the final schedule as a CSV file.

---

## 🛠️ Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/timetable-generator.git
   cd timetable-generator
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies** (if any required in `requirements.txt`):
    - script only relies on built-in modules (`os`, `csv`, `datetime`), there are no external dependencies

---

## 📂 File Structure

```
timetable-generator/
│── students/                 # Folder containing student CSV files
│   ├── TE.csv
│   ├── ZZ.csv
│   ├── AA.csv
│   └── ...  
│── room_capacities.py         # Defines available rooms and seating capacities
│── timetable_generator.py     # Main script to generate the timetable
│── final_data.csv             # Output timetable (auto-generated)
│── .gitignore                 # Excludes unnecessary files from Git
│── README.md                  # Project documentation
```

---

## 📌 Usage

1. **Prepare Student Data:**
   - Place student lists inside the `students/` folder.
   - Each file should be named as `<LECTOR_CODE>.csv` (e.g., `TE.csv`).
   - Format each CSV file using **tab-separated values (`\t`)**:
     ```
     student_id<TAB>student_name
     12345<TAB>John Doe
     67890<TAB>Jane Smith
     ```

2. **Run the script:**
   ```sh
   python generate_timetable.py
   ```

3. **View the generated timetable:**
   - The output will be saved as `final_data.csv`.

---

## ⚙️ Configuration

- Modify room capacities in `room_capacities.py` to adjust the available rooms and their seating capacities.

---