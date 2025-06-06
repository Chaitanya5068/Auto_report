import os
import sys
import tempfile
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

def load_file(file_path):
    """Load data from CSV or Excel file."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File does not exist.")
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        df = pd.read_csv(file_path)
    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
    return df

def save_plot_image(df, col):
    """Generate and save pie chart or histogram depending on data type with larger size."""
    plt.figure(figsize=(6, 5))  # Larger figure size for A4
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col].dropna().hist(bins=15, color='skyblue', edgecolor='black')
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
    else:
        counts = df[col].value_counts(dropna=True)
        top_counts = counts.head(6)
        others = counts.iloc[6:].sum()
        if others > 0:
            top_counts['Others'] = others
        top_counts.plot.pie(autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.ylabel('')
        plt.title(f'Value Distribution of {col}')
    plt.tight_layout()

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(tmp_file.name)
    plt.close()
    return tmp_file.name

def generate_column_summary(pdf, df):
    total_rows = len(df)

    for col in df.columns:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"Column: {col}", ln=True)
        
        col_data = df[col]
        non_null_count = col_data.count()
        missing_count = total_rows - non_null_count
        missing_pct = (missing_count / total_rows) * 100
        unique_count = col_data.nunique(dropna=True)
        dtype = col_data.dtype
        
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 7, f"Data type: {dtype}", ln=True)
        pdf.cell(0, 7, f"Non-null count: {non_null_count} ({100 * non_null_count / total_rows:.1f}%)", ln=True)
        pdf.cell(0, 7, f"Missing values: {missing_count} ({missing_pct:.1f}%)", ln=True)
        pdf.cell(0, 7, f"Unique values: {unique_count}", ln=True)
        
        if pd.api.types.is_numeric_dtype(col_data):
            pdf.cell(0, 7, f"Min: {col_data.min()}", ln=True)
            pdf.cell(0, 7, f"Max: {col_data.max()}", ln=True)
            pdf.cell(0, 7, f"Mean: {col_data.mean():.2f}", ln=True)
            pdf.cell(0, 7, f"Median: {col_data.median()}", ln=True)
            pdf.cell(0, 7, f"Std Dev: {col_data.std():.2f}", ln=True)

        if unique_count > 0:
            mode_series = col_data.mode(dropna=True)
            if not mode_series.empty:
                mode_val = mode_series[0]
                mode_count = col_data[col_data == mode_val].count()
                pdf.cell(0, 7, f"Most frequent value: {mode_val} (Count: {mode_count})", ln=True)

        pdf.ln(3)

        try:
            img_path = save_plot_image(df, col)
            pdf.image(img_path, w=pdf.w * 0.75)  # Increase image width to 75% of page width
            pdf.ln(15)
            os.remove(img_path)
        except Exception as e:
            pdf.cell(0, 7, f"[Could not generate chart: {e}]", ln=True)
            pdf.ln(5)

def create_pdf_report(df, output_path, input_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title from input file name (without extension)
    title = os.path.splitext(os.path.basename(input_file))[0]
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Data Summary Report - {title}", ln=True, align='C')
    pdf.ln(5)

    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 8,
        "This report presents a detailed summary of each column's data in the input file, "
        "including counts, unique values, descriptive statistics, and visualizations."
    )
    pdf.ln(10)

    generate_column_summary(pdf, df)

    pdf.output(output_path)

def main():
    print("\n📁 Your reports will be saved to:", os.path.join(os.path.expanduser("~"), "Downloads"))
    input_path = input("📂 Enter full path of CSV or Excel file: ").strip('"').strip()
    
    try:
        df = load_file(input_path)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    
    print("📂 File selected:", input_path)
    print("✅ File loaded successfully!")
    print("📊 Columns detected:", list(df.columns))
    
    output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_file = f"{base_name}_Data_Summary_Report.pdf"
    output_path = os.path.join(output_dir, output_file)
    
    try:
        create_pdf_report(df, output_path, input_path)
        print(f"✅ PDF report generated successfully at:\n{output_path}")
    except Exception as e:
        print(f"❌ Error generating PDF report: {e}")

if __name__ == "__main__":
    main()
