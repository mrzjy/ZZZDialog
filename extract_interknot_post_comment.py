import argparse
import json
import os.path

from util import load_json


def parse(args, text_map: dict):
    # load interknot post
    data = load_json(os.path.join(args.repo, "FileCfg/InterKnotConfigTemplateTb.json"))
    post_mapping = {}
    for post in data["GMNCBMLIHPE"]:
        post_id = post["AGPIJOGPGEG"].split("_")[-1]
        post_mapping[post_id] = {
            "id": post_id,
            "poster": text_map.get(post["AGPIJOGPGEG"]),
            "title": text_map.get(post["GGCPHHGDFGB"]),
            "text": text_map.get(post["OJCGCLOKPDI"]),
            "script": text_map.get(post["GPGNJEOPEDC"]),
            "comments": [],
            "player_reply": [text_map.get(v) for k, v in post.items() if "Reply" in str(v)],
        }

    # load comments
    data = load_json(os.path.join(args.repo, "FileCfg/PostCommentConfigTemplateTb.json"))
    for comment in data["GMNCBMLIHPE"]:
        post_id = comment["ENBGFBIDAFJ"].split("_")[-1]
        if post_id not in post_mapping:
            continue
        post_mapping[post_id]["comments"].append({
            "role": text_map.get(comment["ENBGFBIDAFJ"]),
            "content": text_map.get(comment["EHCEBAMJGJP"]),
        })

    with open(f"data/interknot_post_comment_{args.lang}.jsonl", "w", encoding="utf-8") as f:
        for post_id, post in post_mapping.items():
            print(json.dumps(post, ensure_ascii=False), file=f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo",
        default="../ZenlessData",
        type=str,
        help="data dir",
    )
    parser.add_argument("--lang", default="", type=str, help="language type")
    args = parser.parse_args()

    # load text_map
    string = f"_{args.lang}" if args.lang else ""
    text_map = load_json(os.path.join(args.repo, f"TextMap/TextMap{string}TemplateTb.json"))

    parse(args, text_map)