import datetime
import jdatetime
from hijridate import Hijri

PERSIAN_WEEKDAYS = {
    0: "دوشنبه",
    1: "سه‌شنبه",
    2: "چهارشنبه",
    3: "پنج‌شنبه",
    4: "جمعه",
    5: "شنبه",
    6: "یکشنبه"
}

PERSIAN_MONTHS = [
    "فروردین", "اردیبهشت", "خرداد",
    "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر",
    "دی", "بهمن", "اسفند"
]

HIJRI_MONTHS = [
    "محرم", "صفر", "ربیع‌الاول", "ربیع‌الثانی",
    "جمادی‌الاول", "جمادی‌الثانی", "رجب", "شعبان",
    "رمضان", "شوال", "ذی‌القعده", "ذی‌الحجه"
]

GREGORIAN_MONTHS = [
    "ژانویه", "فوریه", "مارس", "آوریل", "مه", "ژوئن",
    "ژوئیه", "اوت", "سپتامبر", "اکتبر", "نوامبر", "دسامبر"
]

def get_today_dates():
    # Gregorian
    today_gregorian = datetime.date.today()
    g_day = today_gregorian.day
    g_month_name = GREGORIAN_MONTHS[today_gregorian.month - 1]
    g_year = today_gregorian.year
    g_weekday = today_gregorian.weekday()
    gregorian_str = f"{g_day} {g_month_name} {g_year}"
    
    # Jalali (Persian)
    today_jalali = jdatetime.date.fromgregorian(date=today_gregorian)
    j_day = today_jalali.day
    j_month_name = PERSIAN_MONTHS[today_jalali.month - 1]
    j_year = today_jalali.year
    persian_weekday_name = PERSIAN_WEEKDAYS[g_weekday]
    jalali_str = f"{persian_weekday_name} {j_day} {j_month_name} {j_year}"
    
    # Hijri
    try:
        today_hijri = Hijri.today()
        h_day = today_hijri.day
        h_month_name = HIJRI_MONTHS[today_hijri.month - 1]
        h_year = today_hijri.year
        hijri_str = f"{h_day} {h_month_name} {h_year}"
    except Exception:
        # Fallback if Hijri conversion fails
        hijri_str = ""
        
    return {
        "jalali": jalali_str,
        "gregorian": gregorian_str,
        "hijri": hijri_str,
        "month_day_jalali": f"{today_jalali.month}-{today_jalali.day}",
        "jalali_year": j_year,
        "jalali_month": today_jalali.month,
        "jalali_day": j_day
    }

def replace_numbers_with_persian(text: str) -> str:
    persian_numbers = "۰۱۲۳۴۵۶۷۸۹"
    english_numbers = "0123456789"
    translation_table = str.maketrans(english_numbers, persian_numbers)
    return text.translate(translation_table)
