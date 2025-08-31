# A Systematic Literature Review Scripts
While conducting a large-scale systematic literature review, I found myself navigating a massive dataset of over 180k papers (in the year of 2025). The scripts in this repository were born out of that challenge and proved to be a complete lifesaver for processing and analyzing the data.

It occurred to me that other researchers might be facing similar hurdles. I've decided to share my work publicly in the hope that these scripts can help streamline your own research efforts. If you find them useful, a shout-out or a simple thank you would be amazing! :)

This repository contains the data, scripts, and analysis for a systematic literature review (SLR) research stuff. The goal of this research is to identify key trends, and highlight potential future research directions.

## 📖 About The Project

Federated Learning is a rapidly evolving field in machine learning. This project was initiated to systematically review the vast body of literature, starting from an initial dataset of over 60,000 papers. We use data processing scripts to filter, analyze, and synthesize findings from this extensive collection.

## 🚀 Getting Started

Follow these steps to set up your local development environment and start working with the data and scripts.

### Prerequisites

Make sure you have the following software installed on your machine:

* [Python 3.8+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads/)

### Installation & Setup

1.  **Clone the repository**
    Open your terminal and clone this repository to your local machine.
    ```sh
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```

2.  **Navigate to the project directory**
    ```sh
    cd your-repo-name
    ```

3.  **Create a Python Virtual Environment**
    It is highly recommended to use a virtual environment to manage project-specific dependencies.

    * **On macOS and Linux:**
        ```sh
        python3 -m venv venv
        ```

    * **On Windows:**
        ```sh
        python -m venv venv
        ```

4.  **Activate the Virtual Environment**
    You must activate the environment every time you work on the project.

    * **On macOS and Linux:**
        ```sh
        source venv/bin/activate
        ```

    * **On Windows:**
        ```sh
        .\venv\Scripts\activate
        ```
    Your terminal prompt should now be prefixed with `(venv)`.

5.  **Install Required Packages**
    With the environment active, install all the necessary libraries using the `requirements.txt` file.
    ```sh
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file. You can do this by running `pip freeze > requirements.txt` after installing your packages.)*

## 💻 Usage

Once the setup is complete, you can begin working with the project. For example, to start data processing, you might run a script like this:
```sh
python scripts/process_data.py
```

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request


## 📄 License
Distributed under the MIT License. See LICENSE for more information.