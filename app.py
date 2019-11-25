#!/usr/bin/env python3

import os
import json

from flask import Flask, render_template, request, jsonify
from crontab import CronTab

app = Flask(__name__)


config_file = "config.json"


@app.route("/")
def index():
    with open(config_file, "r") as f:
        config = json.load(f)
    days = config["days"]
    time = config["time"]
    duration = config["duration"]
    return render_template("index.html", days=days, time=time, duration=duration)


@app.route("/api/update", methods=["POST"])
def update():
    print("Updating")
    values = request.get_json()
    days = values.get("days")
    time = values.get("time")
    duration = values.get("duration")

    with open(config_file, "w") as f:
        json.dump({"days": days, "time": time, "duration": duration}, fp=f)

    hour, minute = time.split(":")

    cron = CronTab(user="root")
    cron.remove_all(comment="wake")
    if days != "off":
        job = cron.new(
            command=f"/home/pi/wake-up-light/lights.py sunrise {duration}",
            comment="wake",
        )
        job.minute.on(minute)
        job.hour.on(hour)
        if days == "all":
            job.dow.every(1)
        else:
            job.dow.on(1, 2, 3, 4, 5)
    cron.write()

    return jsonify("Updated")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
