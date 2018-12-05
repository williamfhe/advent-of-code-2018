from datetime import datetime
from typing import NamedTuple
from collections import defaultdict
from enum import Enum


class Status(Enum):
    NEW_SHIFT = 0
    WAKE_UP = 1
    SLEEP = 2


class Record(NamedTuple):
    date: datetime
    guard_id: int
    status: int
    raw: str

    def __str__(self):
        return f'{self.date} {self.guard_id} {self.status}, {self.raw}'


def parse_record(record_str: str) -> Record:
    date = datetime.strptime(record_str[:18], '[%Y-%m-%d %H:%M]')
    infos = record_str[19:].split()
    awake = False
    guard_id = -1
    if infos[0] == 'wakes':
        awake = Status.WAKE_UP
    elif infos[0] == 'Guard':
        awake = Status.NEW_SHIFT
        guard_id = int(infos[1][1:])
    else:
        awake = Status.SLEEP

    return Record(date, guard_id, awake, infos)

with open('input.txt') as f:
    records = [parse_record(line) for line in f.readlines()]

# order the records by date

records = sorted(records, key=lambda record: record.date)

sleep_map = defaultdict(lambda: defaultdict(int))

last_start_minute = records[0].date.minute if records[0].date.hour != 23 else 0
last_guard_id = records[0].guard_id
max_sleep_guard_id = last_guard_id
max_sleep_minute = 0


for record in records[1:]:
    if record.status == Status.NEW_SHIFT:
        guard_stats = sleep_map[last_guard_id]
        last_start_minute = record.date.minute if record.date.hour != 23 else 0

        last_guard_id = record.guard_id

    elif record.status == Status.SLEEP:
        last_start_minute = record.date.minute
    else:
        sleep_time = record.date.minute - last_start_minute
        for i in range(sleep_time):
            current_minute = i + last_start_minute
            sleep_map[current_minute][last_guard_id] += 1

            if sleep_map[current_minute][last_guard_id] > sleep_map[max_sleep_minute][max_sleep_guard_id]:
                max_sleep_minute = current_minute
                max_sleep_guard_id = last_guard_id


print(max_sleep_guard_id * max_sleep_minute)