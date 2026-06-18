# Network Inventory- Ping Sweep

**Tools:** Python 3 (standard library only)

**Environment:** Daily driver- Fedora Linux, Niri compositor

**Part of:** Security Tooling Portfolio- built alongside CompTIA Network+ study

---

## What this is

Before you can monitor or secure a network, you need an accurate picture of what's actually connected to it- and "what's on the network" is a surprisingly easy thing to get wrong if you're relying on memory or an outdated spreadsheet. This script sweeps an entire subnet, pings every address in range, and writes the results out to a CSV so there's an actual record of what was up and when. The kind of basic asset inventory that underpins a lot of real security monitoring.

---

## What it does

The script loops through every address from `192.168.1.1` to `192.168.1.254`, sends a single ping to each, and records whether it responded. It includes logic to detect whether it's running on Linux or Windows and adjust the ping flags accordingly (though in practice every run so far has been on my daily driver). Once the sweep finishes, it writes everything to `network_inventory.csv` with three columns: IP address, status, and timestamp.

```text
Starting ping sweep...
----------------------------------------
192.168.1.1 : Down
192.168.1.2 : Down
...
192.168.1.254 : Up
----------------------------------------
Sweep complete. Results saved to network_inventory.csv
```

Most addresses on a typical home or lab network will show as 'Down', that's completely normal, only active devices respond. The CSV only gets written once the full sweep has finished, so a partial run won't leave a half-complete file behind.

```bash
ip a  # confirm your subnet first
/usr/bin/python "/path/to/pingSweep.py"
```

To scan a different subnet, update the `base_ip` variable directly in the script (e.g. `base_ip = "192.168.1"`).

---

## How I built it

The core of this script is genuinely simple, a loop and a ping call,  but the part that took actual thought was handling permission and timeout issues cleanly rather than letting the script crash partway through a 254-address sweep. I also built in OS detection up front so the ping command itself adjusts depending on platform (Windows and Linux specify count and timeout differently). It's the kind of thing that's far easier to write in from the start than to bolt on later if I ever need to run this somewhere else.

No external libraries were needed; `subprocess` to actually run the ping command and `csv` to write the output cover the entire tool.

---

## What I took from this

This is a small script, but it's the kind of small script that's actually useful. Asset inventory is unglamorous compared to recon or exploitation work, but you can't detect an unauthorised device on a network if you don't already know what's supposed to be there in the first place. The bigger habit this reinforced was building for portability before I actually needed it, rather than assuming the environment I'm developing in is the only one this will ever run in.

---

## Files in this repo

| File | What it is |
|------|-----------|
| `pingSweep.py` | Main script — runs the sweep and writes results |
| `network_inventory.csv` | Output file — full results with status and timestamps |
| `screenshots/` | Script running, sweep in progress |
