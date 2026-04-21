# Geospatial Query Engine

A natural language processing system that identifies geospatial entities (place names) from user queries with intelligent fuzzy matching to handle spelling variations and provide canonical names.

## Features

✨ **Smart Place Recognition**

- Extracts geographic entities using spaCy NLP (recognizes GPE and LOC entities)
- Identifies proper nouns as potential place names
- Supports three geographic levels: Countries, States, and Cities

🔤 **Intelligent Fuzzy Matching**

- Handles spelling variations and typos (e.g., "Indya" → "India", "Londan" → "London")
- Normalizes hyphens and alternate separators ("New-Zealand" → "new zealand")
- Provides confidence scores for each match

📝 **Multiple Query Formats**

- Questions: "Which of the following saw the highest average temperature in January, Maharashtra, Ahmedabad or entire New-Zealand?"
- Imperative: "Show me a graph of rainfall for Chennai for the month of October"
- Statements: "Compare population of Indya and Austrla"

## Installation

### Prerequisites

- Python 3.7+
- pip

### Setup

```bash
# Clone or navigate to the project directory
cd Geospatial-Query-Engine-main

# Install required Python packages
pip install -r requirements.txt

# Download spaCy language model
python -m spacy download en_core_web_sm
```

## Usage

### Run the Web Interface

```bash
python app.py
```

Then open http://localhost:5000 in your browser.

**API Endpoint:** POST `/parse`

Request:

```json
{
  "sentence": "Which cities are in Maharashtra and what is their weather?"
}
```

Response:

```json
{
  "success": true,
  "sentence": "Which cities are in Maharashtra and what is their weather?",
  "results": [
    {
      "token": "Maharashtra",
      "canonical_name": "maharashtra",
      "table": "State",
      "confidence": 100.0
    }
  ],
  "count": 1,
  "message": "Successfully parsed 1 geospatial entities"
}
```

### Test Core Logic

```bash
python geoparser.py
```

This runs 5 test cases demonstrating the system's capabilities:

1. **Temperature query** with multiple place types
2. **Rainfall query** (imperative format)
3. **Population comparison** with misspellings
4. **Area query** with spelling variations
5. **Weather data request** with international places

## System Architecture

### Components

**`geoparser.py`** - Core NLP and matching engine

- `normalize_token()` - Normalizes user input (handles hyphens, spaces)
- `extract_candidates_nlp()` - Uses spaCy to identify place name candidates
- `fuzzy_match_token()` - Finds best canonical name match across tables
- `parse_geonames()` - Main processing function

**`places_db.py`** - Canonical database of place names

- 60+ countries (COUNTRIES table)
- 35+ Indian states (STATES table)
- 140+ cities (CITIES table)

**`app.py`** - Flask web server

- GET `/` - Serves HTML interface
- POST `/parse` - Processes natural language queries
- GET `/health` - Health check endpoint

**`templates/index.html`** - Web UI with example queries

## Processing Pipeline

```
User Input (Natural Language Query)
           ↓
    [NLP Extraction]
    - Extract Named Entities (GPE, LOC)
    - Extract Proper Nouns (PROPN)
           ↓
    [Candidate Normalization]
    - Remove duplicates
    - Filter subwords
           ↓
    [Fuzzy Matching]
    - Match against Country table (WRatio scorer)
    - Match against State table
    - Match against City table
           ↓
    [Output]
    - Return canonical names
    - Provide confidence scores
    - Classify by geographic table
```

## Examples

### Example 1: Question with Multiple Locations

**Input:**

```
Which of the following saw the highest average temperature in January, Maharashtra, Ahmedabad or entire New-Zealand?
```

**Output:**

```
Token: New-Zealand  → Canonical: new zealand      Table: Country   Confidence: 100.0%
Token: Maharashtra → Canonical: maharashtra       Table: State     Confidence: 100.0%
Token: Ahmedabad   → Canonical: ahmedabad        Table: City      Confidence: 100.0%
```

### Example 2: Imperative with Exact Match

**Input:**

```
Show me a graph of rainfall for Chennai for the month of October
```

**Output:**

```
Token: Chennai → Canonical: chennai  Table: City  Confidence: 100.0%
```

### Example 3: Handling Misspellings

**Input:**

```
Compare population of Indya and Austrla
```

**Output:**

```
Token: Indya    → Canonical: india       Table: Country  Confidence: 80.0%
Token: Austrla  → Canonical: australia   Table: Country  Confidence: 87.5%
```

## Configuration

### Match Threshold

In `geoparser.py`, adjust the MATCH_THRESHOLD to control fuzzy matching strictness:

```python
MATCH_THRESHOLD = 72  # 0-100, higher = stricter matching
```

- **72** (default): Good balance - catches misspellings, avoids false positives
- **80+**: Stricter - only very close matches
- **60-70**: Looser - more permissive fuzzy matching

### Adding More Places

Edit `places_db.py` and add entries to COUNTRIES, STATES, or CITIES lists:

```python
COUNTRIES = [
    ...,
    "new country name",
    ...
]
```

## Requirements

- flask - Web framework
- rapidfuzz - Fuzzy string matching
- spacy - Natural Language Processing
- numpy - Numerical computing (spaCy dependency)

## Performance

- **Latency**: ~100-500ms per query (depending on sentence length)
- **Accuracy**:
  - Exact matches: 100%
  - Misspellings: 80-95% (depending on edit distance)
  - Unrecognized places: 0% (filtered out)

## License

SIH 1517 (ISRO) Challenge

## Notes

- The system respects the input case but matches canonically against lowercase database
- Multi-word place names are correctly handled (e.g., "new zealand", "uttar pradesh")
- Duplicate matches are automatically deduplicated
- Confidence scores use the WRatio algorithm (0-100%)
