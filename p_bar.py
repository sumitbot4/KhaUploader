import math
import time

def progress_bar(current, total, start, message):
    now = time.time()
    diff = now - start
    if diff == 0:
        diff = 1e-6  # avoid divide by zero

    percent = current * 100 / total
    speed = current / diff
    elapsed_time = round(diff)
    eta = round((total - current) / speed) if speed > 0 else 0

    bar_length = 20
    filled_length = int(bar_length * current // total)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)

    text = f"{message}\n[{bar}] {percent:.2f}%\n" \
           f"Done: {humanbytes(current)} of {humanbytes(total)}\n" \
           f"Speed: {humanbytes(speed)}/s\n" \
           f"ETA: {time_formatter(eta)}"
    return text

def humanbytes(size):
    # convert bytes to human readable format
    if not size:
        return "0B"
    power = 2**10
    n = 0
    Dic_powerN = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {Dic_powerN[n]}"

def time_formatter(seconds: int) -> str:
    result = ""
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    if days:
        result += f"{days}d "
    if hours:
        result += f"{hours}h "
    if minutes:
        result += f"{minutes}m "
    if seconds:
        result += f"{seconds}s"
    return result.strip()
