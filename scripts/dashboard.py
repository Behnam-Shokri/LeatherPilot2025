import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# بارگذاری داده‌ها
model_file = Path(r"D:\beno.co\My_Python_Project\LeatherPilot2025\data\output_model.xlsx")
kpi_file = Path(r"D:\beno.co\My_Python_Project\LeatherPilot2025\data\kpi_log.xlsx")

model_df = pd.read_excel(model_file, engine='openpyxl')
kpi_df = pd.read_excel(kpi_file, engine='openpyxl')

print("✅ Data loaded successfully")
print(model_df.head())
print(kpi_df.head())

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib import rcParams
import numpy as np
from scipy.interpolate import make_interp_spline

# تنظیم فونت فارسی
rcParams['font.family'] = 'Tahoma'  # یا هر فونت فارسی نصب‌شده

# مسیر فایل KPI_Log
kpi_file = Path(r"D:\beno.co\My_Python_Project\LeatherPilot2025\data\kpi_log.xlsx")
kpi_df = pd.read_excel(kpi_file, engine='openpyxl')

# مقدار Δs هدف
Delta_s_target = 0.025  # مثال: 2.5%
kpi_df['Delta_s_target'] = Delta_s_target

# نرم کردن خط Δs واقعی
weeks = kpi_df['Week']
delta_real = kpi_df['Delta_s_real']

# استفاده از spline برای نرمی خط
x_new = np.linspace(weeks.min(), weeks.max(), 300)  # نقاط بیشتر برای خط صاف
spl = make_interp_spline(weeks, delta_real, k=3)  # k=3 برای cubic spline
delta_s_smooth = spl(x_new)

# رسم نمودار
plt.figure(figsize=(10, 6))
plt.plot(x_new, delta_s_smooth, label='Δs  (Actual)', color='blue')
plt.plot(weeks, kpi_df['Delta_s_target'], linestyle='--', color='red', label='Δs  (Target)', marker='o')

plt.title('Actual vs. Planned Scrap')
plt.xlabel('Week')
plt.ylabel('Δs')
plt.xticks(weeks)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# ذخیره نمودار
output_path = Path(r"D:\beno.co\My_Python_Project\LeatherPilot2025\data\Scrap_Actual_vs_Target.png")
plt.savefig(output_path, dpi=300)
plt.show()
print(f"✅ نمودار ذخیره شد در: {output_path}")


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# -----------------------------
# Example data (from your scenario file)
# -----------------------------
data = {
    'Delta_s': [0.01, 0.025, 0.05],
    'Payback_months': [3.5, 1.95, 1.1]
}

df = pd.DataFrame(data)

# -----------------------------
# Smooth the curve using spline
# -----------------------------
x = df['Delta_s']
y = df['Payback_months']

x_new = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=2)
y_smooth = spl(x_new)

# -----------------------------
# Plot setup
# -----------------------------
plt.figure(figsize=(9, 6))
plt.plot(x_new, y_smooth, color='#007acc', linewidth=2.5, label='Payback Curve')
plt.scatter(x, y, color='red', s=80, zorder=5, label='Scenarios')

# Labels and title
plt.title('Impact of Scrap Reduction on Payback Period', fontsize=14, fontweight='bold')
plt.xlabel('Scrap Reduction (Δs)', fontsize=12)
plt.ylabel('Payback Period (months)', fontsize=12)

# Grid and legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig(r"D:\beno.co\My_Python_Project\LeatherPilot2025\data\Payback_vs_Scrap.png", dpi=300)

plt.show()
print("✅ Chart saved successfully: Payback_vs_Scrap.png")

