@app.route('/api/data', methods=['POST'])
def store_data():
    # Authenticate request
    api_key = request.headers.get('api_key')
    if api_key != 'YOUR_API_KEY':
        return jsonify({'message': 'Invalid API key.'}), 401

    # Get data from request body
    data = request.get_json()

    # Store data in database or file
    # ...

    # Return success message
    return jsonify({'message': 'Data stored successfully.'}), 201

@app.route('/api/data', methods=['GET'])
def get_data():
    # Authenticate request
    api_key = request.headers.get('api_key')
    if api_key != 'YOUR_API_KEY':
        return jsonify({'message': 'Invalid API key.'}), 401

    # Retrieve data from database or file
    # ...

    # Convert data to JSON and return it
    return jsonify(data)

if __name__ == '__main__':
    app.run()
