        # حقول الإدخال
        fields = [
            ("اسم العميل:", "name"),
            ("المدينة:", "city"),
            ("الحي:", "district"),
            ("رقم الجوال:", "phone"),
            ("نوع الجهاز:", "device_type")
        ]
        
        entries = {}
        
        for i, (label, key) in enumerate(fields):
            tk.Label(add_window, text=label, bg='#f0f0f0').grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(add_window, width=25)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            entries[key] = entry
        
        # حقل تاريخ التركيب مع زر التقويم
        tk.Label(add_window, text="تاريخ التركيب:", bg='#f0f0f0').grid(row=5, column=0, padx=10, pady=5, sticky="e")

        date_frame = tk.Frame(add_window, bg='#f0f0f0')
        date_frame.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        installation_entry = tk.Entry(date_frame, width=15)
        installation_entry.pack(side="left")
        entries['installation_date'] = installation_entry

        def choose_installation_date():
            from tkinter import simpledialog
            import datetime
            
            date_str = simpledialog.askstring("اختيار التاريخ", "أدخل التاريخ (YYYY-MM-DD):\nمثال: 2024-01-15")
            if date_str:
                try:
                    datetime.datetime.strptime(date_str, "%Y-%m-%d")
                    installation_entry.delete(0, tk.END)
                    installation_entry.insert(0, date_str)
                except ValueError:
                    messagebox.showerror("خطأ", "صيغة التاريخ غير صحيحة. استخدم YYYY-MM-DD")

        tk.Button(date_frame, text="📅", command=choose_installation_date, width=3).pack(side="left", padx=5)
