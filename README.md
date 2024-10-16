
# AI-Driven Log File Analyzer for Intrusion Detection

This tool analyzes log files to detect potential intrusions using machine learning. It employs the Isolation Forest algorithm to identify anomalies in log data, helping security analysts to spot suspicious activities.

## Features
- Loads log files in CSV format.
- Preprocesses log data for analysis.
- Detects anomalies indicating possible intrusions.

## Requirements
- pandas
- numpy
- scikit-learn

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai_driven_log_file_analyzer.git
   cd ai_driven_log_file_analyzer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare your log file in CSV format with the following columns:
   - `timestamp`: The time of the log entry.
   - `ip_address`: The IP address associated with the log entry.
   - `event_type`: The type of event logged.

4. Update the `log_file_path` in `log_file_analyzer.py` to the path of your log file.

5. Run the analyzer:
   ```bash
   python log_file_analyzer.py
   ```

## Usage Example
- Prepare a log file `log_file.csv` with the necessary columns and format.
- Update the path in the script and run it to detect intrusions.

## License
This project is licensed under the MIT License.
