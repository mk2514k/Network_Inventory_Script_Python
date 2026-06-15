# Network Inventory- Ping Sweep

A Python script that sweeps a subnet by pinging every host in a given IP range, records whether each one is up or down, and exports the results to a CSV file.

---

## What the Script Does

The script loops through every address from `192.168.1.1` to `192.168.1.254`, sends a single ping to each one, and records the result. Once the sweep is complete it writes everything to `network_inventory.csv` with three columns — IP address, status, and timestamp.

It automatically detects whether you're on Linux or Windows and uses the correct ping flags for each.

---

## What to Expect

The terminal prints each IP as it's checked in real time:

```
Starting ping sweep...
----------------------------------------
192.168.1.1 — Down
192.168.1.2 — Down
...
192.168.1.254 — Up
----------------------------------------
Sweep complete. Results saved to network_inventory.csv
```

The sweep runs through all 254 addresses one by one — most will show as Down on a typical home network, which is completely normal. Only active devices on your subnet will show as Up.

The CSV is only created once the full sweep has finished.

---

## How to Run It

No additional installs needed — the script uses Python built-in libraries only.

Before running, check your machine's IP address and make sure `base_ip` in the script matches your subnet:

```bash
ip a
```

Then run:

```bash
/usr/bin/python "/path/to/pingSweep.py"
```

To change the subnet being scanned, update this line in the script:

```python
base_ip = "192.168.1"  # change to match your network
```

---

## Files

| File | Description |
|---|---|
| `pingSweep.py` | Main script — runs the ping sweep and writes results |
| `network_inventory.csv` | Output file — full results of the sweep with status and timestamps |
| `screenshots/` | script_running01, script_running02 |
