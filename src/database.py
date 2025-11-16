import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        self.db_path = "customers.db"
        self.init_database()
    
    def init_database(self):
        """إنشاء الجداول الأساسية"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # جدول العملاء
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
        
        # جدول الموظفين
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT,
                is_active INTEGER DEFAULT 1,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # جدول التفعيلات
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activation_code TEXT UNIQUE NOT NULL,
                user_type TEXT NOT NULL,
                max_employees INTEGER DEFAULT 0,
                is_used INTEGER DEFAULT 0,
                used_date TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✅ تم إنشاء قاعدة البيانات بنجاح")

    # دوال إدارة العملاء
    def add_customer(self, name, city, district, phone, device_type, installation_date, next_maintenance, employee_id):
        """إضافة عميل جديد"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO customers (name, city, district, phone, device_type, installation_date, next_maintenance, employee_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, city, district, phone, device_type, installation_date, next_maintenance, employee_id))
        
        conn.commit()
        conn.close()
        return True
    
    def get_customers(self, employee_id=None):
        """جلب قائمة العملاء"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if employee_id:
            cursor.execute('''
                SELECT * FROM customers WHERE employee_id = ? ORDER BY next_maintenance
            ''', (employee_id,))
        else:
            cursor.execute('SELECT * FROM customers ORDER BY next_maintenance')
        
        customers = cursor.fetchall()
        conn.close()
        return customers
    
    def get_due_customers(self):
        """جلب العملاء الذين حان موعد صيانتهم"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM customers 
            WHERE next_maintenance <= date('now') 
            ORDER BY next_maintenance
        ''')
        
        due_customers = cursor.fetchall()
        conn.close()
        return due_customers
    
    def update_maintenance_date(self, customer_id, new_date):
        """تحديث موعد الصيانة"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE customers SET next_maintenance = ? WHERE id = ?
        ''', (new_date, customer_id))
        
        conn.commit()
        conn.close()
        return True

# اختبار التشغيل
if __name__ == "__main__":
    db = DatabaseManager()
    print("✅ تم اختبار قاعدة البيانات بنجاح")
