import pandas as pd
from pathlib import Path


def load_inputs(file_path):
    """
    خواندن داده‌های ورودی از فایل Excel (inputs.xlsx)
    خروجی: دیکشنری شامل پارامترها
    """
    df = pd.read_excel(file_path)
    # بررسی اینکه ستون‌ها درست باشند
    if not {'Key', 'Value'}.issubset(df.columns):
        raise ValueError("فایل ورودی باید دو ستون با نام‌های 'Key' و 'Value' داشته باشد.")

    # تبدیل DataFrame به دیکشنری
    inputs_dict = pd.Series(df.Value.values, index=df.Key).to_dict()
    return inputs_dict


if __name__ == "__main__":
    # مسیر فایل ورودی (اینجا باید مسیر واقعی فایل توی دسکتاپت رو بنویسی)
    file_path = Path(r"/D:\beno.co\My_Python_Project\LeatherPilot2025\inputs.xlsx")

    inputs = load_inputs(file_path)
    print("✅ داده‌های ورودی با موفقیت بارگذاری شدند:")
    for key, value in inputs.items():
        print(f"{key}: {value}")
