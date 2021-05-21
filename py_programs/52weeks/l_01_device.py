from pprint import pprint

device = {
  "name": "sbx-n9kv-ao",
  "vendor": "cisco",
  "model": "Nexus9000 C9300v Chassis",
  "os": "nxos",
  "version": "9.3(3)",
  "ip": "10.1.1.1",
  "1": "any data goes here",
}
#SIMPLE PRINT
print("\n_______SIMPLE  PRINT_______")
print("device:", device)
print("device name:", device["name"])

#PRETTY PRINT
print("\n_____PRETTY PRINT________")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT
print("\n_____FOR LOOP, USING F-STRING")
for key, value in device.items():
    print (f"{key:>16s} : {value}")

