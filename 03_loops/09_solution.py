items = ["fomgo","arms","carm","apple","apple"]

uniqe_item = set()

for item in items:
    if item in uniqe_item:
        print("duplicate",item)
        break
    uniqe_item.add(item)
print(uniqe_item)