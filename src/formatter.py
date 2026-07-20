from src.config import CHANNEL_NAME, CHANNEL_LINK
from src.dates import replace_numbers_with_persian

def format_daily_message(dates, occasions, poem, greeting, weather=None, prayer_times=None):
    """
    Combines all parts into the final Telegram HTML message.
    """
    msg_parts = []
    
    # 1. Greeting
    msg_parts.append(f"<b>{greeting}</b>\n")
    
    # 2. Dates
    msg_parts.append("📅 <b>تاریخ امروز:</b>")
    msg_parts.append(f"☀️ شمسی: {replace_numbers_with_persian(dates['jalali'])}")
    msg_parts.append(f"🌍 میلادی: {replace_numbers_with_persian(dates['gregorian'])}")
    msg_parts.append(f"🌙 قمری: {replace_numbers_with_persian(dates['hijri'])}\n")
    
    # 3. Occasions
    if occasions:
        msg_parts.append("🎉 <b>مناسبت‌های امروز:</b>")
        for occ in occasions:
            msg_parts.append(f"• {occ}")
        msg_parts.append("")
        
    # 4. Weather
    if weather:
        msg_parts.append("🌤 <b>وضعیت هوا:</b>")
        msg_parts.append(f"{replace_numbers_with_persian(weather)}\n")
        
    # 5. Prayer times
    if prayer_times:
        msg_parts.append("🕋 <b>اوقات شرعی (تهران):</b>")
        msg_parts.append(f"اذان صبح: {replace_numbers_with_persian(prayer_times['fajr'])}")
        msg_parts.append(f"طلوع آفتاب: {replace_numbers_with_persian(prayer_times['sunrise'])}")
        msg_parts.append(f"اذان ظهر: {replace_numbers_with_persian(prayer_times['dhuhr'])}")
        msg_parts.append(f"اذان مغرب: {replace_numbers_with_persian(prayer_times['maghrib'])}\n")

    # 6. Poem
    msg_parts.append("📜 <b>شعر روز:</b>")
    msg_parts.append(f"<i>{poem}</i>\n")
    
    # 7. Footer
    msg_parts.append("🌿")
    msg_parts.append(f"کانال: {CHANNEL_NAME}")
    msg_parts.append(f"🔗 {CHANNEL_LINK}")
    
    return "\n".join(msg_parts)
