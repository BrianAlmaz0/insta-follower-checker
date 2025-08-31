import json

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    # Load following and followers JSON
    following_data = load_json("following.json")
    followers_data = load_json("followers_1.json")

    # Extract usernames (Instagram data structure has nested fields)
    following = {entry["string_list_data"][0]["value"] for entry in following_data["relationships_following"]}
    followers = {entry["string_list_data"][0]["value"] for entry in followers_data}

    # Find non-followers
    not_following_back = following - followers

    print(f"People you follow who don’t follow you back ({len(not_following_back)}):")
    for user in sorted(not_following_back):
        print(user)

if __name__ == "__main__":
    main()
