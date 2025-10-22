import pandas as pd
import numpy as np

def simulate_kpi_log(inputs, weeks=12, scenario_key='Delta_s_2'):
    """
    شبیه‌سازی KPI_Log هفتگی با Δs واقعی تصادفی
    ورودی:
        inputs: دیکشنری داده‌های ورودی
        weeks: تعداد هفته‌ها
        scenario_key: کلید سناریویی که Δs واقعی حول آن شبیه‌سازی می‌شود
    خروجی:
        DataFrame هفتگی شامل Δs واقعی، Saving و Cf واقعی
    """
    np.random.seed(42)  # برای reproducibility

    # مقدار Δs سناریوی انتخاب شده
    delta_s_plan = inputs[scenario_key]

    # بازده واقعی
    y = 1 - inputs['s0_Scrap_rate']

    data = []
    cumulative_saving = 0

    for week in range(1, weeks+1):
        # شبیه‌سازی Δs واقعی با نویز ±10٪
        delta_s_real = np.random.normal(loc=delta_s_plan, scale=delta_s_plan*0.1)
        delta_s_real = max(0, delta_s_real)  # Δs نمی‌تواند منفی باشد

        # محاسبه صرفه‌جویی هفتگی
        saving_week = inputs['Qu_Output_ft2_per_month'] * inputs['Cf_Toman_per_ft2'] * delta_s_real / (y + delta_s_real)
        cumulative_saving += saving_week

        # محاسبه Cf واقعی
        Cf_real = inputs['Cf_Toman_per_ft2'] * y / (y + delta_s_real)

        data.append({
            'Week': week,
            'Delta_s_real': delta_s_real,
            'Saving_T_week': saving_week,
            'Cumulative_Saving_T': cumulative_saving,
            'Saving_USD_week': saving_week / inputs['Toman_per_USD'],
            'Cumulative_Saving_USD': cumulative_saving / inputs['Toman_per_USD'],
            'Cf_real': Cf_real
        })

    df_kpi = pd.DataFrame(data)
    return df_kpi

if __name__ == "__main__":
    from inputs_manager import load_inputs
    from pathlib import Path

    file_path = Path(r"D:\beno.co\My_Python_Project\LeatherPilot2025\data\inputs.xlsx.xlsx")
    inputs = load_inputs(file_path)

    kpi_df = simulate_kpi_log(inputs)
    print("✅ KPI_Log simulation completed:")
    print(kpi_df)

    # ذخیره در Excel
    output_path = Path(r"D:\beno.co\My_Python_Project\LeatherPilot2025\data\kpi_log.xlsx")
    kpi_df.to_excel(output_path, index=False)
    print(f"✅ KPI_Log saved to {output_path}")
