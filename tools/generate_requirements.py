# tools/generate_requirements.py

import subprocess

def export_requirements(output_path="requirements.txt"):
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            subprocess.run(["pip", "freeze"], stdout=f, check=True)
        print(f"✅ فایل {output_path} با موفقیت ساخته شد.")
    except Exception as e:
        print(f"❌ خطا در ساخت فایل requirements.txt: {e}")

if __name__ == "__main__":
    export_requirements()
