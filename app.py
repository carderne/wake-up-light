#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
from crontab import CronTab

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/update", methods=["POST"])
def update():
    values = request.get_json()
    days = values.get("days")
    time = values.get("time")
    duration = values.get("duration")

    hour, minute = time.split(":")

    cron = CronTab(user="root")
    cron.remove_all(comment="wake")
    if days != "off":
        job = cron.new(command=f"/home/pi/app/wake.py {duration}", comment="wake")
        job.minute.on(minute)
        job.hour.on(hour)
        if days == "all":
            job.dow.every(1)
        else:
            job.dow.on(1,2,3,4,5)
    cron.write()

    return jsonify("Done!")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
