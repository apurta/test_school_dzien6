device_names = {1: "cpu0", 2: "mem_b.nk0", 3: "mem_bank1"}
device_models = {1 : "Xenon", 2 : "Corsair", 3: "Corsair"}

# tak to ma wyglądać:
# [{id : 1, name: blavbl, model: blabla}
#  {id: 2, name: blavbl, model: blabla}]

#rozwiązanie polecenia 1

devices = []
for dev_id, name in device_names.items():
    model = device_models[dev_id]
    devices.append({"id": dev_id, "name": name, "model": model})

print(devices)

print()
print()

# rozwiazanie polecenia 2
# {"Xenon: [cpu], "Corsiar": [mem_bako0, mem_bank1]}

# moje :/
name_by_model = {}

for record in device_models:
    name = device_names[dev_id]
    model = device_models[dev_id]
    if record[model] in device_models:
        name_by_model[record[model]].append(record[name])
    else:
        name_by_model[record[model]] = [record[name]]

print(name_by_model)

# rozw własciwe:
model_map = {}

for dev_id, model in device_models.items():
    if model in model_map:
        model_map[model].append(device_names[dev_id])
    else:
        model_map[model] = [device_names[dev_id]]
print(model_map)