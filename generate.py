import requests

url = "https://raw.githubusercontent.com/ipverse/rir-ip/master/country/ru/ipv4-aggregated.txt"

data = requests.get(url, timeout=30).text.splitlines()

with open("ru.rsc", "w") as f:
    f.write("/ip firewall address-list remove [find list=ru]\n")

    for net in data:
        net = net.strip()

        if not net or net.startswith("#"):
            continue

        f.write(
            f'/ip firewall address-list add list=ru address={net}\n'
        )
