import argparse
import json
import os.path

from util import load_json


def parse(args, text_map: dict):
    # load interknot post
    data = load_json(os.path.join(args.repo, "FileCfg/PartnerConfigTemplateTb.json"))
    partners = []
    for partner in data["GMNCBMLIHPE"]:
        partner_dict = {v: text_map.get(v) for v in partner.values() if isinstance(v, str) and "_" in v}
        partner_dict["nickname"] = partner["AKEMNEKJMKD"]
        partners.append(partner_dict)

    with open(f"data/partner_{args.lang}.jsonl", "w", encoding="utf-8") as f:
        for partner in partners:
            print(json.dumps(partner, ensure_ascii=False), file=f)


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