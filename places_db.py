"""
Geospatial Database: Canonical names for Countries, States, and Cities with coordinates.

This module provides the universe of canonical (standardized) place names
with latitude/longitude coordinates for map visualization.
"""

# Countries with coordinates (lat, lon)
COUNTRIES = {
    "afghanistan": (33.9391, 67.2994),
    "albania": (41.1533, 20.1683),
    "algeria": (28.0339, 1.6596),
    "argentina": (-38.4161, -63.6167),
    "australia": (-25.2744, 133.7751),
    "austria": (47.5162, 14.5501),
    "bangladesh": (23.6850, 90.3563),
    "belgium": (50.5039, 4.4699),
    "brazil": (-14.2350, -51.9253),
    "canada": (56.1304, -106.3468),
    "chile": (-35.6751, -71.5430),
    "china": (35.8617, 104.1954),
    "colombia": (4.5709, -74.2973),
    "denmark": (56.2639, 9.5018),
    "egypt": (26.8206, 30.8025),
    "ethiopia": (9.1450, 40.4897),
    "finland": (61.9241, 25.7482),
    "france": (46.2276, 2.2137),
    "germany": (51.1657, 10.4515),
    "ghana": (7.3697, -5.5825),
    "greece": (39.0742, 21.8243),
    "hungary": (47.1625, 19.5033),
    "india": (20.5937, 78.9629),
    "indonesia": (-0.7893, 113.9213),
    "iran": (32.4279, 53.6880),
    "iraq": (33.3128, 44.3615),
    "ireland": (53.4129, -8.2439),
    "israel": (31.0461, 34.8516),
    "italy": (41.8719, 12.5674),
    "japan": (36.2048, 138.2529),
    "jordan": (30.5852, 36.2384),
    "kenya": (-0.0236, 37.9062),
    "malaysia": (4.2105, 101.6964),
    "mexico": (23.6345, -102.5528),
    "morocco": (31.7917, -7.0926),
    "myanmar": (21.9162, 95.9560),
    "nepal": (28.3949, 84.1240),
    "netherlands": (52.1326, 5.2913),
    "new zealand": (-40.9006, 174.8860),
    "nigeria": (9.0820, 8.6753),
    "norway": (60.4720, 8.4689),
    "pakistan": (30.3753, 69.3451),
    "peru": (-9.1900, -75.0152),
    "philippines": (12.8797, 121.7740),
    "poland": (51.9194, 19.1451),
    "portugal": (39.3999, -8.2245),
    "romania": (45.9432, 24.9668),
    "russia": (61.5240, 105.3188),
    "saudi arabia": (23.8859, 45.0792),
    "singapore": (1.3521, 103.8198),
    "south africa": (-30.5595, 22.9375),
    "south korea": (35.9078, 127.7669),
    "spain": (40.4637, -3.7492),
    "sri lanka": (7.8731, 80.7718),
    "sweden": (60.1282, 18.6435),
    "switzerland": (46.8182, 8.2275),
    "syria": (34.8021, 38.9968),
    "taiwan": (23.6978, 120.9605),
    "thailand": (15.8700, 100.9925),
    "turkey": (38.9637, 35.2433),
    "ukraine": (48.3794, 31.1656),
    "united arab emirates": (23.4241, 53.8478),
    "united kingdom": (55.3781, -3.4360),
    "united states": (37.0902, -95.7129),
    "venezuela": (6.4238, -66.5897),
    "vietnam": (14.0583, 108.2772),
    "zimbabwe": (-19.0154, 29.1549),
}

# Indian States with coordinates (lat, lon)
STATES = {
    "andhra pradesh": (15.9129, 78.6675),
    "arunachal pradesh": (28.2180, 94.7278),
    "assam": (26.1445, 94.5771),
    "bihar": (25.0961, 85.3131),
    "chhattisgarh": (21.2787, 81.8661),
    "goa": (15.2993, 73.8243),
    "gujarat": (22.2587, 71.1924),
    "haryana": (29.0588, 75.6753),
    "himachal pradesh": (31.7433, 77.1205),
    "jharkhand": (23.6102, 85.2799),
    "karnataka": (15.3173, 75.7139),
    "kerala": (10.8505, 76.2711),
    "madhya pradesh": (22.9068, 78.6569),
    "maharashtra": (19.7515, 75.7139),
    "manipur": (24.6637, 93.9063),
    "meghalaya": (25.4670, 91.3662),
    "mizoram": (23.1645, 92.9376),
    "nagaland": (26.1584, 94.5624),
    "odisha": (20.9517, 85.0985),
    "punjab": (31.1471, 75.3412),
    "rajasthan": (27.0238, 74.2179),
    "sikkim": (27.5330, 88.5122),
    "tamil nadu": (11.1271, 79.2803),
    "telangana": (18.1124, 79.0193),
    "tripura": (23.9408, 91.9882),
    "uttar pradesh": (26.8467, 80.9462),
    "uttarakhand": (30.0668, 79.0193),
    "west bengal": (24.5155, 88.2289),
    "delhi": (28.7041, 77.1025),
    "jammu and kashmir": (33.7782, 76.5769),
    "ladakh": (34.1526, 77.5773),
    "chandigarh": (30.7333, 76.7794),
    "puducherry": (12.0657, 79.8711),
    "andaman and nicobar islands": (11.7401, 92.6586),
    "dadra and nagar haveli": (20.1809, 73.0533),
    "daman and diu": (20.6329, 72.8479),
    "lakshadweep": (10.5667, 72.7417),
}

