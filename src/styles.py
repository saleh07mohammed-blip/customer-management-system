# styles.py - تصاميم النظام
class Colors:
    # الألوان الرئيسية
    PRIMARY = "#2E86AB"      # أزرق محترف
    SECONDARY = "#A23B72"    # بنفسجي
    SUCCESS = "#18A558"      # أخضر
    WARNING = "#F18F01"      # برتقالي
    DANGER = "#C73E1D"       # أحمر
    LIGHT = "#F8F9FA"        # فاتح
    DARK = "#212529"         # غامق
    
    # خلفيات
    BG_LIGHT = "#F5F7FA"
    BG_WHITE = "#FFFFFF"
    
    # جداول
    TABLE_HEADER = "#2E86AB"
    TABLE_ODD = "#FFFFFF"
    TABLE_EVEN = "#F8F9FA"
    TABLE_HOVER = "#E3F2FD"

class Fonts:
    # الخطوط
    TITLE = ("Arial", 16, "bold")
    HEADER = ("Arial", 12, "bold")
    NORMAL = ("Arial", 10)
    SMALL = ("Arial", 9)

class Styles:
    # أنماط الأزرار
    BTN_PRIMARY = {
        'bg': Colors.PRIMARY,
        'fg': 'white',
        'font': Fonts.NORMAL,
        'relief': 'flat',
        'bd': 0,
        'padx': 15,
        'pady': 8
    }
    
    BTN_SUCCESS = {
        'bg': Colors.SUCCESS,
        'fg': 'white',
        'font': Fonts.NORMAL,
        'relief': 'flat',
        'bd': 0,
        'padx': 15,
        'pady': 8
    }
    
    # أنماط الحقول
    ENTRY_STYLE = {
        'font': Fonts.NORMAL,
        'relief': 'solid',
        'bd': 1,
        'bg': Colors.BG_WHITE
    }
    
    # أنماط العناوين
    LABEL_HEADER = {
        'font': Fonts.HEADER,
        'bg': Colors.BG_LIGHT,
        'fg': Colors.DARK
    }
