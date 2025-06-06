# 🧾 Python_Report_Generator

A smart, terminal-based automated report generator built with Python — transforms CSV, Excel, PDF, and DOCX files into clean, insightful PDF reports with charts and data summaries.

---

## 🎯 Purpose

To automatically analyze a user-provided data file and generate a neat, readable PDF report containing summaries, charts, and visualizations — no manual work required.

---

## 🧠 Core Features

✅ Supports multiple file formats: `.csv`, `.xlsx`, `.xls`, `.pdf`, `.docx`  
✅ Automatically extracts and summarizes data  
✅ Generates well-formatted PDF reports with:  
- 📊 Pie charts  
- 📈 Bar and line graphs  
- 📝 Data column summaries  

✅ Detects data types and handles Unicode safely  
✅ Saves output to the user's `Downloads` folder with smart naming  
✅ Automatically uses input filename as the report title

---

## ⚙️ Technologies Used

- `Python 3.11+`  
- `pandas` — for data handling  
- `matplotlib` — for chart generation  
- `fpdf2` — for generating PDFs  
- `openpyxl` — to read Excel files  
- `PyPDF2` — to read PDFs  
- `python-docx` — to read Word files  

---

## 💡 Sample Use Cases

- Sales or marketing data analysis  
- Academic performance reports  
- Employee or HR summaries  
- Market research visualizations  
- Quick reporting for any structured dataset

---
## ▶️ Run the Project

bash
Copy
Edit
python report_generator.py

🔸 When prompted, paste the full path to your input file

🔸 The report will be saved in your Downloads folder automatically

---
## 📦 Dependencies
Make sure you install these with pip:

pandas

matplotlib

fpdf2

openpyxl

PyPDF2

python-docx

---
## 💬 Sample Terminal Output
plaintext
Copy
Edit
📁 Your reports will be saved to: C:\Users\YourName\Downloads

📂 Enter full path of CSV, Excel, PDF or DOCX file: D:\data\sales.xlsx

✅ File loaded successfully!

📊 Data summarized and visualized!

📄 Report saved: C:\Users\YourName\Downloads\sales_summary_report.pdf

---
## 📜 License
This project is licensed under the MIT License — free to use, modify, and distribute with credit.

---
## 👨‍💻 Developed By
Chaitanya Bhosale

🔗 GitHub Profile: https://github.com/Chaitanya5068
