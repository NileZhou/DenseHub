import requests
import base64
import hashlib
import hmac
import time
import urllib.parse
import shutil  # For disk usage
import os  # For inode usage
import schedule  # For scheduling tasks
import random  # For Trump messages

# --- Configuration ---
MONITORED_PATH = "要监控的目录"
SPACE_THRESHOLD_TB = 1.0  # Alert if available space is less than this value in TB
INODE_THRESHOLD_PERCENT = 90.0  # Alert if inode usage is above this percentage
DINGTALK_SECRET = "..."  # IMPORTANT: Replace with your actual DingTalk robot secret if signing is enabled
DINGTALK_ACCESS_TOKEN = "..."
AT_USER_IDS = ["要@的人的dingtalk id"]  # User IDs to @ in DingTalk messages
ALERT_COOLDOWN_MINUTES = 10 # Cooldown period for sending alerts in minutes
# --- End Configuration ---

# --- Global State for Alert Cooldown ---
LAST_ALERT_TIMESTAMP = 0
# --- End Global State ---


def get_dingtalk_signed_url_params():
    """
    Generates timestamp and sign for DingTalk robot URL using global configurations.
    """
    timestamp = str(round(time.time() * 1000))

    # If no secret is provided or it's the placeholder, skip signing.
    # This is for robots that do not have "加签" (signing) enabled.
    if not DINGTALK_SECRET:
        # print(
        #     "Warning: DINGTALK_SECRET is not set or is a placeholder. "
        #     "Proceeding without message signing. "
        #     "This may fail if your robot requires a signature."
        # )
        return DINGTALK_ACCESS_TOKEN, timestamp, None

    secret_enc = DINGTALK_SECRET.encode("utf-8")
    string_to_sign = "{}\n{}".format(timestamp, DINGTALK_SECRET)
    string_to_sign_enc = string_to_sign.encode("utf-8")
    hmac_code = hmac.new(
        secret_enc, string_to_sign_enc, digestmod=hashlib.sha256
    ).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return DINGTALK_ACCESS_TOKEN, timestamp, sign


def send_dingtalk_message(message_text: str, title: str = "System Alert"):
    """
    Sends a markdown message to the DingTalk robot.
    """
    access_token, timestamp, sign = get_dingtalk_signed_url_params()

    url = f"https://oapi.dingtalk.com/robot/send?access_token={access_token}&timestamp={timestamp}"
    if sign:
        url += f"&sign={sign}"

    at_mentions_text = ""
    if AT_USER_IDS:
        at_mentions_text = " " + " ".join([f"@{user_id}" for user_id in AT_USER_IDS])

    payload = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": message_text + at_mentions_text,
        },
        "at": {
            "atUserIds": AT_USER_IDS if AT_USER_IDS else [],
            "isAtAll": False,
        },
    }
    try:
        response = requests.post(url, json=payload, timeout=15)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        print(
            f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] DingTalk message sent successfully. Response: {response.json()}"
        )
        return response.json()
    except requests.exceptions.Timeout:
        print(
            f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error sending DingTalk message: Request timed out."
        )
    except requests.exceptions.HTTPError as http_err:
        print(
            f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error sending DingTalk message: HTTP error occurred: {http_err} - {response.text}"
        )
    except requests.exceptions.RequestException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error sending DingTalk message: {e}")
    return None


def get_disk_available_tb(path: str) -> float:
    """
    Returns the available disk space in Terabytes (TiB) for the given path.
    1 TiB = 1024^4 bytes.
    Returns -1.0 if an error occurs (e.g., path not found).
    """
    try:
        total, used, free = shutil.disk_usage(path)
        # Convert free space from bytes to Terabytes (TiB)
        free_tb = free / (1024**4)
        return free_tb
    except FileNotFoundError:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: Path '{path}' not found for disk usage check.")
        return -1.0  # Indicate error
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error getting disk usage for '{path}': {e}")
        return -1.0 # Indicate error


def get_inode_usage_percent(path: str) -> float:
    """
    Returns the inode usage percentage for the given path.
    Returns -1.0 if an error occurs (e.g., path not found).
    """
    try:
        statvfs = os.statvfs(path)
        total_inodes = statvfs.f_files
        free_inodes = statvfs.f_ffree
        used_inodes = total_inodes - free_inodes
        
        if total_inodes == 0:
            return -1.0  # Avoid division by zero
            
        usage_percent = (used_inodes / total_inodes) * 100
        return usage_percent
    except FileNotFoundError:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: Path '{path}' not found for inode usage check.")
        return -1.0  # Indicate error
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error getting inode usage for '{path}': {e}")
        return -1.0 # Indicate error


