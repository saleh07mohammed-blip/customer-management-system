# نظام إدارة العملاء
# Customer Management System

from src.admin_panel import AdminPanel

def main():
    print("🚀 بدء تشغيل نظام إدارة العملاء...")
    
    # اختبار واجهة المدير
    try:
        app = AdminPanel()
        app.run()
    except Exception as e:
        print(f"❌ خطأ في التشغيل: {e}")
        input("اضغط Enter للإغلاق...")

if __name__ == "__main__":
    main()
