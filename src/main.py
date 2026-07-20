from src.dates import get_today_dates
from src.occasions import get_today_occasions
from src.poems import get_random_poem
from src.greetings import get_random_greeting
from src.images import get_random_image
from src.weather import get_aliabad_weather
from src.prayer_times import get_aliabad_prayer_times
from src.formatter import format_daily_message
from src.config import CHANNEL_ID
from src.telegram_sender import send_message, send_photo

def main():
    print("شروع اجرای ربات صبحانه...")
    
    # 1. Get dates
    dates = get_today_dates()
    
    # 2. Get occasions for today (Jalali month-day)
    occasions = get_today_occasions(dates["month_day_jalali"])
    
    # 3. Get poem (Ganjoor API)
    poem = get_random_poem()
    
    # 4. Get greeting
    greeting = get_random_greeting()
    
    # 5. Get weather (wttr.in API)
    weather = get_aliabad_weather()
    
    # 6. Get prayer times (Aladhan API)
    prayer_times = get_aliabad_prayer_times()
    
    # 7. Format message
    message = format_daily_message(dates, occasions, poem, greeting, weather, prayer_times)
    print("متن پیام آماده شد:")
    print(message)
    print("-" * 30)
    
    # 8. Get image (Picsum API)
    image_path = get_random_image()
    
    # 9. Send to Telegram
    try:
        if image_path:
            print(f"در حال ارسال عکس ({image_path}) با کپشن...")
            send_photo(CHANNEL_ID, image_path, message)
        else:
            print("عکسی یافت نشد، در حال ارسال متن خالی...")
            send_message(CHANNEL_ID, message)
            
        print("✅ پیام با موفقیت ارسال شد.")
    except Exception as e:
        print(f"❌ خطا در ارسال پیام: {e}")

if __name__ == "__main__":
    main()
