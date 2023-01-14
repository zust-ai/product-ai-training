
from pathlib import Path
import requests



concepts_list = [
    {
        "instance_prompt":      "photo of baggitb1 handbag",
        "class_prompt":         "photo of a handbag",
        "instance_data_dir":    "subjects/baggitb1",
        "class_data_dir":       "/content/data/handbag",
        "custom_class_dirs": ["classes/handbag"]
    },
]

instance_images_path = []
for concept in concepts_list:
    inst_img_path = [(x, concept["instance_prompt"]) for x in Path(concept["instance_data_dir"]).iterdir() if x.is_file()]
    instance_images_path.extend(inst_img_path)

    for class_dir in concept.get('custom_class_dirs', []):
        inst_img_path = []
        for x in Path(class_dir).iterdir():
            if x.is_file() and x.suffix == '.jpg':
                txt_path = x.with_suffix('.txt')
                txt = ""
                with open(txt_path) as f:
                    txt = f.read()
                inst_img_path.append((x, txt))
        instance_images_path.extend(inst_img_path)

    # if with_prior_preservation:
    #     class_img_path = [(x, concept["class_prompt"]) for x in Path(concept["class_data_dir"]).iterdir() if x.is_file()]
    #     self.class_images_path.extend(class_img_path[:num_class_images])

print(instance_images_path)