# Major Cities with coordinates (lat, lon)
CITIES = {
    "mumbai": (19.0760, 72.8777),
    "delhi": (28.7041, 77.1025),
    "bangalore": (12.9716, 77.5946),
    "hyderabad": (17.3850, 78.4867),
    "ahmedabad": (23.0225, 72.5714),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "surat": (21.1705, 72.8311),
    "pune": (18.5204, 73.8567),
    "jaipur": (26.9124, 75.7873),
    "lucknow": (26.8467, 80.9462),
    "kanpur": (26.4499, 80.3319),
    "nagpur": (21.1458, 79.0882),
    "indore": (22.7196, 75.8577),
    "thane": (19.2183, 72.9781),
    "bhopal": (23.1815, 77.4104),
    "visakhapatnam": (17.6869, 83.2185),
    "pimpri-chinchwad": (18.6298, 73.8114),
    "patna": (25.5941, 85.1376),
    "vadodara": (22.3072, 73.1812),
    "ghaziabad": (28.6692, 77.4538),
    "ludhiana": (30.9010, 75.8573),
    "agra": (27.1767, 78.0081),
    "nashik": (19.9975, 73.7898),
    "faridabad": (28.4089, 77.3178),
    "meerut": (28.9845, 77.7064),
    "rajkot": (22.3039, 70.8022),
    "kalyan-dombivali": (19.2403, 73.1305),
    "vasai-virar": (19.5330, 72.7920),
    "varanasi": (25.3176, 82.9739),
    "srinagar": (34.0837, 74.7973),
    "aurangabad": (19.8762, 75.3433),
    "dhanbad": (23.7957, 86.4304),
    "amritsar": (31.6340, 74.8723),
    "navi mumbai": (19.0330, 73.0297),
    "allahabad": (25.4358, 81.8463),
    "ranchi": (23.3441, 85.3096),
    "howrah": (22.5958, 88.2636),
    "coimbatore": (11.0026, 76.9124),
    "jabalpur": (23.1815, 79.9864),
    "gwalior": (26.2183, 78.1634),
    "vijayawada": (16.5062, 80.6480),
    "jodhpur": (26.2389, 73.0243),
    "madurai": (9.9252, 78.1198),
    "raipur": (21.2514, 81.6296),
    "kota": (25.2138, 75.8648),
    "chandigarh": (30.7333, 76.7794),
    "guwahati": (26.1445, 91.7362),
    "solapur": (17.6569, 75.9064),
    "hubballi-dharwad": (15.3647, 75.1240),
    "mysore": (12.2958, 76.6394),
    "tiruchirappalli": (10.7905, 78.7047),
    "bareilly": (28.3670, 79.4304),
    "aligarh": (27.8974, 77.8912),
    "tiruppur": (11.1087, 77.3411),
    "moradabad": (28.8385, 77.7597),
    "jalandhar": (31.7264, 75.5761),
    "bhubaneswar": (20.2961, 85.8245),
    "salem": (11.6643, 78.1460),
    "warangal": (17.9689, 79.5941),
    "mira-bhayandar": (19.6783, 72.6405),
    "thiruvananthapuram": (8.5241, 76.9366),
    "bhiwandi": (19.2835, 73.0561),
    "saharanpur": (29.9676, 77.5619),
    "guntur": (16.5864, 80.4458),
    "amravati": (20.8439, 77.7539),
    "bikaner": (28.0229, 71.4882),
    "noida": (28.5355, 77.3910),
    "jamshedpur": (22.8045, 84.8790),
    "bhilai": (21.1938, 81.3304),
    "cuttack": (20.4625, 85.8830),
    "firozabad": (27.1480, 77.8482),
    "kochi": (9.9312, 76.2673),
    "dehradun": (30.3165, 78.0322),
    "durgapur": (23.5185, 87.3228),
    "asansol": (23.6858, 86.9646),
    "nanded": (19.1647, 77.3173),
    "kolhapur": (17.7330, 73.7325),
    "ajmer": (26.4499, 74.6399),
    "akola": (20.7136, 77.0994),
    "gulbarga": (17.3373, 76.8343),
    "jamnagar": (22.4707, 70.0883),
    "ujjain": (23.1815, 75.7873),
    "loni": (28.7041, 77.0541),
    "siliguri": (26.7271, 88.4230),
    "jhansi": (25.4358, 78.5976),
    "ulhasnagar": (19.2035, 73.1550),
    "jammu": (32.7266, 74.8570),
    "sangli-miraj & kupwad": (17.3666, 74.5606),
    "mangalore": (12.8628, 74.8628),
    "erode": (11.3919, 79.1159),
    "belgaum": (15.8601, 74.5029),
    "ambattur": (13.0721, 80.1348),
    "tirunelveli": (8.7642, 77.7567),
    "malegaon": (20.5522, 74.5275),
    "gaya": (24.7955, 84.9994),
    "jalgaon": (21.1458, 75.5625),
    "udaipur": (24.5854, 73.7125),
    "maheshtala": (22.4474, 88.3278),
    "davanagere": (14.4644, 75.9226),
    "kolapur": (17.6550, 74.2433),
    "rajpur sonarpur": (22.5136, 88.3236),
    "rajahmundry": (16.9891, 81.8044),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "paris": (48.8566, 2.3522),
    "tokyo": (35.6762, 139.6503),
    "beijing": (39.9042, 116.4074),
    "dubai": (25.2048, 55.2708),
    "singapore": (1.3521, 103.8198),
    "sydney": (-33.8688, 151.2093),
    "toronto": (43.6532, -79.3832),
    "berlin": (52.5200, 13.4050),
    "moscow": (55.7558, 37.6173),
    "istanbul": (41.0082, 28.9784),
    "shanghai": (31.2304, 121.4737),
    "los angeles": (34.0522, -118.2437),
    "chicago": (41.8781, -87.6298),
    "houston": (29.7604, -95.3698),
    "phoenix": (33.4484, -112.0742),
    "philadelphia": (39.9526, -75.1652),
    "san antonio": (29.4241, -98.4936),
    "san diego": (32.7157, -117.1611),
    "dallas": (32.7767, -96.7970),
    "san jose": (37.3382, -121.8863),
    "austin": (30.2672, -97.7431),
    "washington": (38.9072, -77.0369),
    "boston": (42.3601, -71.0589),
    "seattle": (47.6062, -122.3321),
    "denver": (39.7392, -104.9903),
    "nashville": (36.1627, -86.7816),
    "karachi": (24.8607, 66.9937),
    "dhaka": (23.8103, 90.4125),
    "lahore": (31.5497, 74.3436),
    "colombo": (6.9271, 80.7580),
    "kathmandu": (27.7172, 85.3240),
    "kabul": (34.5199, 69.1789),
    "tehran": (35.6895, 51.3896),
    "riyadh": (24.7136, 46.6753),
    "cairo": (30.0444, 31.2357),
    "nairobi": (-1.2921, 36.8219),
    "lagos": (6.5244, 3.3792),
    "johannesburg": (-26.2023, 28.0436),
}

