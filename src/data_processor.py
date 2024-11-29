import pandas as pd
from datetime import datetime
import os

class DataProcessor:
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """
        Load data from CSV or Excel file
        """
        file_ext = os.path.splitext(self.data_file)[1].lower()
        try:
            if file_ext == '.csv':
                self.data = pd.read_csv(self.data_file)
            elif file_ext in ['.xlsx', '.xls']:
                self.data = pd.read_excel(self.data_file)
            else:
                raise ValueError(f"Unsupported file format: {file_ext}")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise

    def generate_report(self) -> str:
        """
        Generate HTML report from data
        """
        if self.data is None:
            return "No data available"

        # Example report generation - customize as needed
        report = f"""
        <html>
            <body>
                <h2>Daily Report - {datetime.now().strftime('%Y-%m-%d')}</h2>
                <p>Total Records: {len(self.data)}</p>
                <h3>Summary Statistics:</h3>
                {self.data.describe().to_html()}
            </body>
        </html>
        """
        return report