def create_trump_alert_message(available_tb: float, path: str, inode_usage_percent: float = None) -> str:
    """
    Creates a funny, Trump-like alert message about low disk space and/or high inode usage (in English).
    """
    if inode_usage_percent is not None and inode_usage_percent >= INODE_THRESHOLD_PERCENT:
        # Both disk space and inode issues
        if available_tb < SPACE_THRESHOLD_TB:
            messages = [
                f"This is a TOTAL DISASTER for `{path}`! We've got TWO problems - BIG problems! Storage is down to **{available_tb:.2f}TB** AND inodes are at **{inode_usage_percent:.1f}%**! This is worse than fake news! We need to fix this IMMEDIATELY!",
                f"Believe me, nobody has ever seen problems like this before! `{path}` is running out of EVERYTHING - only **{available_tb:.2f}TB** space left AND **{inode_usage_percent:.1f}%** inodes used! This is a complete and total catastrophe! We're going to make storage great again!",
                f"BREAKING: `{path}` is facing a DOUBLE WHAMMY! Space: **{available_tb:.2f}TB** remaining, Inodes: **{inode_usage_percent:.1f}%** used! This is the worst storage crisis in the history of servers, maybe ever! We need to act NOW!",
            ]
        else:
            # Only inode issue
            messages = [
                f"Listen, we have a YUGE problem with `{path}`! The inodes are at **{inode_usage_percent:.1f}%**! Nobody told me inodes could be so complicated! This is a disaster of epic proportions! We need to clean up these files, big league!",
                f"Fake news won't report this, but our inodes at `{path}` are CRITICALLY HIGH at **{inode_usage_percent:.1f}%**! We have too many files, way too many! We're going to have the best file cleanup, tremendous cleanup!",
                f"This is frankly a disgrace! `{path}` inodes at **{inode_usage_percent:.1f}%**! We need to delete files, lots of files! Make our filesystem great again!",
            ]
    else:
        # Only disk space issue (original messages)
        messages = [
            f"Listen, we've got a problem with `{path}`, a BIG problem! Our storage, the BEST storage, is down to **{available_tb:.2f}TB**. This is a DISASTER! We need more space, and we need it NOW! Sad!",
            f"Fake news media won't report this, but our server space at `{path}` is running LOW, very low, only **{available_tb:.2f}TB** left! We build the best systems, the most tremendous systems, and they're filling up. We need to make our storage GREAT again!",
            f"Believe me, nobody knew storage for `{path}` could be so complicated. But we're running out! Only **{available_tb:.2f}TB** left. We have the best data, the most important data, and it needs more room. We're going to fix this, big league.",
            f"This is frankly, and I say this with great respect for storage, a disgrace for `{path}`. **{available_tb:.2f}TB** remaining? Unacceptable! We are going to build a beautiful, new, YUGE amount of storage, and the data will pay for it (somehow)!",
            f"They said it couldn't happen for `{path}`. They said our storage was infinite. WRONG! We're at **{available_tb:.2f}TB**. We need to act strongly. Very strongly. Get more storage, make America great again... I mean, make the server great again!",
        ]
    return random.choice(messages)


