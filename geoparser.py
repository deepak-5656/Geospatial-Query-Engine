import spacy
import re
from rapidfuzz import process, fuzz
from places_db import ALL_TABLES

nlp = spacy.load("en_core_web_sm")

MATCH_THRESHOLD = 72


def normalize_token(token):
    """Normalize token by converting hyphens/underscores to spaces and removing extra whitespace."""
    normalized = re.sub(r'[-_]+', ' ', token)
    normalized = re.sub(r'\s+', ' ', normalized).strip()
    return normalized


def extract_candidates_nlp(sentence):
    """
    Extract place name candidates from sentence using NLP and proper noun detection.
    
    Process:
    1. Identify Named Entities labeled as GPE (Geopolitical) or LOC (Location)
    2. Extract all PROPN (Proper Noun) tokens
    3. Remove duplicate candidates
    4. Filter out subwords (tokens that are parts of larger multi-word candidates)
    
    Returns: List of unique candidate place names
    """
    doc = nlp(sentence)

    candidates = []

    # Extract named entities recognized as geographical or location entities
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:
            candidates.append(ent.text)

    # Extract additional proper nouns that might have been missed
    for token in doc:
        if token.pos_ == "PROPN" and token.text.strip():

            part_of_existing = False

            for existing in candidates:
                if token.text.lower() in existing.lower().split():
                    part_of_existing = True
                    break

            if not part_of_existing and token.text not in candidates:
                candidates.append(token.text)

    # Remove case-insensitive duplicates
    seen = set()
    unique = []

    for c in candidates:
        if c.lower() not in seen:
            seen.add(c.lower())
            unique.append(c)

    # Remove subwords - filter out tokens that are parts of larger multi-word candidates
    final_candidates = []

    for candidate in unique:
        is_subword = False

        for other in unique:
            if candidate != other:
                words = other.lower().split()

                if len(words) > 1 and candidate.lower() in words:
                    is_subword = True
                    break

        if not is_subword:
            final_candidates.append(candidate)

    return final_candidates


def fuzzy_match_token(token):
    """
    Find the best matching canonical name for a given token across all tables.
    
    Process:
    1. Normalize the token (handle hyphens, spaces)
    2. Perform fuzzy matching against each table using WRatio scorer
    3. Return the best match with highest confidence and coordinates
    
    Args:
        token: The place name token to match
        
    Returns:
        Dictionary with token, canonical_name, table, confidence, and coordinates; or None if no match
    """
    normalized_token = normalize_token(token)
    best_match = None
    best_score = 0
    best_table = None
    best_coords = None

    for table_name, place_dict in ALL_TABLES.items():
        # Extract place names from dictionary keys
        place_names = list(place_dict.keys())
        
        result = process.extractOne(
            normalized_token.lower(),
            place_names,
            scorer=fuzz.WRatio,
            score_cutoff=MATCH_THRESHOLD
        )

        if result and result[1] > best_score:
            best_match = result[0]
            best_score = result[1]
            best_table = table_name
            best_coords = place_dict[best_match]

    if best_match:
        return {
            "token": token,
            "canonical_name": best_match,
            "table": best_table,
            "confidence": round(best_score, 1),
            "latitude": round(best_coords[0], 4),
            "longitude": round(best_coords[1], 4)
        }

    return None


def parse_geonames(sentence):
    """
    Parse a sentence and identify all geospatial entities with canonical mappings.
    
    Full process:
    1. Extract place name candidates using NLP (named entities + proper nouns)
    2. Perform fuzzy matching on each candidate against canonical tables
    3. Filter duplicates (same canonical name matched multiple times)
    4. Return results with confidence scores and table classification
    
    Args:
        sentence: Natural language text (question, statement, or imperative)
        
    Returns:
        List of dictionaries with:
        - token: Original text from input
        - canonical_name: Standardized spelling from database
        - table: Classification (Country/State/City)
        - confidence: Fuzzy match score (0-100%)
    """
    candidates = extract_candidates_nlp(sentence)

    results = []
    seen = set()

    for candidate in candidates:
        match = fuzzy_match_token(candidate)

        if match and match["canonical_name"] not in seen:
            results.append(match)
            seen.add(match["canonical_name"])

    return results

if __name__ == "__main__":
    # Test sentences covering different scenarios
    test_sentences = [
        # Example 1: Question with multiple place types
        "Which of the following saw the highest average temperature in January, Maharashtra, Ahmedabad or entire New-Zealand?",
        
        # Example 2: Imperative sentence
        "Show me a graph of rainfall for Chennai for the month of October",
        
        # Example 3: Statement with misspellings
        "Compare population of Indya and Austrla",
        
        # Example 4: Question with spelling variations
        "What is the area of Rajasthan and Gujrat?",
        
        # Example 5: Query with international places
        "Give me weather data for New York and Londan",
    ]

    print("=" * 80)
    print("GEOSPATIAL ENTITY PARSER - TEST RESULTS")
    print("=" * 80)
    
    for idx, sentence in enumerate(test_sentences, 1):
        print(f"\n[Test {idx}]")
        print(f"Input: {sentence}")
        print("-" * 80)
        
        results = parse_geonames(sentence)
        
        if results:
            for r in results:
                print(f"  Token: {r['token']:20} → Canonical: {r['canonical_name']:20} Table: {r['table']:8} Confidence: {r['confidence']:6.1f}%")
        else:
            print("  ✗ No place names found")
        print()

