# styles.py - تصاميم النظام
class Colors:
    PRIMARY = "#2E86AB"
    SECONDARY = "#A23B72"
    SUCCESS = "#18A558"
    WARNING = "#F18F01"
    DANGER = "#C73E1D"
    LIGHT = "#F8F9FA"
    DARK = "#212529"
    BG_LIGHT = "#F5F7FA"
    BG_WHITE = "#FFFFFF"
    TABLE_HEADER = "#2E86AB"
    TABLE_ODD = "#FFFFFF"
    TABLE_EVEN = "#F8F9FA"
    TABLE_HOVER = "#E3F2FD"

class Fonts:
    TITLE = ("Arial", 16, "bold")
    HEADER = ("Arial", 12, "bold")
    NORMAL = ("Arial", 10)
    SMALL = ("Arial", 9)

class Styles:
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
    
    # إصلاح: إزالة 'font' من ENTRY_STYLE
    ENTRY_STYLE = {
        'bg': Colors.BG_WHITE
    }
    
    LABEL_HEADER = {
        'font': Fonts.HEADER,
        'bg': Colors.BG_LIGHT,
        'fg': Colors.DARK
    }
