from flask import Flask, request, jsonify


app = Flask(__name__)

# Disabling sorting keys of the JSON response
app.json.sort_keys = False


users = []
user_id_counter = 1

# --- HELPERS
# Checking the uniqueness of a new user_name
def is_name_unique(user_name):
    return all(user['user_name'] != user_name for user in users)

# Getting the user by id
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# --- GET /api/welcome
@app.route("/api/welcome", methods=['GET'])
def welcome():
    return jsonify(message="Hi, this is your API!")

# --- GET /api/greet/<string:name>
@app.route("/api/greet/<string:name>", methods=['GET'])
def greet(name):
    return jsonify(message=f"Hello, {name.title()}!")

# --- POST /api/users
@app.route("/api/users", methods=['POST'])
def create_user():
    global user_id_counter
    data = request.get_json(silent=True)

    if data is None:
        return jsonify(error="Invalid JSON"), 400

    # Defining all required fields for the POST request
    required_fields = ["user_name", "gender", "age"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        fields = ", ".join(f"'{field}'" for field in missing_fields)
        plural = "fields" if len(missing_fields) > 1 else "field"
        return jsonify(error=f"Missing {plural}: {fields}."), 422

    # Displaying an error if a username already exists
    if not is_name_unique(data['user_name']):
        return jsonify(error=f"User '{data['user_name']}' already exists."), 409

    # Displaying errors if values' data types are not valid
    if not isinstance(data["user_name"], str):
        return jsonify(error="'user_name' must be a string."), 422
    if not isinstance(data["gender"], str):
        return jsonify(error="'gender' must be a string."), 422
    if not isinstance(data["age"], int):
        return jsonify(error="'age' must be an integer."), 422

    new_user = {
        "id": user_id_counter,
        "user_name": data["user_name"],
        "gender": data["gender"],
        "age": data["age"]
    }

    # Adding a new user if username is unique and increment the id counter
    users.append(new_user)
    user_id_counter += 1

    # Displaying a message after a successful user creation
    return (jsonify(
        message=f"User '{new_user["user_name"]}' created successfully.",
        user=new_user),
            201)

# --- GET /api/users
@app.route("/api/users", methods=['GET'])
def get_users():
    return jsonify({"users": users})

# --- DELETE /api/users/<int:user_id>
@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global user_id_counter
    user_to_delete = get_user_by_id(user_id)

    if user_to_delete:
        user_name = user_to_delete.get('user_name')
        users.remove(user_to_delete)
        return jsonify(message=f"User '{user_name}' deleted successfully."), 200
    else:
        return jsonify(error=f"User with ID '{user_id}' not found."), 404

# --- PUT /api/users/<int:user_id>
@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json(silent=True)

    if data is None:
        return jsonify(error="Invalid JSON"), 400

    # Defining all required fields for the PUT request
    required_fields = ["user_name", "gender", "age"]
    missing_fields = [field for field in required_fields if field not in data]

    # Displaying an error if some field are missing
    if missing_fields:
        fields = ", ".join(f"'{field}'" for field in missing_fields)
        plural = "fields" if len(missing_fields) > 1 else "field"
        return jsonify(error=f"Missing {plural}: {missing_fields}."), 422

    # Displaying errors if values' data types are not valid
    if not isinstance(data['user_name'], str):
        return jsonify(error=f"'user_name' must be a string."), 422
    if not isinstance(data["gender"], str):
        return jsonify(error="'gender' must be a string."), 422
    if not isinstance(data["age"], int):
        return jsonify(error="'age' must be an integer."), 422

    user = get_user_by_id(user_id)
    if not user:
        return jsonify(error=f"User with ID '{user_id}' not found."), 404

    if not is_name_unique(data["user_name"]) and user["user_name"] != data["user_name"]:
        return jsonify(error=f"User '{data['user_name']}' already exists."), 409

    user.update(
        {
            "user_name": data["user_name"],
            "gender": data["gender"],
            "age": data["age"],
        }
    )

    # Displaying a message after a successful user info update
    return jsonify(message=f"User with ID '{user['id']}' updated successfully.", user=user), 200

# --- ERROR HANDLERS
@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Route not found. Please check the URL."), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(error="Method not allowed."), 405


if __name__ == "__main__":
    app.run(debug=True)
