import pandas as pd

def build_model(inputs):
    """
    محاسبات شیت Model مشابه VBA
    ورودی: inputs -> دیکشنری داده‌های ورودی
    خروجی: DataFrame شامل سناریوها و محاسبات
    """
    scenarios = ['Delta_s_1', 'Delta_s_2', 'Delta_s_3']

    df = pd.DataFrame({
        'Scenario': scenarios,
        'Delta_s': [inputs[s] for s in scenarios]
    })

    # بازده واقعی
    y = 1 - inputs['s0_Scrap_rate']

    # محاسبه صرفه‌جویی ماهانه و سایر شاخص‌ها
    df['Saving_T_per_month'] = inputs['Qu_Output_ft2_per_month'] * inputs['Cf_Toman_per_ft2'] * df['Delta_s'] / (y + df['Delta_s'])
    df['Saving_USD_per_month'] = df['Saving_T_per_month'] / inputs['Toman_per_USD']
    df['Saving_90d_T'] = df['Saving_T_per_month'] * 3
    df['Cf_new_T'] = inputs['Cf_Toman_per_ft2'] * y / (y + df['Delta_s'])

    # فرض می‌کنیم Plan با Delta_s_2 به عنوان سناریوی برنامه استفاده شود
    delta_s_plan = inputs['Delta_s_2']

    df_plan = pd.DataFrame({
        'Scenario': ['Plan'],
        'Delta_s': [delta_s_plan],
        'Saving_T_per_month': [
            inputs['Qu_Output_ft2_per_month'] * inputs['Cf_Toman_per_ft2'] * delta_s_plan / (y + delta_s_plan)
        ]
    })
    df_plan['Saving_USD_per_month'] = df_plan['Saving_T_per_month'] / inputs['Toman_per_USD']
    df_plan['Saving_90d_T'] = df_plan['Saving_T_per_month'] * 3
    df_plan['Cf_new_T'] = inputs['Cf_Toman_per_ft2'] * y / (y + delta_s_plan)
    df_plan['Payback_months'] = inputs['Budget_Toman'] / df_plan['Saving_T_per_month']
    df_plan['s_new_plan'] = inputs['s0_Scrap_rate'] - delta_s_plan
    df_plan['Delta_s_break_even_90d'] = (inputs['Budget_Toman'] * y) / (
        3 * inputs['Qu_Output_ft2_per_month'] * inputs['Cf_Toman_per_ft2'] - inputs['Budget_Toman']
    )

    # ترکیب سناریوها و Plan
    df_final = pd.concat([df, df_plan], ignore_index=True)

    return df_final


if __name__ == "__main__":
    from inputs_manager import load_inputs
    from pathlib import Path

    # مسیر صحیح فایل ورودی
    file_path = Path(r"D:\beno.co\My_Python_Project\LeatherPilot2025\data\inputs.xlsx.xlsx")
    inputs = load_inputs(file_path)

    model_df = build_model(inputs)
    print("✅ Model calculations completed:")
    print(model_df)

    # ذخیره در Excel
    output_path = Path(r"D:\beno.co\My_Python_Project\LeatherPilot2025\data\output_model.xlsx")
    model_df.to_excel(output_path, index=False)
    print(f"✅ Model saved to {output_path}")
