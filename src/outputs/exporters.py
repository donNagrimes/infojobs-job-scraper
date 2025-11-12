thonimport json

def export_to_json(data, file_name='output.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)