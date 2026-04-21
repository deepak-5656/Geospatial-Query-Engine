from flask import Flask, request, jsonify, render_template
import logging
from geoparser import parse_geonames

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def home():
    """Serve the main HTML interface."""
    return render_template("index.html")


@app.route("/parse", methods=["POST"])
def parse():
    """
    Parse geospatial entities from a sentence.
    
    Expected JSON input:
    {
        "sentence": "Which of the following saw the highest average temperature in January, Maharashtra, Ahmedabad or entire New-Zealand?"
    }
    
    Response format:
    {
        "success": true,
        "sentence": "...",
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
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "error": "Request body must be valid JSON"
            }), 400
        
        sentence = data.get("sentence", "").strip()

        if not sentence:
            return jsonify({
                "success": False,
                "error": "No sentence provided. Please provide a 'sentence' field."
            }), 400

        logger.info(f"Parsing sentence: {sentence}")
        results = parse_geonames(sentence)
        
        return jsonify({
            "success": True,
            "sentence": sentence,
            "results": results,
            "count": len(results),
            "message": f"Successfully parsed {len(results)} geospatial entities"
        }), 200
        
    except Exception as e:
        logger.error(f"Error parsing sentence: {str(e)}")
        return jsonify({
            "success": False,
            "error": f"Internal server error: {str(e)}"
        }), 500


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "Geospatial Query Engine"
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
