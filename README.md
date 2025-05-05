# 🧪 SauceDemo Automation Framework (Playwright + Behave + Python)

This project contains automated end-to-end (E2E), Functional and Error Handling tests for the [SauceDemo v1](https://www.saucedemo.com/v1/) website using:

- Python
- Playwright (synchronous mode)
- Behave (Gherkin-style BDD)
- Page Object Model (POM)
- Git + GitHub

---

## 🔧 Technologies Used

- Python 3.12.1
- Playwright 1.44+
- Behave 1.2.6
- Git (SSH)
- macOS Terminal / SourceTree (GUI)
- Pycharm IDE
---

## 📁 Project Structure
(example of folder structure)

playwright_POM_project
-behave/
├── features/
│ ├── login.feature
│ ├── steps/
│ │ └── login_steps.py
│ ├── pages/
│ │ ├── base_page.py
│ │ ├── login_page.py
│ │ ├── inventory_page.py
│ │ └── menus/
│ │ └── sort_menu.py
│ ├── utils/
│ │ ├── constants.py
│ │ └── helpers.py
├── environment.py
├── requirements.txt
├── README.md
└── .gitignore


👤 Author

Developed by robertpython39 (Robert Nicolescu)
This project serves as both a personal automation framework and a learning path for mastering Playwright and Behave.