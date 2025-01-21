

# NOAALOGVISUALIZATION

## Overview
NOAALOGVISUALIZATION is a Streamlit-based web application that fetches and visualizes NOAA shipstat data. The application downloads the latest ship log data from the NOAA website, processes it, and displays the data on an interactive map using Folium. Users can explore the latitude and longitude of ships along with additional details like ocean and quadrant.

---

## Features
- **Automatic Data Fetching**: Fetches the latest ship log data from the NOAA website.
- **Interactive Map**: Visualizes ship locations on an interactive map using Folium.
- **Streamlit Frontend**: Provides a user-friendly interface for exploring the data.

---

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8 or higher
- `pip` (Python package manager)

---

## Installation and Setup

### Step 1: Clone the Repository
Clone the project repository to your local machine using the following command:
```bash
git clone https://github.com/Tw0side/NOAALOGVISUALIZATION.git
```

### Step 2: Navigate to the Project Directory
Change to the project directory:
```bash
cd NOAALOGVISUALIZATION
```

### Step 3: Create a Virtual Environment (Optional but Recommended)
Create a virtual environment to isolate the project dependencies:
```bash
python3 -m venv venv
```

Activate the virtual environment:
- On Linux/Mac:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

### Step 4: Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

---

## Running the Application

### Step 1: Start the Streamlit App
Run the Streamlit application using the following command:
```bash
streamlit run fetch.py
```

### Step 2: Access the Application
Once the app is running, Streamlit will provide a local URL (usually `http://localhost:8501`). Open this URL in your web browser to access the application.

---

## Project Structure
```
NOAALOGVISUALIZATION/
├── fetch.py                # Main script to fetch and visualize data
├── requirements.txt        # List of Python dependencies
├── README.md               # Project documentation
└── venv/                   # Virtual environment (created during setup)
```

---

## Dependencies
The project relies on the following Python packages:
- `streamlit`: For the web application frontend.
- `folium`: For creating interactive maps.
- `pandas`: For data processing.
- `requests`: For fetching data from the NOAA server.
- `beautifulsoup4`: For parsing HTML content.
- `chardet`: For detecting file encoding.

All dependencies are listed in `requirements.txt`.

---

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- NOAA for providing the ship log data.
- Streamlit and Folium for enabling interactive data visualization.

---

## Contact
For questions or feedback, please contact:
- **Your Name**: [Your Email Address]
- **GitHub**: [https://github.com/Tw0side](https://github.com/Tw0side)

---

Enjoy exploring NOAA ship log data with NOAALOGVISUALIZATION! 🚢🌍

---

