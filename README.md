# Persian Morning Telegram Bot (ربات صبحانه تلگرام)

A robust, fully automated Python-based Telegram bot that sends a daily morning message to your channel using GitHub Actions. It runs completely free of charge, requires no continuous server, and leverages multiple public APIs to generate rich, dynamic content every morning.

## 🌟 Features

Every morning, the bot automatically sends a beautiful, structured message containing:
- 🌅 **Greeting**: A warm, welcoming daily greeting.
- 📅 **Dates**: The current day in Jalali (Persian), Gregorian, and Hijri calendars.
- 🎉 **Occasions**: Iranian and global occasions for the day.
- 🌤 **Weather**: Live weather updates for Aliabad-e-Katul (using wttr.in API).
- 🕋 **Prayer Times**: Daily prayer times for Aliabad-e-Katul (using Aladhan API).
- 📜 **Poem of the Day**: A random Persian poem fetched live from the Ganjoor API.
- 📸 **Beautiful Image**: A high-quality random image dynamically downloaded from Picsum.
- 📢 **Channel Signature**: Your custom channel name and link at the bottom.

## 🏗 Architecture

This project is specifically designed to run as a **serverless cron job via GitHub Actions**.
- **No Hosting Required**: It executes once a day via `.github/workflows/morning.yml` and shuts down immediately.
- **Resilient Content**: Uses live APIs for fresh content (Poems, Weather, Images, Prayer Times), while securely falling back to local JSON data (`data/` directory) if any API experiences downtime.
- **Decoupled Modules**: Each feature (weather, image fetching, dates, telegram sender) is isolated in its own file under `src/` for easy customization.

## 🚀 Setup & Deployment

1. **Clone/Fork the Repository**: Create your own copy of this repository.
2. **Add Telegram Bot Settings**: 
   Go to your GitHub Repository -> **Settings** -> **Secrets and variables** -> **Actions** and add the following repository secrets:
   - `BOT_TOKEN`: Your Telegram Bot API Token (from @BotFather).
   - `CHANNEL_ID`: Your channel username (e.g., `@my_morning_channel`) or numeric ID.
   - `CHANNEL_NAME`: The display name of your channel for the footer.
   - `CHANNEL_LINK`: The invite link for your channel.
3. **Add the Bot to your Channel**: Ensure your bot is added to your Telegram channel as an Administrator with permissions to *Post Messages*.
4. **Enable Actions**: In your GitHub repository, go to the **Actions** tab and enable workflows.

## ⏰ Schedule

By default, the GitHub Action is configured to run daily at `03:30 UTC` (which corresponds to `07:00 AM` Tehran time).
You can change this schedule by modifying the cron expression in `.github/workflows/morning.yml`:
```yaml
on:
  schedule:
    - cron: '30 3 * * *'
```

## 🛠 Local Development

If you want to test the bot locally before deploying:

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory:
   ```env
   BOT_TOKEN=123456789:YOUR_BOT_TOKEN
   CHANNEL_ID=@your_channel_username
   CHANNEL_NAME=صبحانه ایرانی
   CHANNEL_LINK=https://t.me/your_channel
   ```
4. Run the bot:
   ```bash
   export PYTHONPATH=.
   python src/main.py
   ```

## 📂 Project Structure

```text
├── .github/workflows/    # GitHub Actions workflow
├── data/                 # Local fallback datasets (JSON)
│   ├── images/           # Fallback images
│   └── ...               # occasions, greetings, poems
├── src/                  # Source code modules
│   ├── config.py         # Environment configuration
│   ├── dates.py          # Calendar conversions
│   ├── formatter.py      # Message text assembly
│   ├── images.py         # Live image downloading (Picsum)
│   ├── main.py           # Core orchestrator
│   ├── occasions.py      # Holiday & occasion data
│   ├── poems.py          # Ganjoor API fetching
│   ├── prayer_times.py   # Aladhan API fetching
│   ├── telegram_sender.py# Bot API communication
│   └── weather.py        # Wttr.in API fetching
└── requirements.txt      # Python dependencies
```
