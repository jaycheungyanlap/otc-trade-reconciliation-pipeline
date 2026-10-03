# config.py 增強版

INTERNAL_FILE = 'internal_trades.xlsx'
BROKER_FILE = 'broker_feed.csv'
OUTPUT_REPORT = 'Daily_Break_Report.xlsx'

TOLERANCE_THRESHOLD = 1.0

COLOR_HEADER = '1F4E78'
COLOR_RED = 'FFC7CE'
COLOR_YELLOW = 'FFEB9C'
COLOR_ORANGE = 'FCE4D6'

# 郵件通知設定 (SMTP Config)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'jaycheung90@gmail.com'
SENDER_PASSWORD = 'your_app_password'  # 應用程式密碼
RECIPIENTS = ['cheungyanlap@icloud.com']

# 大額 Break 警報閥值 ($500,000)
LARGE_BREAK_THRESHOLD = 500000.0