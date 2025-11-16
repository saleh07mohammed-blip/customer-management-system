# ملف اختبار النظام
from src.database import DatabaseManager

def test_database():
    print("🧪 بدء اختبار قاعدة البيانات...")
    
    try:
        # اختبار إنشاء قاعدة البيانات
        db = DatabaseManager()
        print("✅ تم إنشاء قاعدة البيانات بنجاح")
        
        # اختبار إضافة عميل
        db.add_customer(
            name="أحمد محمد",
            city="جدة",
            district="المشرفة",
            phone="0550555555",
            device_type="جامبو",
            installation_date="2024-01-01",
            next_maintenance="2024-04-01",
            employee_id=1
        )
        print("✅ تم إضافة عميل اختبار")
        
        # اختبار جلب العملاء
        customers = db.get_customers()
        print(f"✅ عدد العملاء في النظام: {len(customers)}")
        
        # اختبار العملاء المستحقين
        due_customers = db.get_due_customers()
        print(f"✅ عدد العملاء المستحقين: {len(due_customers)}")
        
        print("🎉 جميع الاختبارات completed بنجاح!")
        
    except Exception as e:
        print(f"❌ خطأ في الاختبار: {e}")

if __name__ == "__main__":
    test_database()
