# Energy Performance Diagnosis Estimation Tool

## Project Description
This GitHub repository pertains to a digital product designed to estimate the Energy Performance Diagnosis (DPE) of an apartment. The product revolves around an Excel file provided to the user, allowing them to input information about their residence through a form. Upon validation of the Excel form, it triggers the execution of a Python script (without user action) that calculates the DPE of the property using predictive models and generates graphs as results. These results are then transmitted to the Excel workbook and immediately displayed to the user.

## Repository File Organization
This repository consists of the following three folders:
- `docs`
- `src`
- `test`

Additionally, there is the `README` file explaining the repository's structure and a `requirements.txt` file indicating the different libraries necessary for this project along with their versions.

The `docs` folder contains various progress reports made during the project.

The `src` folder, at its root, contains the `formulaire.xlsm` file, which is the Excel file of the project intended for the user. This file initiates the form and executes the Python script. The `src` folder also includes the following subfolders:
- `data`: This folder contains all Python scripts for cleaning the database, including the binary transformation script. A subfolder named `database` is also present, containing the cleaned database in both CSV and pickle formats.
- `features`
- `models`: This folder contains Python scripts for data analysis and prediction models.
- `notebook`: This folder contains note-taking files regarding the project.
- `visualization`: This folder includes Python scripts for creating graphs needed for DPE results and preliminary data visualization.

Finally, the `test` folder consists of the following four subfolders:
- `data`: This folder contains tests for the database cleaning programs.
- `features`
- `models`: This folder contains tests for prediction model scripts.
- `visualization`: This folder contains tests for graph creation scripts.

Documentation on the database, DPE, and GDPR compliance regarding our data is available in the repository's Wiki.

## How to Use the Project

### Installation

Clone the GitHub repository and install the necessary dependencies:

```bash
git clone https://github.com/gbar-dev/stock_prediction_by_asset.git
cd stock_prediction_by_asset
pip install -r requirements.txt
```

### Model Training

Train the model using the dedicated script:

```bash
python src/main.py
```

## Contribute

If you wish to contribute to improving the model or adding new features, follow the contribution steps in the [Contribute](#contribute) section of the README file.

## License

This project is distributed under the [MIT License](link_to_license), allowing free use and distribution.

---
Remember to adjust the sections based on the specifics of your project, the data used, and any other relevant information.