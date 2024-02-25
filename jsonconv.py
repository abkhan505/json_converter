import json
import os

def transform_params(params):
    speaker = None
    text = []

    for param in params:
        if isinstance(param, str):
            if param in ["Lucia", "Liv", "Lee"]:
                speaker = param
            else:
                text.append(param)
        elif isinstance(param, int):
            text.append(str(param))
        elif isinstance(param, float):
            text.append(str(int(param)))  # Convert float to int, then to string
        else:
            text.append(str(param))

    return {
        "speaker": speaker,
        "text": " ".join(text)
    }
def transform_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    transformed_data = []
    for item in data:
        transformed_params = transform_params(item["Params"])
        transformed_item = {
            "id": item["Id"],
            "Actionid": item["ActionId"],
            "NextActionid": item["NextActionId"],
            "Type": item["Type"],
            "IsBlock": item["IsBlock"],
            "IsEnd": item["IsEnd"],
            "BeginAnim": item["BeginAnim"],
            "EndAnim": item["EndAnim"],
            "BeginDelay": item["BeginDelay"],
            "EndDelay": item["EndDelay"],
            "img": item.get("img"),
            "speaker": transformed_params["speaker"],
            "text": transformed_params["text"]
        }
        transformed_data.append(transformed_item)
    
    with open(output_file, 'w') as f:
        json.dump(transformed_data, f, indent=4)

def main():
    input_dir = "import"  # Directory containing input JSON files
    output_dir = "export"  # Directory to store output JSON files

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(input_dir):
        if file.endswith(".json"):
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(output_dir, file)
            transform_json(input_file, output_file)

if __name__ == "__main__":
    main()