ALL_TABLES = {
    "Country": COUNTRIES,
    "State": STATES,
    "City": CITIES
}


def get_canonical_name(table_name, canonical_name):
    """
    Retrieve a canonical name from a specific table with coordinates.
    
    Args:
        table_name: Table to search ('Country', 'State', or 'City')
        canonical_name: The name to search for
        
    Returns:
        Tuple of (canonical_name, lat, lon) if found, None otherwise
    """
    if table_name not in ALL_TABLES:
        return None
    
    table = ALL_TABLES[table_name]
    for name, coords in table.items():
        if name.lower() == canonical_name.lower():
            return (name, coords[0], coords[1])
    return None


def get_coordinates(table_name, place_name):
    """
    Get latitude and longitude coordinates for a place.
    
    Args:
        table_name: Table to search ('Country', 'State', or 'City')
        place_name: The place name to search for
        
    Returns:
        Tuple of (lat, lon) if found, None otherwise
    """
    if table_name not in ALL_TABLES:
        return None
    
    table = ALL_TABLES[table_name]
    for name, coords in table.items():
        if name.lower() == place_name.lower():
            return coords
    return None


def get_all_places(table_name=None):
    """
    Get all places from a specific table or all tables.
    
    Args:
        table_name: Specific table to retrieve ('Country', 'State', 'City'), or None for all
        
    Returns:
        Dictionary with table(s) and their places with coordinates
    """
    if table_name:
        if table_name in ALL_TABLES:
            return {table_name: ALL_TABLES[table_name]}
        return {}
    return ALL_TABLES

