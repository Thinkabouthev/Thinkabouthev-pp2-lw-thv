import json

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

with open("database.json") as f:
    main_data = json.load(f)
    # print(heading)
    for i in main_data["imdata"]:
        print(
            f'{i["l1PhysIf"]["attributes"]["dn"]:<73}{i["l1PhysIf"]["attributes"]["descr"]}{i["l1PhysIf"]["attributes"]["speed"]:<9}{i["l1PhysIf"]["attributes"]["mtu"]}'
        )