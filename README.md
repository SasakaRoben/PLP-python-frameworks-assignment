Here’s a polished, copyable version of your **README.md**:

```markdown
# Frameworks Assignment: CORD-19 Data Exploration

This project explores the **CORD-19 metadata dataset** (COVID-19 research papers) using **pandas**, **matplotlib**, and **seaborn**, and presents the results through a simple **Streamlit web application**.

---

## 🎯 Objectives
- Load and clean a real-world dataset  
- Perform basic data analysis  
- Create clear visualizations  
- Build an interactive web app with Streamlit  
- Present findings effectively  

---

## 📂 Project Structure
```

Frameworks\_Assignment/
│
├── data/
│   └── metadata.csv        # dataset file (or sample)
│
├── notebooks/
│   └── exploration.ipynb   # optional Jupyter notebook
│
├── app/
│   └── streamlit\_app.py    # Streamlit app
│
├── analysis.py             # main script for analysis + plots
├── requirements.txt        # dependencies
└── README.md               # project documentation

````

---

## ⚙️ Setup Instructions

**Clone this repository:**
```bash
git clone <your-repo-url>
cd Frameworks_Assignment
````

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run analysis (to generate plots):**

```bash
python analysis.py
```

**Launch the Streamlit app:**

```bash
streamlit run app/streamlit_app.py
```

---

## 📊 Data Exploration

**Dataset:** `metadata.csv` from the [CORD-19 dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

* Shape: \~ *\[rows × columns depending on sample]*
* Columns include: `title`, `abstract`, `publish_time`, `authors`, `journal`, `source_x`
* Missing values: found in `abstract`, `journal`, and `publish_time`

---

## 🧹 Data Cleaning

* Converted `publish_time` to datetime
* Extracted **year** for trend analysis
* Created `abstract_word_count` column
* Handled missing abstracts with empty strings

---

## 🔎 Analysis & Findings

* **Publications Over Time**: Spike in 2020–2021 reflecting COVID-19 research boom.
* **Top Journals**: *medRxiv* and *bioRxiv* had the highest number of papers.
* **Abstract Word Counts**: Most abstracts range between 100–300 words.
* **Scatter Trends**: No strong correlation between year and abstract length, though 2020 abstracts tended to be shorter (likely due to urgency).

---

## 📈 Visualizations

* 📊 Bar chart: Publications by year
* 📊 Bar chart: Top 10 journals
* 📊 Histogram: Abstract word count distribution
* 📊 Scatter plot: Year vs abstract word count

---

## 🌐 Streamlit App

The Streamlit app allows **interactive exploration**:

* Filter by year range
* View publications by year
* See top journals
* Preview dataset samples

**Launch app:**

```bash
streamlit run app/streamlit_app.py
```

---

## 📝 Reflection

**Challenges**

* Large dataset size → worked with a smaller sample for speed.
* Handling missing values (`publish_time`, `abstract`).
* Learning Streamlit layout & caching for performance.

**Learnings**

* Practical use of pandas for data cleaning & grouping.
* Experience with matplotlib/seaborn for professional visualizations.
* Building an interactive dashboard with Streamlit.

---

## ✅ Expected Outcomes

By completing this project, you will have:

* A cleaned and analyzed dataset
* Multiple visualizations (bar, histogram, scatter)
* An interactive Streamlit app
* Documentation of findings and reflection

