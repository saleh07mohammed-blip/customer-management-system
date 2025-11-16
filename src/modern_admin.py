import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime, timedelta
from styles import Colors, Fonts, Styles

class ModernAdminPanel:
    def __init__(self):
        self.db_path = "customers.db"
        self.current_user = None
        self.setup_database()
        
        # إنشاء النافذة الرئيسية
        self.root = tk.Tk()
        self.root.title("نظام إدارة العملاء - الإصدار المحترف")
        self.root.geometry("1400x800")
        self.root.configure(bg=Colors.BG_LIGHT)
        
        # جعل النافذة في المنتصف
        self.center_window()
        
        self.show_login()
    
    def center_window(self):
        """جعل النافذة في منتصف الشاشة"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_database(self):
        """إعداد جداول قاعدة البيانات"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                city TEXT,
                district TEXT,
                phone TEXT,
                device_type TEXT,
                installation_date TEXT,
                next_maintenance TEXT,
                employee_id INTEGER,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def show_login(self):
        """واجهة تسجيل الدخول المحسنة"""
        self.login_frame = tk.Frame(self.root, bg=Colors.BG_LIGHT)
        self.login_frame.pack(expand=True, fill='both')
        
        # إطار البطاقة
        card_frame = tk.Frame(self.login_frame, bg=Colors.BG_WHITE, relief='raised', bd=2)
        card_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=350)
        
        # العنوان
        title_label = tk.Label(card_frame, text="تسجيل الدخول", 
                              font=Fonts.TITLE, bg=Colors.BG_WHITE, fg=Colors.PRIMARY)
        title_label.pack(pady=30)
        
        # حقل اسم المستخدم
        tk.Label(card_frame, text="اسم المستخدم", font=Fonts.NORMAL, 
                bg=Colors.BG_WHITE).pack(pady=(20, 5))
        
        self.username_entry = tk.Entry(card_frame, font=Fonts.NORMAL, width=25, 
                                      justify='center', **Styles.ENTRY_STYLE)
        self.username_entry.pack(pady=5)
        
        # حقل كلمة المرور
        tk.Label(card_frame, text="كلمة المرور", font=Fonts.NORMAL, 
                bg=Colors.BG_WHITE).pack(pady=(20, 5))
        
        self.password_entry = tk.Entry(card_frame, font=Fonts.NORMAL, width=25, 
                                      show="•", justify='center', **Styles.ENTRY_STYLE)
        self.password_entry.pack(pady=5)
        
        # زر الدخول
        login_btn = tk.Button(card_frame, text="دخول إلى النظام", 
                             command=self.handle_login, cursor='hand2', **Styles.BTN_PRIMARY)
        login_btn.pack(pady=30)
        
        # ربط الأزرار بالكيبورد
        self.root.bind('<Return>', lambda e: self.handle_login())
        self.username_entry.focus()
        
        # منع الكتابة بالعربي
        self.prevent_arabic(self.username_entry)
        self.prevent_arabic(self.password_entry)
    
    def prevent_arabic(self, entry_widget):
        """منع الكتابة بالعربي في الحقول"""
        def validate_input(char):
            # السماح فقط بالإنجليزية والأرقام
            return char.isascii() and not char.isalpha() or char.isalnum()
        
        entry_widget.config(validate="key", validatecommand=(entry_widget.register(validate_input), '%S'))
    
    def handle_login(self):
        """معالجة تسجيل الدخول"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and password == "admin123":
            self.current_user = username
            self.login_frame.destroy()
            self.show_main_panel()
        else:
            messagebox.showerror("خطأ", "بيانات الدخول غير صحيحة")
            self.password_entry.delete(0, tk.END)
            self.username_entry.focus()
    
    def show_main_panel(self):
        """الواجهة الرئيسية المحسنة"""
        self.root.title(f"نظام إدارة العملاء - المدير: {self.current_user}")
        
        # الشريط العلوي
        self.create_top_bar()
        
        # شريط الأدوات
        self.create_toolbar()
        
        # منطقة المحتوى
        self.create_content_area()
        
        # تحميل البيانات الأولية
        self.load_data()
    
    def create_top_bar(self):
        """الشريط العلوي"""
        top_bar = tk.Frame(self.root, bg=Colors.PRIMARY, height=60)
        top_bar.pack(fill='x', side='top')
        top_bar.pack_propagate(False)
        
        # العنوان
        title = tk.Label(top_bar, text="نظام إدارة عملاء الصيانة الدورية", 
                        font=Fonts.TITLE, bg=Colors.PRIMARY, fg='white')
        title.pack(side='right', padx=20, pady=15)
        
        # معلومات المستخدم
        user_info = tk.Label(top_bar, text=f"المدير: {self.current_user}", 
                           font=Fonts.NORMAL, bg=Colors.PRIMARY, fg='white')
        user_info.pack(side='left', padx=20, pady=15)
    
    def create_toolbar(self):
        """شريط أدوات البحث والتحكم"""
        toolbar = tk.Frame(self.root, bg=Colors.BG_LIGHT, height=80)
        toolbar.pack(fill='x', side='top', pady=10)
        toolbar.pack_propagate(False)
        
        # شريط البحث
        search_frame = tk.Frame(toolbar, bg=Colors.BG_LIGHT)
        search_frame.pack(side='right', padx=20, pady=10)
        
        tk.Label(search_frame, text="بحث سريع:", **Styles.LABEL_HEADER).pack(side='right', padx=5)
        
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, 
                               font=Fonts.NORMAL, width=30, **Styles.ENTRY_STYLE)
        search_entry.pack(side='right', padx=5)
        search_entry.bind('<KeyRelease>', self.on_search)
        
        # فلترة المدينة
        filter_frame = tk.Frame(toolbar, bg=Colors.BG_LIGHT)
        filter_frame.pack(side='right', padx=20, pady=10)
        
        tk.Label(filter_frame, text="فلترة حسب المدينة:", **Styles.LABEL_HEADER).pack(side='right', padx=5)
        
        self.city_var = tk.StringVar(value="جميع المدن")
        city_combo = ttk.Combobox(filter_frame, textvariable=self.city_var, 
                                 values=["جميع المدن", "جدة", "مكة", "الرياض", "الدمام"], 
                                 state="readonly", width=15)
        city_combo.pack(side='right', padx=5)
        city_combo.bind('<<ComboboxSelected>>', self.on_city_filter)
        
        # أزرار التحكم
        buttons_frame = tk.Frame(toolbar, bg=Colors.BG_LIGHT)
        buttons_frame.pack(side='left', padx=20, pady=10)
        
        tk.Button(buttons_frame, text="➕ إضافة عميل", command=self.show_add_customer,
                 cursor='hand2', **Styles.BTN_SUCCESS).pack(side='left', padx=5)
        
        tk.Button(buttons_frame, text="📊 التقارير", command=self.show_reports,
                 cursor='hand2', **Styles.BTN_PRIMARY).pack(side='left', padx=5)
    
    def create_content_area(self):
        """منطقة المحتوى الرئيسية"""
        # إطار رئيسي للمحتوى
        content_frame = tk.Frame(self.root, bg=Colors.BG_LIGHT)
        content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # العملاء المستحقين (50% من الأعلى)
        due_frame = tk.LabelFrame(content_frame, text="🔄 العملاء الذين حان موعد صيانتهم", 
                                 font=Fonts.HEADER, bg=Colors.BG_LIGHT, fg=Colors.DARK, height=300)
        due_frame.pack(fill='x', pady=(0, 10))
        due_frame.pack_propagate(False)
        
        self.create_due_table(due_frame)
        
        # جميع العملاء (50% من الأسفل)
        all_frame = tk.LabelFrame(content_frame, text="👥 جميع العملاء", 
                                 font=Fonts.HEADER, bg=Colors.BG_LIGHT, fg=Colors.DARK)
        all_frame.pack(fill='both', expand=True)
        
        self.create_all_table(all_frame)
    
    def create_due_table(self, parent):
        """جدول العملاء المستحقين"""
        columns = ("الاسم", "المدينة", "الحي", "الجوال", "الجهاز", "الموعد")
        self.due_tree = ttk.Treeview(parent, columns=columns, show="headings", height=8)
        
        # تحديد عرض الأعمدة
        widths = [150, 100, 120, 120, 100, 100]
        for col, width in zip(columns, widths):
            self.due_tree.heading(col, text=col)
            self.due_tree.column(col, width=width, anchor='center')
        
        # شريط التمرير
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.due_tree.yview)
        self.due_tree.configure(yscrollcommand=scrollbar.set)
        
        self.due_tree.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y', pady=5)
    
    def create_all_table(self, parent):
        """جدول جميع العملاء"""
        columns = ("الرقم", "الاسم", "المدينة", "الحي", "الجوال", "الجهاز", "التركيب", "التغيير")
        self.all_tree = ttk.Treeview(parent, columns=columns, show="headings", height=15)
        
        # تحديد عرض الأعمدة
        widths = [60, 150, 100, 120, 120, 100, 100, 100]
        for col, width in zip(columns, widths):
            self.all_tree.heading(col, text=col)
            self.all_tree.column(col, width=width, anchor='center')
        
        # شريط التمرير
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.all_tree.yview)
        self.all_tree.configure(yscrollcommand=scrollbar.set)
        
        self.all_tree.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y', pady=5)
    
    def load_data(self):
        """تحميل البيانات في الجداول"""
        self.load_due_customers()
        self.load_all_customers()
    
    def load_due_customers(self):
        """تحميل العملاء المستحقين"""
        for item in self.due_tree.get_children():
            self.due_tree.delete(item)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT name, city, district, phone, device_type, next_maintenance 
            FROM customers 
            WHERE next_maintenance <= date('now') 
            ORDER BY city, next_maintenance
        ''')
        
        for row in cursor.fetchall():
            self.due_tree.insert("", "end", values=row)
        
        conn.close()
    
    def load_all_customers(self):
        """تحميل جميع العملاء"""
        for item in self.all_tree.get_children():
            self.all_tree.delete(item)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, name, city, district, phone, device_type, 
                   installation_date, next_maintenance 
            FROM customers 
            ORDER BY city, name
        ''')
        
        for row in cursor.fetchall():
            self.all_tree.insert("", "end", values=row)
        
        conn.close()
    
    def on_search(self, event=None):
        """البث الفوري عند البحث"""
        pass  # سيتم تنفيذها لاحقاً
    
    def on_city_filter(self, event=None):
        """فلترة حسب المدينة"""
        pass  # سيتم تنفيذها لاحقاً
    
    def show_add_customer(self):
        """نافذة إضافة عميل جديد"""
        messagebox.showinfo("قريباً", "سيتم تنفيذ نافذة إضافة عميل في الخطوة القادمة")
    
    def show_reports(self):
        """نافذة التقارير"""
        messagebox.showinfo("قريباً", "سيتم تنفيذ التقارير في الخطوة القادمة")
    
    def run(self):
        """تشغيل التطبيق"""
        self.root.mainloop()

# تشغيل التطبيق
if __name__ == "__main__":
    app = ModernAdminPanel()
    app.run()
