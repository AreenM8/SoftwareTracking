import streamlit as st
import pandas as pdstreamlit 
from openpyxl import load_workbook
from datetime import datetime

excel_file = "Software_Tracking.xlsx"

st.title("نموذج متابعة البرامج")

program_name = st.text_input("اسم البرنامج")
program_goal = st.text_input("الهدف من البرنامج")
college = st.selectbox("الكلية", ["كلية العلوم", "كلية الهندسة", "كلية الحاسبات وتقنية المعلومات", "كلية الطب", "كلية الإقتصاد والإدارة", "كلية الآداب والعلوم الإنسانية", "كلية علوم الإنسان والتصاميم"])
department = st.text_input("القسم")
responsible_person = st.text_input("الجهة المسؤولة")
user_type = st.selectbox("نوع المستخدمين", ["طلاب", "أعضاء هيئة التدريس", "إداريين"])
user_num =  st.number_input("عدد المستخدمين ", min_value=1, step=1)
program_status = st.selectbox("حالة البرنامج", ["نشط", "غير نشط", "منتهي الصلاحية"])

license_type = st.selectbox("نوع الترخيص", ["شهري", "سنوي", "مدى الحياة"])
start_date = st.date_input("تاريخ بداية الترخيص")
end_date = st.date_input("تاريخ نهاية الترخيص")
cost = st.number_input("التكلفة", min_value=0.0, step=0.01)
payment_method = st.selectbox("آلية الدفع", ["شهرياً", "سنويًا", "دفعة واحدة"])
license_number = st.text_input("رقم الترخيص")
available_licenses = st.number_input("عدد التراخيص المتوفرة", min_value=1, step=1)

update_frequency = st.selectbox("تكرار التحديثات", ["شهري", "نصف سنوي", "سنوي"])
usage_rating = st.selectbox("تقييم الاستخدام", ["عالي", "متوسط", "منخفض"])
last_update_date = st.date_input("تاريخ آخر تحديث")
security_updates_needed = st.selectbox("الحاجة لتحديثات الأمان", ["نعم", "لا"])

supported_os = st.selectbox("نظام التشغيل المدعوم", ["Windows", "macOS", "Linux", "Android", "iOS", "Chrome OS"])
internet_dependency = st.selectbox("مستوى الاعتماد على الإنترنت", ["عالي", "متوسط", "منخفض"])

#  لحفظ البيانات
if st.button("حفظ البيانات"):
    new_data = {
        "اسم البرنامج": program_name,
        "الهدف من البرنامج": program_goal,
        "الكلية": college,
        "القسم": department,
        "الجهة المسؤولة": responsible_person,
        "نوع المستخدمين": user_type,
        "عدد المستخدمين ": user_num,
        "حالة البرنامج": program_status,
        "نوع الترخيص": license_type,
        "تاريخ بداية الترخيص": start_date,
        "تاريخ نهاية الترخيص": end_date,
        "التكلفة": cost,
        "آلية الدفع": payment_method,
        "رقم الترخيص": license_number,
        "عدد التراخيص المتوفرة": available_licenses,
        "تكرار التحديثات": update_frequency,
        "تقييم الاستخدام": usage_rating,
        "تاريخ آخر تحديث": last_update_date,
        "الحاجة لتحديثات الأمان": security_updates_needed,
        "نظام التشغيل المدعوم": supported_os,
        "مستوى الاعتماد على الإنترنت": internet_dependency
    }

    wb = load_workbook(excel_file)
    sheet = wb.active
    sheet.append(list(new_data.values()))
    wb.save(excel_file)
    st.success("تمت إضافة البيانات بنجاح!")
