import os
from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

# الحصول على المسار المطلق للملف الحالي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# تحديد مسار مجلد التنزيلات كمسار مطلق
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'configs')

# التأكد من وجود المجلدات
for config_type in ['HTTP_CUSTOM', 'Dark_Tunnel','Tls_Tunnel']:
    config_type_path = os.path.join(DOWNLOAD_FOLDER, config_type)
    if not os.path.exists(config_type_path):
        os.makedirs(config_type_path)

# أنواع الكونفيغ المتاحة
CONFIG_TYPES = ['HTTP_CUSTOM', 'Dark_Tunnel','Tls_Tunnel']

def get_unique_filename(directory, filename):
    """إضافة رقم في حالة وجود ملف بنفس الاسم لتجنب التداخل"""
    base_name, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base_name}({counter}){extension}"
        counter += 1
    return new_filename

@app.route('/')
def index():
    config_files = {}
    for config_type in CONFIG_TYPES:
        config_dir = os.path.join(DOWNLOAD_FOLDER, config_type)
        config_files[config_type] = [f for f in os.listdir(config_dir) if os.path.isfile(os.path.join(config_dir, f))]
    
    return render_template_string(HTML_TEMPLATE, config_files=config_files)

@app.route('/download/<config_type>/<filename>')
def download(config_type, filename):
    config_path = os.path.join(DOWNLOAD_FOLDER, config_type)
    return send_from_directory(config_path, filename, as_attachment=True)

# ... باقي الكود مع القالب HTML يبقى كما هو دون تغيير ...
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تنزيل كونفغات كسر محدودية واتساب</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
            background-color: #f4f4f4;
            background-image: url('https://i.pinimg.com/736x/8d/a7/d4/8da7d4f6b60163fecb7177f3180073b5.jpg');
           
            background-size: cover;
            background-position: center center fixed;
            color: #ffffff;
        }
        .container {
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.5);
            background: rgba(0, 0, 0, 0.7);
        }
        .header {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #ffcc00;
            text-shadow: 0 0 5px #ff6600, 0 0 10px #ff6600, 0 0 15px #ff6600;
            animation: glow 1.5s ease-in-out infinite alternate;
        }
        .file-select select {
            padding: 10px;
            font-size: 16px;
            width: 100%;
            border-radius: 15px;
            border: 2px solid #ffcc00;
            background-color: #333;
            color: #ffcc00;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .file-list {
            margin-top: 20px;
            width: 100%;
        }
        .file-item {
            background-color: #333;
            padding: 10px;
            margin: 10px 0;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
            transition: transform 0.2s ease;
        }
        .file-item:hover {
            transform: scale(1.05);
            box-shadow: 0 0 10px #ff6600;
        }
        .file-item button {
            background-color: #ff6600;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            padding: 5px 15px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .file-item button:hover {
            background-color: #ff4500;
            transform: scale(1.1);
        }
        .icon {
            display: inline-block;
            vertical-align: middle;
            margin-right: 8px;
            width: 24px;
            height: 24px;
        }
        .telegram-icon {
            width: 40px;
            height: 40px;
            margin-top: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 50%;
            background-color: #0088cc;
            padding: 5px;
            box-shadow: 0 0 10px #0088cc, 0 0 20px #0088cc, 0 0 30px #0088cc;
        }
        .telegram-icon:hover {
            transform: scale(1.2);
            box-shadow: 0 0 15px #0088cc, 0 0 25px #0088cc, 0 0 40px #0088cc;
        }
        .animated-name {
            font-size: 36px;
            font-weight: bold;
            margin-top: 15px;
            color: #ff3300;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            animation: colorShift 4s ease-in-out infinite, text3D 2s infinite;
        }
        @keyframes glow {
            from { color: #ffcc00; text-shadow: 0 0 5px #ff6600, 0 0 10px #ff6600; }
            to { color: #ff6600; text-shadow: 0 0 10px #ffcc00, 0 0 20px #ffcc00; }
        }
        @keyframes colorShift {
            0% { color: #ff3300; }
            25% { color: #ff6600; }
            50% { color: #ffcc00; }
            75% { color: #ff4500; }
            100% { color: #ff3300; }
        }
        @keyframes text3D {
            0%, 100% { transform: translate3d(1px, 1px, 0px); }
            25% { transform: translate3d(-2px, 2px, 1px); }
            50% { transform: translate3d(2px, -2px, 2px); }
            75% { transform: translate3d(-1px, -1px, 1px); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
          𝗙𝗥𝗘𝗘 𝗜𝗡𝗧𝗘𝗥𝗡𝗘𝗧 🔥 \n𝗞𝗛𝗔𝗟𝗜𝗟 👑
        </div>
        <hr size="1" width="100%" align="left" color="blue">
        <div class="file-select">
            <label for="config-type">اختر نوع VPN</label>
            <select id="config-type" onchange="toggleFileList()">
                <option value="">اختر نوع التطبيق...</option>
                {% for config_type in config_files %}
                    <option value="{{ config_type }}">{{ config_type }}</option>
                {% endfor %}
            </select>
        </div>
        <div id="file-options" class="file-list" style="display: none;">
            {% for config_type, files in config_files.items() %}
                <div id="{{ config_type }}-files" class="file-list-group" style="display: none;">
                    <h3>
                        <img src="{% if config_type == 'HTTP_CUSTOM' %}https://images.squarespace-cdn.com/content/v1/5b7257d68ab7222baffba243/93300b11-86f1-48f3-8a05-6b197b0f710b/HeroLightLogo.png{% elif config_type == 'Dark_Tunnel' %}https://play-lh.googleusercontent.com/Ax34UpElSZmCPzKIIzf0m_vqMPQmAartTHzkMx3dZ3c5a3wWCfA6CcsJgOi4ob36PSmG{% endif %}" alt="{{ config_type }} Icon" class="icon">
                        {{ config_type }}
                    </h3>
                    {% for file in files %}
                        <div class="file-item">
                            <span>{{ file }}</span>
                            <button onclick="window.location.href='/download/{{ config_type }}/{{ file }}'">تنزيل</button>
                        </div>
                    {% endfor %}
                </div>
            {% endfor %}
        </div>
        <a href="https://t.me/khalil_vip1" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram Icon" class="telegram-icon">
        </a>
        <div class="animated-name">
            ⓀⒽⒶⓁⒾⓁ
        </div>
    </div>

    <script>
        function toggleFileList() {
            var selectedType = document.getElementById("config-type").value;
            var fileOptions = document.getElementById("file-options");
            var fileListGroups = document.querySelectorAll(".file-list-group");

            fileListGroups.forEach(function(group) {
                group.style.display = "none";
            });

            if (selectedType !== "") {
                document.getElementById(selectedType + "-files").style.display = "block";
            } else {
                fileOptions.style.display = "none";
            }
        }

        document.getElementById("config-type").addEventListener("change", function() {
            var fileOptions = document.getElementById("file-options");
            fileOptions.style.display = this.value ? "block" : "none";
        });
    </script>
</body>
</html>

"""

if __name__ == '__main__':
    app.run(debug=False)