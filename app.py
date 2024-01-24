from flask import Flask, request, jsonify


app = Flask(__name__)


users = []
user_id_counter = 1


@app.route("/api/welcome", methods=['GET'])
def welcome():
    return jsonify(message="Hi, this is your API!")


@app.route("/api/greet/<name>", methods=['GET'])
def greet(name):
    return jsonify(message=f"Hello, {name.title()}!")


# Checking the uniqueness of a new username
def is_name_unique(user_name):
    return all(user['user_name'] != user_name for user in users)


# POST request - receives "user_name", "gender", "age" in the request body
@app.route("/api/users", methods=['POST'])
def create_user():
    global user_id_counter
    data = request.get_json()

    if "user_name" not in data or "gender" not in data or "age" not in data:
        return jsonify(error="Missing required fields"), 400

    new_user = {
        "id": user_id_counter,
        "user_name": data["user_name"],
        "gender": data["gender"],
        "age": data["age"]
    }

    # displaying an error if a username already exists
    if not is_name_unique(data['user_name']):
        return jsonify(error=f"User '{data['user_name']}' already exists"), 400
    else:
        # adding a new user if username is unique and increment the id counter
        users.append(new_user)
        user_id_counter += 1

    # displaying a message after a successful user creation
    return jsonify(message=
                   f"User '{new_user["user_name"]}' created successfully"), 201


@app.route("/api/users", methods=['GET'])
def get_users():
    return jsonify({"users": users})


# Get a user by id
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


# DELETE request - receives only "id" in the body
@app.route("/api/users", methods=["DELETE"])
def delete_user():
    global user_id_counter
    data = request.get_json()
    user_id = data.get("id")  # getting the id from json object

    if user_id is not None:
        user_to_delete = get_user_by_id(user_id)  # getting the id of a user

        # deleting a user if the specified id matches the user id
        if user_to_delete:
            user_name = user_to_delete.get('user_name')
            users.remove(user_to_delete)
            user_id_counter -= 1  # decrease the global user id counter

            """decreasing the id of each remaining user from the users list 
            after deleting
            """
            for user in users:
                user["id"] -= 1

            return jsonify(message=
                           f"User '{user_id}' ('{user_name}') "
                           f"deleted successfully")
        else:
            # displaying an error if there is no user with such id
            return jsonify(error="User not found"), 404
    else:
        # displaying an error if other key is passed in the body
        return jsonify(error="'id' is required in the request body"), 400


if __name__ == "__main__":
    app.run()
