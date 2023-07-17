import random

def assess_traffic_congestion():
    # Simulate traffic data
    traffic_data = [random.randint(0, 50) for _ in range(24)]
    
    # Calculate average traffic volume
    avg_traffic = sum(traffic_data) / len(traffic_data)
    
    # Determine congestion level based on average traffic volume
    if avg_traffic < 10:
        congestion_level = "Very Low"
    elif avg_traffic < 20:
        congestion_level = "Low"
    elif avg_traffic < 30:
        congestion_level = "Moderate"
    elif avg_traffic < 40:
        congestion_level = "High"
    else:
        congestion_level = "Very High"
        
    return congestion_level
