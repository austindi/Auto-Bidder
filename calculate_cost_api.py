from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-cost', methods=['POST'])
def calculate_cost():
    data = request.get_json()
    print(f'Data: {data}')
    distance_miles = data.get("distance_miles", 0.0)
    weight_lbs = data.get("weight_lbs", 0.0)
    shipping_speed = data.get("shipping_speed", "standard")
    print(f'Distance: {distance_miles}, Weight: {weight_lbs}, Speed: {shipping_speed}')
    base_cost = 50.0  # USD
    cost_per_mile = 0.35
    cost_per_lb = 0.03
    speed_multiplier = 1.0 if shipping_speed == "standard" else 1.5

    total_cost = (
        base_cost +
        distance_miles * cost_per_mile +
        weight_lbs * cost_per_lb 
    ) * speed_multiplier

    return jsonify({
        "total_cost_usd": round(total_cost, 2),
        "details": {
            "base_cost": base_cost,
            "distance_charge": distance_miles * cost_per_mile,
            "weight_charge": weight_lbs * cost_per_lb,
            "speed_multiplier": speed_multiplier,
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
