
def main():

    import json
    import os

    folder = os.path.dirname(__file__)

    COMMAND = 'item replace entity @s weapon.offhand with written_book{author:"Naratna", title:"Commands", pages:%s} 1'
    with open(os.path.join(folder,"pages.json")) as pages:
        pages_json = json.load(pages)

    for obj in pages_json:
        if "extra" not in obj:
            break
        for line in obj["extra"]:
            try:
                contents = line["clickEvent"]["value"]
                action = "show_text"
                if "[Clear]" in line["text"]:
                    contents = "/clear"
                elif "/give" in contents:
                    action = "show_item"
                    contents = contents.split(" ")[2]
                line["hoverEvent"] = {
                    "action":action,
                    "contents": contents
                }
            except KeyError:
                pass

    pages_json = [json.dumps(obj) for obj in pages_json]
    
    with open(os.path.join(folder,"give.mcfunction"), "w") as give:
        give.write(COMMAND % pages_json)

if __name__ == "__main__":
    main()