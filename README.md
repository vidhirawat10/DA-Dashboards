# Mental Health Dashboard

![Dashboard Screenshot](image_f94f46.jpg) ## 🌟 Project Overview

The **Mental Health Dashboard** is a comprehensive analytics tool designed to provide insights into mental health trends and offer a personalized stress analysis. Built with Python's Dash framework, this interactive dashboard helps users understand potential stress factors based on their lifestyle and mental health responses, while also visualizing key findings from a mental health survey.

**Key Features:**

* **Personalized Stress Analyzer:** Input your personal, lifestyle, and mental health data to receive a unique stress score, identify risk factors, and get tailored recommendations.
* **Survey Results & Trends:** Explore an interactive dashboard displaying demographic distributions, treatment-seeking behaviors, workplace support insights, and more from a real-world mental health survey.
* **Interactive Visualizations:** Leverage Plotly graphs for dynamic and insightful data representation.
* **Two-Column Layout:** A clean, intuitive layout separating input fields from results on the stress analyzer page.
* **Dark Mode Theme:** An aesthetically pleasing dark interface for comfortable viewing.

## 🚀 Demo & Screenshots

Here are some glimpses of the dashboard:

### Personalized Stress Analyzer
*Input Section*
![Stress Analyzer Input](image_f953f7.png) *Stress Analysis Results (Example)*
![Stress Analyzer Output](image_f9b89f.jpg) ### Dashboard in Dark Mode
![Dark Mode Dashboard](image_f94f46.jpg) ### Survey Results Page
*You can add a screenshot of your 'Survey Results & Trends' page here once deployed, or after running locally.*

## ⚙️ Installation

To run this dashboard locally, follow these steps:

1.  **Clone the repository:**
    First, navigate to your desired directory on your local machine. If you're cloning the entire `DA-Dashboards` repository, you would do:
    ```bash
    git clone [https://github.com/vidhirawat10/DA-Dashboards.git](https://github.com/vidhirawat10/DA-Dashboards.git)
    cd DA-Dashboards
    ```
    Then, navigate into the specific dashboard's directory:
    ```bash
    cd "Mental Health Dashboard"
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage dependencies.
    * **Windows (PowerShell):**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **macOS/Linux (Bash/Zsh):**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    With your virtual environment activated, install all required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♀️ Usage

Once all dependencies are installed, you can run the dashboard:

1.  **Ensure your virtual environment is active.**
2.  **Navigate to the `Mental Health Dashboard` directory** in your terminal.
3.  **Run the main application file:**
    ```bash
    python index.py
    ```
4.  Open your web browser and go to `http://127.0.0.1:8050/` (or the address provided in your terminal).

## 📁 Project Structure
Mental Health Dashboard/<br>
├── app.py                  # Initializes the Dash app instance and server
<br>
├── index.py                # Main entry point, handles URL routing and shared callbacks
<br>
├── Procfile                # For deployment (e.g., Heroku/Render)
<br>
├── requirements.txt        # Lists all Python dependencies
<br>
├── data/
<br>
│   └── cleaned_mental_health_survey.csv # Cleaned survey data for analysis
<br>
│   └── survey.csv                   # Raw survey data (if you keep it)
<br>
├── pages/
<br>
│   ├── init.py         # Makes 'pages' a Python package
<br>
│   ├── stress_analyzer.py  # Defines the layout for the Personalized Stress Analyzer page
<br>
│   └── survey_results.py   # Defines the layout for the Survey Results & Trends page
<br>
└── eda_and_cleaning.ipynb  # Jupyter Notebook for Exploratory Data Analysis and data cleaning
<br>

---

## 📊 Data Source

The insights and trends presented in the "Survey Results & Trends" section are derived from the **OSMI 2014 Mental Health in Tech Survey**. The raw data is processed and cleaned in the `eda_and_cleaning.ipynb` notebook.

## ✨ Future Enhancements

* Implement user authentication.
* Add more sophisticated machine learning models for stress prediction.
* Incorporate real-time data input and analysis.
* Expand recommendations based on more diverse datasets.
* Integrate with external APIs for additional health metrics.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes and commit them (`git commit -m 'Add Your Feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (if you have one).

## 📧 Contact

For any questions or feedback, please reach out to:

* **Vidhi Rawat**
* GitHub: [vidhirawat10](https://github.com/vidhirawat10)

---
