import os

# 1. सैंपल बैंक डेटा
banks_data = [
    {
        "bank": "State Bank of India",
        "ifsc": "SBIN0000152",
        "branch": "Patna Main Branch",
        "city": "Patna",
        "district": "Patna",
        "state": "Bihar",
        "address": "West Gandhi Maidan, Patna, Bihar 800001"
    },
    {
        "bank": "Punjab National Bank",
        "ifsc": "PUNB0011200",
        "branch": "Kankarbagh",
        "city": "Patna",
        "district": "Patna",
        "state": "Bihar",
        "address": "Old Bypass Road, Kankarbagh, Patna 800020"
    },
    {
        "bank": "HDFC Bank",
        "ifsc": "HDFC0000262",
        "branch": "Boring Road",
        "city": "Patna",
        "district": "Patna",
        "state": "Bihar",
        "address": "Boring Road Crossing, Patna, Bihar 800001"
    }
]

# 2. HTML टेम्पलेट
html_template = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{bank} {branch} IFSC Code - {ifsc}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #f0f2f5; margin: 0; padding: 15px; }}
        .card {{ background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); max-width: 500px; margin: 0 auto; }}
        h1 {{ font-size: 20px; color: #0f172a; margin-top: 0; }}
        .badge {{ background: #e0f2fe; color: #0369a1; padding: 10px; border-radius: 8px; font-weight: bold; font-size: 18px; text-align: center; margin: 15px 0; letter-spacing: 1px; }}
        .row {{ display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #f1f5f9; font-size: 14px; }}
        .label {{ color: #64748b; font-weight: 500; }}
        .val {{ color: #1e293b; font-weight: 600; text-align: right; }}
        .btn {{ display: block; text-align: center; background: #2563eb; color: white; padding: 12px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{bank}</h1>
        <p style="color:#64748b; margin-top:-5px;">शाखा: {branch}</p>
        <div class="badge">IFSC: {ifsc}</div>
        <div class="row"><span class="label">शहर / ज़िला</span><span class="val">{city}, {district}</span></div>
        <div class="row"><span class="label">राज्य</span><span class="val">{state}</span></div>
        <div class="row"><span class="label">पता</span><span class="val">{address}</span></div>
        <a href="https://wa.me/?text={bank}%20{branch}%20IFSC%20Code:%20{ifsc}" class="btn">WhatsApp पर शेयर करें</a>
    </div>
</body>
</html>"""

# 3. फाइल जनरेट करें
for item in banks_data:
    filename = f"{item['bank']}-{item['branch']}-{item['ifsc']}".lower().replace(" ", "-") + ".html"
    
    content = html_template.format(
        bank=item["bank"],
        branch=item["branch"],
        ifsc=item["ifsc"],
        city=item["city"],
        district=item["district"],
        state=item["state"],
        address=item["address"]
    )
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"तैयार हुआ: {filename}")

print("\nसारे वेब पेज आपके फोन में बन गए हैं!")
