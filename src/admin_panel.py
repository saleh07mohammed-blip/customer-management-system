import tkinter as tk
from tkinter import ttk, messagebox
from database import DatabaseManager
from datetime import datetime, timedelta

class AdminPanel:
    def __init__(self):
        self.db = DatabaseManager()
        self.current_user = None
        
        # إنشاء النافذة الرئيسية
        self.root = tk.Tk()
        self.root.title("نظام إدارة العملاء - الواجهة الإدارية")
        self.root.geometry("1200x700")
        self.root.configure(bg='#f0f0f0')
        
        # تشغيل واجهة تسجيل الدخول أولاً
        self.show_login()
    
    def show_login(self):
        """شاشة تسجيل الدخول"""
        login_window = tk.Toplevel(self.root)
        login_window.title("تسجيل الدخول")
        login_window.geometry("300x200")
        login_window.configure(bg='#f0f0f0')
        login_window.transient(self.root)
        login_window.grab_set()
        
        tk.Label(login_window, text="اسم المستخدم:", bg='#f0f0f0').pack(pady=5)
        username_entry = tk.Entry(login_window, width=20)
        username_entry.pack(pady=5)
        
        tk.Label(login_window, text="كلمة المرور:", bg='#f0f0f0').pack(pady=5)
        password_entry = tk.Entry(login_window, width=20, show="*")
        password_entry.pack(pady=5)
        
        def login():
            username = username_entry.get()
            password = password_entry.get()
            
            # هنا سيتم التحقق من قاعدة البيانات
            if username == "admin" and password == "admin123":
                self.current_user = username
                login_window.destroy()
                self.show_main_panel()
            else:
                messagebox.showerror("خطأ", "اسم المستخدم أو كلمة المرور غير صحيحة")
        
        tk.Button(login_window, text="دخول", command=login, bg='#4CAF50', fg='white').pack(pady=10)
        
        # جعل النافذة في المنتصف
        login_window.update_idletasks()
        x = (login_window.winfo_screenwidth() // 2) - (login_window.winfo_width() // 2)
        y = (login_window.winfo_screenheight() // 2) - (login_window.winfo_height() // 2)
        login_window.geometry(f"+{x}+{y}")

    def show_main_panel(self):
        """الشاشة الرئيسية للمدير"""
        # مسح أي عناصر موجودة مسبقاً
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.title(f"نظام إدارة العملاء - المدير: {self.current_user}")
        
        # إنشاء الهيكل الرئيسي
        self.create_main_layout()
        
        # تحميل البيانات
        self.load_customers()
        self.load_due_customers()

    def create_main_layout(self):
        """إنشاء هيكل الواجهة الرئيسية"""
        # العنوان
        title_label = tk.Label(self.root, text="نظام إدارة عملاء الصيانة", 
                              font=("Arial", 16, "bold"), bg='#f0f0f0')
        title_label.pack(pady=10)
        
        # إطار العملاء الذين حان موعدهم
        due_frame = tk.LabelFrame(self.root, text="العملاء الذين حان موعد صيانتهم", 
                                 font=("Arial", 12, "bold"), bg='#f0f0f0')
        due_frame.pack(fill="x", padx=10, pady=5)
        
        # جدول العملاء المستحقين
        self.due_tree = ttk.Treeview(due_frame, columns=("ID", "Name", "Phone", "DueDate"), show="headings", height=6)
        self.due_tree.heading("ID", text="رقم")
        self.due_tree.heading("Name", text="اسم العميل")
        self.due_tree.heading("Phone", text="رقم الجوال")
        self.due_tree.heading("DueDate", text="موعد الصيانة")
        
        self.due_tree.column("ID", width=50)
        self.due_tree.column("Name", width=150)
        self.due_tree.column("Phone", width=120)
        self.due_tree.column("DueDate", width=120)
        
        self.due_tree.pack(fill="x", padx=5, pady=5)
        
        # أزرار التحكم في العملاء المستحقين
        due_buttons_frame = tk.Frame(due_frame, bg='#f0f0f0')
        due_buttons_frame.pack(pady=5)
        
        tk.Button(due_buttons_frame, text="تم الصيانة", bg='#4CAF50', fg='white').pack(side="left", padx=5)
        tk.Button(due_buttons_frame, text="تأجيل الموعد", bg='#FF9800', fg='white').pack(side="left", padx=5)
        
        # إطار جميع العملاء
        all_customers_frame = tk.LabelFrame(self.root, text="جميع العملاء", 
                                           font=("Arial", 12, "bold"), bg='#f0f0f0')
        all_customers_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # جدول جميع العملاء
        self.customers_tree = ttk.Treeview(all_customers_frame, 
                                          columns=("ID", "Name", "City", "Phone", "Device", "InstallDate", "NextDate"),
                                          show="headings", height=15)
        
        self.customers_tree.heading("ID", text="رقم")
        self.customers_tree.heading("Name", text="اسم العميل")
        self.customers_tree.heading("City", text="المدينة")
        self.customers_tree.heading("Phone", text="رقم الجوال")
        self.customers_tree.heading("Device", text="نوع الجهاز")
        self.customers_tree.heading("InstallDate", text="تاريخ التركيب")
        self.customers_tree.heading("NextDate", text="موعد التغيير")
        
        self.customers_tree.column("ID", width=50)
        self.customers_tree.column("Name", width=150)
        self.customers_tree.column("City", width=100)
        self.customers_tree.column("Phone", width=120)
        self.customers_tree.column("Device", width=100)
        self.customers_tree.column("InstallDate", width=100)
        self.customers_tree.column("NextDate", width=100)
        
        self.customers_tree.pack(fill="both", expand=True, padx=5, pady=5)
        
        # أزرار التحكم
        buttons_frame = tk.Frame(self.root, bg='#f0f0f0')
        buttons_frame.pack(pady=10)
        
        tk.Button(buttons_frame, text="إضافة عميل جديد", bg='#2196F3', fg='white', 
                 command=self.show_add_customer).pack(side="left", padx=5)
        tk.Button(buttons_frame, text="تحديث البيانات", bg='#607D8B', fg='white',
                 command=self.load_customers).pack(side="left", padx=5)
        tk.Button(buttons_frame, text="التقارير", bg='#9C27B0', fg='white').pack(side="left", padx=5)
        tk.Button(buttons_frame, text="خروج", bg='#f44336', fg='white',
                 command=self.root.quit).pack(side="left", padx=5)

    def load_customers(self):
        """تحميل قائمة جميع العملاء"""
        # مسح البيانات الحالية
        for item in self.customers_tree.get_children():
            self.customers_tree.delete(item)
        
        # جلب البيانات من قاعدة البيانات
        customers = self.db.get_customers()
        for customer in customers:
            self.customers_tree.insert("", "end", values=customer)

    def load_due_customers(self):
        """تحميل العملاء الذين حان موعدهم"""
        # مسح البيانات الحالية
        for item in self.due_tree.get_children():
            self.due_tree.delete(item)
        
        # جلب البيانات من قاعدة البيانات
        due_customers = self.db.get_due_customers()
        for customer in due_customers:
            # نأخذ فقط الأعمدة المطلوبة للعرض
            display_data = (customer[0], customer[1], customer[4], customer[7])
            self.due_tree.insert("", "end", values=display_data)

    def show_add_customer(self):
        """نافذة إضافة عميل جديد"""
        add_window = tk.Toplevel(self.root)
        add_window.title("إضافة عميل جديد")
        add_window.geometry("400x500")
        add_window.configure(bg='#f0f0f0')
        add_window.transient(self.root)
        add_window.grab_set()
        
        # حقول الإدخال
        fields = [
            ("اسم العميل:", "name"),
            ("المدينة:", "city"),
            ("الحي:", "district"),
            ("رقم الجوال:", "phone"),
            ("نوع الجهاز:", "device_type"),
            ("تاريخ التركيب (YYYY-MM-DD):", "installation_date")
        ]
        
        entries = {}
        
        for i, (label, key) in enumerate(fields):
            tk.Label(add_window, text=label, bg='#f0f0f0').grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(add_window, width=25)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            entries[key] = entry
        
        # خيارات موعد التغيير
        tk.Label(add_window, text="موعد التغيير بعد:", bg='#f0f0f0').grid(row=6, column=0, padx=10, pady=5, sticky="e")
        
        period_frame = tk.Frame(add_window, bg='#f0f0f0')
        period_frame.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        
        period_value = tk.Entry(period_frame, width=5)
        period_value.pack(side="left")
        
        period_type = ttk.Combobox(period_frame, values=["أيام", "أسابيع", "شهور", "سنوات"], width=8)
        period_type.set("أشهر")
        period_type.pack(side="left", padx=5)
        
        def calculate_next_date():
            """حساب تاريخ التغيير التالي"""
            install_date = entries['installation_date'].get()
            if install_date:
                try:
                    install_dt = datetime.strptime(install_date, "%Y-%m-%d")
                    value = int(period_value.get()) if period_value.get() else 0
                    period = period_type.get()
                    
                    if period == "أيام":
                        next_date = install_dt + timedelta(days=value)
                    elif period == "أسابيع":
                        next_date = install_dt + timedelta(weeks=value)
                    elif period == "شهور":
                        next_date = install_dt + timedelta(days=value * 30)
                    else:  # سنوات
                        next_date = install_dt + timedelta(days=value * 365)
                    
                    entries['next_maintenance'] = next_date.strftime("%Y-%m-%d")
                    messagebox.showinfo("تم", f"موعد التغيير: {entries['next_maintenance']}")
                except ValueError:
                    messagebox.showerror("خطأ", "تاريخ التركيب غير صحيح")
        
        tk.Button(period_frame, text="حساب", command=calculate_next_date).pack(side="left", padx=5)
        
        def save_customer():
            """حفظ العميل الجديد"""
            try:
                # جمع البيانات من الحقول
                customer_data = {
                    'name': entries['name'].get(),
                    'city': entries['city'].get(),
                    'district': entries['district'].get(),
                    'phone': entries['phone'].get(),
                    'device_type': entries['device_type'].get(),
                    'installation_date': entries['installation_date'].get(),
                    'next_maintenance': entries.get('next_maintenance', ''),
                    'employee_id': 1  # سيتم تعديله لاحقاً حسب المستخدم المسجل
                }
                
                # التحقق من البيانات المطلوبة
                if not customer_data['name'] or not customer_data['installation_date']:
                    messagebox.showerror("خطأ", "الرجاء ملء الحقول المطلوبة")
                    return
                
                # حفظ في قاعدة البيانات
                self.db.add_customer(**customer_data)
                messagebox.showinfo("تم", "تم إضافة العميل بنجاح")
                add_window.destroy()
                self.load_customers()
                self.load_due_customers()
                
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الحفظ: {str(e)}")
        
        tk.Button(add_window, text="حفظ", command=save_customer, bg='#4CAF50', fg='white').grid(row=7, column=0, columnspan=2, pady=20)
        
        # جعل النافذة في المنتصف
        add_window.update_idletasks()
        x = (add_window.winfo_screenwidth() // 2) - (add_window.winfo_width() // 2)
        y = (add_window.winfo_screenheight() // 2) - (add_window.winfo_height() // 2)
        add_window.geometry(f"+{x}+{y}")

    def run(self):
        """تشغيل الواجهة"""
        self.root.mainloop()

# اختبار التشغيل
if __name__ == "__main__":
    app = AdminPanel()
    app.run()
