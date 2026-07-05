# Movie Recommender System

A simple content-based movie recommendation system built using **Python**, **Streamlit**, and **Pandas**.

The application recommends five movies similar to the one selected by the user and displays their posters using the TMDB API.

---

## Features

- Recommend movies based on similarity
- Clean and interactive Streamlit interface
- Displays movie posters using TMDB API
- Fast recommendations using a precomputed similarity matrix

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Pickle
- Requests
- TMDB API

---

## Project Structure

```
Movie-Recommender-System/
- app.py
- movie_dict.pkl
- similarity.pkl
- requirements.txt
- README.md
- .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Dhananjay582/Movie-Recommender-System.git
```

Move into the project folder

```bash
cd Movie-Recommender-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Screenshots

```
![Movie Recommender System](images/screenshot.png)
```

---

## Dataset

The recommendation model was built using the TMDB movie dataset.

---

