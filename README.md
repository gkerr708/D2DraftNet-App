# **D2DraftNet-App**

D2DraftNet is a deep-learning-based Dota 2 draft prediction tool. It analyzes hero selections and predicts the win probability for each team based on historical match data. 

## **🚀 Features**
- **Hero Draft Selection**: Interactive UI for selecting Radiant and Dire drafts.
- **Win Probability Prediction**: Uses a trained deep learning model to predict the outcome.
- **User-Friendly Web Interface**: Built with Flask for easy accessibility.

---

## **📦 Dependencies**
D2DraftNet requires the following dependencies, which are managed using [Poetry](https://python-poetry.org/):

- **Python** `>=3.10`
- **Flask** `>=3.1.0`
- **Torch** `>=2.6.0`
- **Pandas** `>=2.2.3`
- **Requests** `>=2.32.3`
- **BeautifulSoup4** `>=4.13.3`

Install all dependencies using:
```sh
poetry install
```

---

## **💻 How to Use**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/gkerr708/D2DraftNet-App.git
cd D2DraftNet-App
```

### **2️⃣ Set Up Poetry Environment**
Make sure you have **Poetry installed**:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```
Then install dependencies:
```sh
poetry install
```

### **3️⃣ Run the Web App**
```sh
poetry run python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

---

## **🤝 Contributing**
Pull requests are welcome! Please make sure your contributions follow best practices and are properly tested.