def check_disk_and_alert():
    """
    Checks disk space and inode usage for MONITORED_PATH and sends an alert if below/above thresholds,
    respecting the cooldown period.
    """
    global LAST_ALERT_TIMESTAMP
    current_time_seconds = time.time()
    current_time_str = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{current_time_str}] Checking disk space and inode usage for {MONITORED_PATH}...")
    
    available_tb = get_disk_available_tb(MONITORED_PATH)
    inode_usage_percent = get_inode_usage_percent(MONITORED_PATH)

    # Check for errors
    if available_tb < 0 or inode_usage_percent < 0:
        error_message = (
            f"🚨 **America Dream is Dying** 🚨\n\n"
            f"Could not check disk space or inode usage for `{MONITORED_PATH}`. "
            f"The path might be missing or inaccessible. Please investigate immediately!"
        )
        print(f"[{current_time_str}] {error_message}")
        # Send error messages immediately, bypassing cooldown for critical errors
        send_dingtalk_message(error_message, title="🚨 Storage Check Failed!")
        return

    print(f"[{current_time_str}] Available space at {MONITORED_PATH}: {available_tb:.2f} TB")
    print(f"[{current_time_str}] Inode usage at {MONITORED_PATH}: {inode_usage_percent:.1f}%")

    # Check thresholds
    space_alert = available_tb < SPACE_THRESHOLD_TB
    inode_alert = inode_usage_percent >= INODE_THRESHOLD_PERCENT
    
    if space_alert or inode_alert:
        alert_title = "📢 Storage Alert! BIG LEAGUE PROBLEMS!"
        alert_reasons = []
        
        if space_alert:
            alert_reasons.append(f"low disk space ({available_tb:.2f}TB < {SPACE_THRESHOLD_TB}TB)")
        if inode_alert:
            alert_reasons.append(f"high inode usage ({inode_usage_percent:.1f}% >= {INODE_THRESHOLD_PERCENT}%)")
            
        alert_reason_text = " and ".join(alert_reasons)
        print(f"[{current_time_str}] ALERT! {alert_reason_text} at {MONITORED_PATH}.")

        # Check cooldown
        if (current_time_seconds - LAST_ALERT_TIMESTAMP) >= (ALERT_COOLDOWN_MINUTES * 60):
            alert_message = create_trump_alert_message(available_tb, MONITORED_PATH, inode_usage_percent if inode_alert else None)
            send_dingtalk_message(alert_message, title=alert_title)
            LAST_ALERT_TIMESTAMP = current_time_seconds
            print(f"[{current_time_str}] Alert sent. Next alert possible after {ALERT_COOLDOWN_MINUTES} minutes.")
        else:
            minutes_since_last_alert = (current_time_seconds - LAST_ALERT_TIMESTAMP) / 60
            remaining_cooldown = ALERT_COOLDOWN_MINUTES - minutes_since_last_alert
            print(
                f"[{current_time_str}] Alert condition met ({alert_reason_text}), but still in cooldown. "
                f"Last alert sent {minutes_since_last_alert:.1f} minutes ago. "
                f"Next alert possible in {remaining_cooldown:.1f} minutes."
            )
    else:
        print(
            f"[{current_time_str}] All good at {MONITORED_PATH} - Space: {available_tb:.2f}TB, Inodes: {inode_usage_percent:.1f}%. No alert needed."
        )


if __name__ == "__main__":
    # 使用方法: 在宿主机上执行:
    # nohup python3 /njfs/train-aitech/toolbox/trump_watch/trump_watch.py > /njfs/train-aitech/toolbox/trump_watch/trump_watch.log 2>&1 &
    print(f"--- TrumpWatch Storage Monitor Initializing ---")
    print(f"Monitoring path: {MONITORED_PATH}")
    print(f"Disk space alert threshold: < {SPACE_THRESHOLD_TB} TB available")
    print(f"Inode usage alert threshold: >= {INODE_THRESHOLD_PERCENT}% used")
    print(f"Alert cooldown: {ALERT_COOLDOWN_MINUTES} minutes between alerts")
    print(f"DingTalk Robot Access Token: ...{DINGTALK_ACCESS_TOKEN[-6:]}") # Show last 6 chars for confirmation
    if not DINGTALK_SECRET or DINGTALK_SECRET == "暂时没有":
        print("WARNING: DingTalk secret (DINGTALK_SECRET) is not configured or is a placeholder. Signing will be skipped.")
        print("         If your robot requires signing, alerts WILL FAIL. Please configure the secret.")
    else:
        print(f"DingTalk Robot Secret: Configured (using HMAC-SHA256 for signing)")
    print(f"Mentioning User IDs: {', '.join(AT_USER_IDS) if AT_USER_IDS else 'No user configured to @'}")
    print(f"Scheduling checks every 1 minute.")
    print("--- Starting initial check now ---")

    check_disk_and_alert()  # Run once immediately on start

    schedule.every(1).minutes.do(check_disk_and_alert)
    # For testing purposes, you might want to run it more frequently:
    # schedule.every(10).seconds.do(check_disk_and_alert)

    print("--- Monitoring started. Press Ctrl+C to stop. ---")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n--- TrumpWatch Storage Monitor shutting down. ---")