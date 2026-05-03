# 🌍 Geospatial Query Engine - Complete Beginner's Guide

## 📚 What is This Project?

The **Geospatial Query Engine** is a smart system that understands human language to find and map places on Earth. It reads what you write, finds place names (like cities, countries, or states), handles spelling mistakes, and shows the locations on an interactive map with real-time disaster alerts.

**In simple words**: You type a question like _"Show me cities in Maharashtra"_, and the system:

1. Understands what you mean
2. Finds the place you're talking about
3. Shows it on a map
4. Tells you if there are any natural disasters happening there

---

## 🎓 What Will You Learn From This Project?

This project teaches you:

1. **Natural Language Processing (NLP)** — How computers understand human language
2. **Fuzzy Matching** — How to handle typos and spelling mistakes intelligently
3. **Web Development** — Building a web app with Flask (Python's web framework)
4. **APIs** — How to connect to external services (NASA satellite data)
5. **Geographic Data** — Working with coordinates, latitude, longitude
6. **Real-time Data** — Fetching live disaster alerts from the internet
7. **Interactive Maps** — Displaying locations on web maps
8. **Database Design** — Organizing geographic information efficiently

---

## 🤔 Why Is This Project Used?

**Real-world applications**:

- **Disaster Management**: Alert systems for earthquakes, fires, tsunamis
- **Travel Apps**: Finding cities and showing weather information
- **News Applications**: Identifying locations mentioned in news articles
- **E-commerce**: Understanding where customers are from (location extraction)
- **Smart Home Systems**: Understanding user commands with place names
- **Environmental Monitoring**: Tracking events like volcanoes and natural disasters

---

## 🔧 How Does It Work? (System Architecture)

```
User Types Text
    ↓
[Flask Web Server (app.py)]
    ↓
[NLP Processing (geoparser.py)]
    ├─ Extract place names using AI
    ├─ Fix typos using fuzzy matching
    └─ Find coordinates from database (places_db.py)
    ↓
[Get Real-time Alerts]
    ├─ NASA Satellite Data
    └─ USGS Earthquake Data
    ↓
[Interactive Map (index.html)]
    └─ Show locations with alerts
```

### File-by-File Explanation

| File                     | Purpose             | What It Does                                                |
| ------------------------ | ------------------- | ----------------------------------------------------------- |
| **app.py**               | Main Web Server     | Receives your requests, processes them, sends back results  |
| **geoparser.py**         | AI Brain            | Reads text, extracts place names, handles spelling mistakes |
| **places_db.py**         | Geographic Database | Stores coordinates for 67 countries, 37 states, 144 cities  |
| **templates/index.html** | Web Interface       | Beautiful UI where you type questions and see the map       |
| **requirements.txt**     | Dependencies List   | Lists all libraries needed to run this project              |

---

## 📦 Libraries Explained (For Beginners)

### What are libraries?

Libraries are pre-written code that other people created. Instead of writing everything from scratch, we use libraries to save time and effort.

### Each Library Explained:

#### 1. **Flask** — Web Framework

- **What it does**: Allows you to create websites using Python
- **Why we use it**: Makes it easy to create web pages and handle user requests
- **How it works**:
  ```
  User visits website → Flask receives request → Python code runs → Flask sends response back
  ```
- **Example**: When you type in the text box and click "Parse", Flask receives that request

#### 2. **spaCy** — Natural Language Processing (NLP)

- **What it does**: Teaches computers to understand human language like we do
- **Why we use it**: Can recognize place names (like "Mumbai" or "California") automatically
- **How it works**:
  - Reads each word in your sentence
  - Identifies what kind of word it is (location, person, company, etc.)
  - Finds proper nouns (words that start with capital letters = place names)
- **Example**: You say "I love Paris" → spaCy identifies "Paris" as a location (GPE = Geopolitical Entity)

#### 3. **rapidfuzz** — Fuzzy Matching

- **What it does**: Finds the closest match when there are spelling mistakes
- **Why we use it**: Users might type "Mumbay" instead of "Mumbai" or "Deli" instead of "Delhi"
- **How it works**:
  - You search for "Indya"
  - rapidfuzz checks: "Is this similar to India?" (99% match!)
  - Returns "India" as the correct spelling
- **Example**:
  ```
  Your input: "Indya"
  Database has: "India"
  Score: 95% match
  Result: "India" ✓
  ```

#### 4. **requests** — HTTP Library

- **What it does**: Downloads data from the internet
- **Why we use it**: We need to fetch real-time disaster data from NASA and USGS
- **How it works**:
  - Asks NASA servers: "Give me earthquake data"
  - NASA sends back: Earthquake information
  - We show it to you on the map
- **Example**: Getting live earthquake data from USGS API (Application Programming Interface)

---

## 🚀 Installation Guide (Step-by-Step)

### Step 1: Install Python

- Download Python from https://www.python.org/
- Make sure to check "Add Python to PATH" during installation

### Step 2: Open Command Prompt / Terminal

- **Windows**: Press `Win + R`, type `cmd`, press Enter
- **Mac/Linux**: Open Terminal from Applications

### Step 3: Navigate to Project Folder

```bash
cd Downloads\Geospatial-Query-Engine-main
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

**What this does**: Installs Flask, spaCy, rapidfuzz, and requests

### Step 5: Download spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

**What this does**: Downloads the AI model that understands English

### Step 6: Run the Application

```bash
python app.py
```

**Expected output**:

```
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

### Step 7: Open in Browser

- Copy the link from the command prompt: `http://127.0.0.1:5000`
- Paste it in your web browser
- **Done!** Now you can use the application

---

## 💻 How to Use the Application

### Using the Web Interface

1. **Type your query** in the text box
   - Example: "Show me earthquakes in Japan"
   - Example: "What cities are in Karnataka?"
   - Example: "Places near Mumbai"

2. **Click "Parse"** button
   - The system extracts place names from your text

3. **Click on a Result** to see it on the map
   - Map shows the location with a pin
   - Real-time alerts appear (if any disasters happening)

4. **View the Map**
   - Red/Orange pins = Disasters/Alerts
   - Blue pins = Your search locations
   - Toggle between Street and Satellite views

### Example Queries to Try

```
"Which states are in north India?"
"Show earthquakes near Mumbai"
"What is the weather in Delhi?"
"List all countries in Asia"
"Find cities in California"
```

---

## 🔌 API Endpoints (For Developers)

### Endpoint 1: Parse Geospatial Entities

**URL**: `POST http://localhost:5000/parse`

```json
Request:
{
  "sentence": "Which cities are in Maharashtra?"
}

Response:
[
  {
    "token": "Maharashtra",
    "canonical": "maharashtra",
    "lat": 19.75,
    "lon": 75.71,
    "match_score": 100,
    "type": "State"
  }
]
```

### Endpoint 2: Get Real-time Alerts

**URL**: `POST http://localhost:5000/alerts`

```json
Request:
{
  "latitude": 19.75,
  "longitude": 75.71,
  "place_name": "maharashtra"
}

Response:
{
  "earthquakes": [...],
  "natural_events": [...],
  "weather_alerts": [...]
}
```

---

## ⚙️ Customization Guide

### Change Fuzzy Matching Sensitivity

Open `geoparser.py` and find this line:

```python
MATCH_THRESHOLD = 70
```

- **90+** = Very strict (only accept very similar names)
- **70-80** = Balanced (default, catches most typos)
- **50-60** = Lenient (might have false matches)

---

## 📊 Database Content (places_db.py)

The database includes:

- **67 Countries**: India, USA, China, Brazil, etc.
- **37 States/Provinces**: Maharashtra, California, Texas, etc.
- **144 Cities**: Mumbai, Delhi, New York, London, Tokyo, etc.
- **Each has**: Latitude and Longitude coordinates

Each place stores:

```python
"Mumbai": (19.08, 72.88)  # City name: (latitude, longitude)
```

---

## 🐛 Troubleshooting

### Problem: "Module not found" error

**Solution**: Run `pip install -r requirements.txt` again

### Problem: spaCy model error

**Solution**: Run `python -m spacy download en_core_web_sm`

### Problem: Port 5000 already in use

**Solution**: Change port in `app.py`:

```python
app.run(debug=True, port=5001)  # Changed from 5000 to 5001
```

### Problem: Map not showing

**Solution**: Check your internet connection (map requires internet for Leaflet library)

---

## 📈 Next Steps to Learn More

1. **Add more cities** to `places_db.py`
2. **Improve NLP** by trying different spaCy models
3. **Add weather data** integration
4. **Build a mobile app** using Flask
5. **Add database** (SQLite/MongoDB) instead of hardcoded data
6. **Deploy to cloud** (Heroku, Azure, AWS)

---

## 🤝 Contributing

Found a bug? Want to add more cities? Create a Pull Request!

---

## 📝 Summary

This project teaches you how:

- **Computers understand human language** (NLP with spaCy)
- **To handle user mistakes gracefully** (fuzzy matching with rapidfuzz)
- **To build web applications** (Flask framework)
- **To work with geographic data** (latitude, longitude, coordinates)
- **To fetch real-time data** (requests library, NASA API)
- **To create interactive maps** (Leaflet, HTML/CSS)

**Great job on learning this!** You're now understanding real-world AI and web development concepts! 🎉
