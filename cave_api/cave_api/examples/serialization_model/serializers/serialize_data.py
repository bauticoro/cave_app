import json
from cave_api.serialization_model.serializers.keys import specified_keys, data_location
from cave_api.serialization_model.utils import enumerate_dir, drop_none
from cave_api.serialization_model.serializers.categories import get_categories_data
from pamda import pamda


def get_file_data(data_dir):
    for _, filename in enumerate_dir(data_dir):
        if filename[-3:] == "csv":
            csv_filename = filename
        else:
            json_filename = filename
    with open(data_dir + json_filename) as f:
        types = json.load(f)

    return {"types": types}, drop_none(pamda.read_csv(data_dir + csv_filename, cast_items=True))


def validate_required_keys(required_keys, data):
    for key in required_keys:
        for element_dict in data.values():
            if key not in element_dict.keys():
                raise ValueError("Missing one or more required keys")


def get_data(data_dir):
    returnable, raw_data = get_file_data(data_dir)

    required_keys = specified_keys.get(data_dir.replace(data_location, "").replace("/", "")).get(
        "required_keys", []
    )
    optional_keys = specified_keys.get(data_dir.replace(data_location, "").replace("/", "")).get(
        "optional_keys", []
    )

    categories = get_categories_data(data_location + "categories/")["data"]
    data = {}
    for element in raw_data:
        element_id = element.pop("id")
        element_dict = {}

        for key, item in element.items():
            if key in required_keys or key in optional_keys:
                if item is not None:
                    if key == "path":
                        item = json.loads(item)
                    element_dict[key] = item
                else:
                    if key in required_keys:
                        raise ValueError(
                            f"Recieved a None value for {key}, but this key is required"
                        )
            elif key in categories.keys():
                if "category" not in element_dict.keys():
                    element_dict["category"] = {}
                element_dict["category"][key] = item.split()
            else:
                if "props" not in element_dict.keys():
                    element_dict["props"] = {}
                try:
                    element_dict["props"][key] = {"value": json.loads(item)}
                except:
                    element_dict["props"][key] = {"value": item}
        data[element_id] = element_dict

    validate_required_keys(required_keys, data)
    returnable["data"] = data
    return returnable
